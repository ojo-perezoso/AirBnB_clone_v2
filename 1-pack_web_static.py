#!/usr/bin/python3
"""First use of Fabric"""
from os import path
from fabric.api import local
from datetime import datetime

def do_pack():
    """Turns the web_static forlder into a .tgz file"""
    if path.isdir('web_static'):
        local('sudo mkdir versions')
        cmd = "tar -cfzv versions/web_static_$(date '+%Y-%m-%d-%H-%M-%s').tgz\
                web_static"
        return(local(cmd))
