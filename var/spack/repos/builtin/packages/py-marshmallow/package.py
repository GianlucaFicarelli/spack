# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyMarshmallow(PythonPackage):
    """marshmallow is an ORM/ODM/framework-agnostic library for converting
    complex datatypes, such as objects, to and from native Python datatypes."""

    homepage = "https://github.com/marshmallow-code/marshmallow"
    pypi     = "marshmallow/marshmallow-3.15.0.tar.gz"

    maintainers = ['haralmha']

    version('3.15.0', sha256='2aaaab4f01ef4f5a011a21319af9fce17ab13bf28a026d1252adab0e035648d5')

    depends_on('python@3.7:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-packaging', type=('build', 'run'))
