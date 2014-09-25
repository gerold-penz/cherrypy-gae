#!/usr/bin/env python
# coding: utf-8
"""
Cherrypy Google App Engine Tools - Setup
 
Created
    2014-09-25 by Gerold - http://halvar.at/
"""

import os
from setuptools import setup, find_packages

THISDIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(THISDIR)

VERSION = open("version.txt").readline().strip()
HOMEPAGE = "https://github.com/gerold-penz/cherrypy-gae"
DOWNLOAD_BASEURL = "https://github.com/gerold-penz/cherrypy-gae/raw/master/dist/"
DOWNLOAD_URL = DOWNLOAD_BASEURL + "cherrypy-gae-%s.tar.gz" % VERSION


setup(
    name = "cherrypy-gae",
    version = VERSION,
    description = (
        "Cherrypy Google App Engine Tools"
    ),
    long_description = open("README.rst").read(),
    keywords = (
        "Google App Engine, Server, HTTP-Server, Cherrypy, WSGI, CGI"
    ),
    author = "Gerold Penz",
    author_email = "gerold@halvar.at",
    url = HOMEPAGE,
    download_url = DOWNLOAD_URL,
    packages = find_packages(),
    classifiers = [
        "Development Status :: 1 - Planning",
        # "Development Status :: 2 - Pre-Alpha",
        # "Development Status :: 3 - Alpha",
        # "Development Status :: 4 - Beta",
        # "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Networking",
        "Topic :: Internet :: WWW/HTTP",
    ],
    install_requires = ["bunch", "cherrypy"],
)

