import os
import socket
import invoke
from edwh_sshfs_plugin import fabfile
from fabric import Connection
import pytest
import anyio

pytest_plugins = ("pytest_anyio",)


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
    await anyio.sleep(3)
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
        create_mount_conn.run("mkdir test_sshfs_dir", hide=True)

    event = anyio.Event()

    async with anyio.create_task_group() as tg:
        create_mount_task = tg.start_soon(
            fabfile.async_remote_mount,
            create_mount_conn,
            f"{os.getcwd()}/tests/sshfs_test_dir",
            "test_sshfs_dir",
            event
        )

        await anyio.sleep(5)

        conn_for_mount = create_new_fabric_connection(host)
        assert (
                "is a mount"
                in conn_for_mount.run("mountpoint test_sshfs_dir", warn=True, hide=True).stdout
        )

        await anyio.maybe_async(event.set())  # Trigger the event to continue execution in async_remote_mount

        await tg.cancel_scope.cancel()

        await anyio.sleep(1)
        conn_for_mount.close()
        create_mount_conn.close()


@pytest.mark.anyio
async def test_local_mount(host):
    create_mount_conn = create_new_fabric_connection(host)
    create_mount_conn.run("umount test_sshfs_dir", warn=True, hide=True)

    event = anyio.Event()

    async with anyio.create_task_group() as tg:
        tg.start_soon(fabfile.async_local_mount, create_mount_conn, f"{os.getcwd()}/tests/sshfs_test_dir", "test_sshfs_dir", event)

        await anyio.sleep(5)

        conn = invoke.context.Context()
        assert (
            "is a mount"
            in conn.run(f"mountpoint {os.getcwd()}/tests/sshfs_test_dir", warn=True, hide=True).stdout
        )

        await anyio.maybe_async(event.set())
        await anyio.sleep(1)

        assert (
            "is a mount"
            not in conn.run(f"mountpoint {os.getcwd()}/tests/sshfs_test_dir", warn=True, hide=True).stdout
        )