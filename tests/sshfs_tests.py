# SPDX-FileCopyrightText: 2023-present Remco Boerma <remco.b@educationwarehouse.nl>
#
# SPDX-License-Identifier: MIT
import sys
sys.path.append("..")
from src.edwh_sshfs_plugin import fabfile
sys.path.append("tests")
import pytest
import socket


def test_is_port_open():
    assert fabfile.get_available_port() == fabfile.get_available_port()
    s = socket.socket()
    open_port = fabfile.get_available_port()
    s.bind(("127.0.0.1", open_port))
    s.listen(5)
    assert open_port != fabfile.get_available_port()
    s.close()


def test_is_param_correct(host):
    print(host)