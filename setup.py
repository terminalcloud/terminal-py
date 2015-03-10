#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup


setup(
  name = 'terminal',
  py_modules = ["terminal", "ez_setup"],
  version = '0.1',
  description = 'Terminal.com API wrapper for python',
  author = 'Enrique Conci',
  author_email = 'e@cloudlabs.io',
  url = 'https://github.com/terminalcloud/terminal-py',
  download_url = 'https://github.com/terminalcloud/terminal-py/archive/master.zip',
  keywords = ['terminal', 'terminal.com', 'API'], # arbitrary keywords
  classifiers = [],
)
