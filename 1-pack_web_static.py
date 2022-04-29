#!/usr/bin/python3
"""First use of Fabric"""
from os import path
from fabric.api import local
from datetime import datetime


def do_pack():
    """Turns the web_static forlder into a .tgz file"""
    f = 'web_static'
    if path.isdir(f):
        d = datetime.now()
        cmd = 'tar -cfzv versions/web_static_{}{}{}{}{}{} {}'.format(
                d.year,
                d.month,
                d.day,
                d.hour,
                d.minute,
                d.second,
                f)
        return(local(cmd))
