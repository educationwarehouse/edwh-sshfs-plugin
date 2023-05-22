import os
import socket
import invoke
from edwh_sshfs_plugin import fabfile
from fabric import Connection
import time
import subprocess
from multiprocessing import Process
import asyncio
import pytest
import logging

pytest_plugins = ("pytest_asyncio",)


def create_new_fabric_connection(host) -> Connection:
    try:
        connection = Connection(host=host)
    except:
        assert False, f"not able to connect to host({host})"
    return connection


def is_given_host_valid(host):
    assert "@" in host, "@ not given in --host parameter"


def test_is_port_open():
    assert fabfile.get_local_available_port() == fabfile.get_local_available_port()
    s = socket.socket()
    open_port = fabfile.get_local_available_port()
    s.bind(("127.0.0.1", int(open_port[0])))
    s.listen(5)
    assert open_port != fabfile.get_local_available_port()
    s.close()


def test_ssh_connection(host):
    conn = create_new_fabric_connection(host)
    # no need for assert here because it will throw an exception if the ssh connection is wrong when executing ls
    conn.run("ls", hide=True)


async def check_if_mount_exists(host):
    await asyncio.sleep(3)
    conn_for_mount = create_new_fabric_connection(host)
    assert (
        "is a mount"
        in conn_for_mount.run("mountpoint test_sshfs_dir", warn=True, hide=True).stdout
    )
    conn_for_mount.close()

@pytest.mark.asyncio
async def test_remote_mount(host):
    create_mount_conn = create_new_fabric_connection(host)
    if create_mount_conn.run("if test -d test_sshfs_dir; then echo \"exist\"; fi", warn=True, hide=True).stdout == "":
        # print(create_mount_conn.run("ls test_sshfs_dir", warn=True, hide=True).stdout == "")
        # return
        create_mount_conn.run("mkdir test_sshfs_dir", hide=True)

    shared_queue = asyncio.Queue()

    create_mount_task = asyncio.create_task(
        fabfile.remote_mount(
            create_mount_conn, f"{os.getcwd()}/tests/sshfs_test_dir", "test_sshfs_dir", shared_queue
        )
    )

    asyncio.gather(create_mount_task)
    await asyncio.sleep(5)

    conn_for_mount = create_new_fabric_connection(host)
    assert (
            "is a mount"
            in conn_for_mount.run("mountpoint test_sshfs_dir", warn=True, hide=True).stdout
    )
    # print(conn_for_mount.run("mountpoint test_sshfs_dir", warn=True, hide=True).stdout)
    # tell remote_mount to stop running
    await shared_queue.put(True)
    shared_queue.join()
    await asyncio.sleep(1)
    conn_for_mount.close()
    create_mount_conn.close()

    c = create_new_fabric_connection(host)

    assert (
        "is a mount"
        not in c.run("mountpoint test_sshfs_dir", warn=True, hide=True).stdout
    )


async def check_local_folder_for_mount():
    await asyncio.sleep(3)

    conn = invoke.context.Context()
    assert (
        "is a mount"
        in conn.run("mountpoint test_sshfs_dir", warn=True, hide=True).stdout
    )
    conn.close()


@pytest.mark.asyncio
async def test_local_mount(host):
    create_mount_conn = create_new_fabric_connection(host)
    create_mount_conn.run("umount test_sshfs_dir", warn=True, hide=True)
    shared_queue = asyncio.Queue()

    create_mount_task = asyncio.create_task(
        fabfile.local_mount(
            create_mount_conn, f"{os.getcwd()}/tests/sshfs_test_dir", "test_sshfs_dir", shared_queue
        )
    )

    asyncio.gather(create_mount_task)

    await asyncio.sleep(5)

    conn = invoke.context.Context()
    assert (
            "is a mount"
            in conn.run(f"mountpoint {os.getcwd()}/tests/sshfs_test_dir", warn=True, hide=True).stdout
    )

    await shared_queue.put(True)
    shared_queue.join()
    await asyncio.sleep(1)

    assert (
            "is a mount"
            not in conn.run(f"mountpoint {os.getcwd()}/tests/sshfs_test_dir", warn=True, hide=True).stdout
    )