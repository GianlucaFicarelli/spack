# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyHepMl(PythonPackage):
    """Machine Learning for High Energy Physics"""

    homepage = "https://github.com/arogozhnikov/hep_ml"
    pypi     = "hep_ml/hep_ml-0.7.0.tar.gz"

    version('0.7.0', sha256='0402037064d78f5723106b385ad5f20df8f67cb312c57cb4ce3839c5616f328e')

    depends_on('py-setuptools',         type='build')
    depends_on('py-numpy@1.9:',         type=('build', 'run'))
    depends_on('py-scipy@0.15.0:',      type=('build', 'run'))
    depends_on('py-pandas@0.14.0:',     type=('build', 'run'))
    depends_on('py-scikit-learn@0.19:', type=('build', 'run'))
    depends_on('py-theano@1.0.2:',      type=('build', 'run'))
    depends_on('py-six',                type=('build', 'run'))
