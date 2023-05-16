from fabric import task
import socket


# check if there are any available ports
def get_available_port(start_port=2222):
    # check all ports between start_port and 60000
    for port in range(start_port, 60000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)  # Timeout in case of port not available
        try:
            s.connect(("127.0.0.1", port))  # localhost. Port, here 2222 is port
            s.close()
            continue
        except:
            s.close()
            return port


@task()
def local_to_remote():
    ...


@task()
def available_port(c):
    print(get_available_port())


