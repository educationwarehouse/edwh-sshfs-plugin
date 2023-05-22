# edwh-sshfs-plugin

[![PyPI - Version](https://img.shields.io/pypi/v/edwh-sshfs-plugin.svg)](https://pypi.org/project/edwh-sshfs-plugin)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/edwh-sshfs-plugin.svg)](https://pypi.org/project/edwh-sshfs-plugin)

-----

**Table of Contents**

- [Installation](#installation)
- [Local Mounts](#creating-local-mounts)
- [Remote Mounts](#creating-remote-mounts)
- [License](#license)

## Installation

```shell
pip install edwh-sshfs-plugin
```

But probably you want to install the whole edwh package:

```shell
pipx install edwh[sshfs]
```
or
```shell
pipx install edwh[plugins,omgeving]
```

Also you will be required to run these commands
```shell
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install openssh-client
sudo apt install openssh-server
sudo systemctl enable ssh
sudo apt install sshfs
sudo ufw allow ssh
sudo init 6 #optional for reboot
```

## creating remote mounts
**usage**
```shell
edwh -h {server} sshfs.remote-mount -w {local_dir} -s {server_dir}
```
The remote_mount function is an asynchronous Python task that allows you to mount a remote directory 
on your local machine using SSHFS (SSH Filesystem). It establishes a secure connection to a remote server, 
forwards a port, and mounts the remote directory on the local machine.

**Parameters**
- `workstation_dir`: The local directory path where the remote directory will be mounted to the server_dir.
- `server_dir`: The remote directory path that will become a mount
- `queue`: An optional parameter representing the queue object for synchronization (default: None).

## creating local mounts
**Usage**
```shell
edwh -h {server} sshfs.local-mount -w {local_dir} -s {server_dir}
```

**Arguments**
- `workstation_dir(-w)`: The local directory path That will become a mount
- `server_dir(-s)`: The remote directory path That will be mounted onto the workstation directory
- `queue`: An optional parameter representing the queue object for synchronization (default: None).

## License

`edwh-demo-plugin` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
