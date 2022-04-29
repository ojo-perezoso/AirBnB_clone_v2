#!/usr/bin/python3
"""First use of Fabric"""
from os import path
from fabric.api import local
from datetime import datetime


def do_pack():
    """Turns the web_static forlder into a .tgz file"""
    if path.isdir('web_static'):
        local('sudo mkdir -p versions')
        d = datetime.now()
        tgz = local(
            "tar -czvf versions/web_static_{}{}{}{}{}{}.tgz web_static".format(
                d.year,
                d.month,
                d.day,
                d.hour,
                d.minute,
                d.second))

        return(tgz)
