#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
import versioneer

setup(
    name='ibapi-grease',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description='Monkey patches to grease the Interactive Brokers Python API',
    maintainer='QuantRocket LLC',
    maintainer_email='support@quantrocket.com',
    url='https://github.com/quantrocket-llc/ibapi-grease',
    license='Apache 2.0',
    packages=['ibapi_grease']
)
