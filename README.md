# edwh-demo-plugin

[![PyPI - Version](https://img.shields.io/pypi/v/edwh-demo-plugin.svg)](https://pypi.org/project/edwh-demo-plugin)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/edwh-demo-plugin.svg)](https://pypi.org/project/edwh-demo-plugin)

-----

**Table of Contents**

- [Installation](#installation)
- [License](#license)

## USING THIS TEMPLATE REPOSITORY
1. remove this markdown section;
2. replace 'demo' in README.md, pyproject.toml and the name of the plugin in `src` to your actual plugin name;
3. (add your actual plugin code of course);
4. run `semantic-release publish`, `hatch build -c` and `hatch publish`.

## Installation

```console
pip install edwh-demo-plugin
```

But probably you want to install the whole edwh package:

```shell
pipx install edwh[demo]
```
or
```shell
pipx install edwh[plugins,omgeving]
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
