import socket
import getpass
import os
from plumbum.cmd import ssh
from fabric import task


def get_available_port(c):
    # get remote available ports
    remote_ports = get_remote_available_ports(c)

    # check if a local port is in a remote port
    for local_port in get_local_available_port():
        if local_port in remote_ports:
            return local_port


def get_remote_available_ports(c):
    port_cmd = c.run("nc -z -v 127.0.0.1 2220-2300 2>&1 | grep refused | cut -d ' ' -f 6", hide=True)
    # return available_port
    return port_cmd.stdout.split("\n")


# check if there are any available ports
def get_local_available_port(start_port=2222):
    available_ports = []

    # check all ports between start_port and 60000
    for port in range(start_port, 2300):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            s.connect(("127.0.0.1", port))
            s.close()
            continue
        except:
            s.close()
            available_ports.append(str(port))

    return available_ports


@task()
def remote_mount(c, workstation_dir, server_dir):
    if not hasattr(c, "host"):
        print("please give up a host using -H")
        exit(255)

    # get an available port that is usable on local and remote so we can setup a connection with the ports
    port = get_available_port(c)
    ssh_cmd = ssh["-A", f"-R {port}:127.0.0.1:22", f"{c.user}@{c.host}"]
    sshfs_cmd = ssh_cmd["sshfs", f"-p {port}", "-o default_permissions",
                        "-o StrictHostKeyChecking=no", "-oauto_cache,reconnect",
                        f"{getpass.getuser()}@127.0.0.1:{workstation_dir}", f"{server_dir}"]

    print(f"running: {str(sshfs_cmd)}")
    print(sshfs_cmd())


# process = subprocess.Popen(f"sshfs -v -p {available_port} -o default_permissions {c.user}@127.0.0.1:{workstation_dir} {server_dir}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# subprocess.Popen(f"ssh -A -R {available_port}:127.0.0.1:22 {c.user}@{c.host}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
