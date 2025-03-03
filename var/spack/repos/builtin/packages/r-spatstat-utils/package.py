# Copyright 2013-2022 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class RSpatstatUtils(RPackage):
    """Utility Functions for 'spatstat'.

    Contains utility functions for the 'spatstat' package which may also be
    useful for other purposes."""

    cran = "spatstat.utils"

    version('2.3-0', sha256='5f096ce5a201482d61e6d6859be7d40a55705ba5c6ebadd4875367ef9cb0db1a')
    version('1.20-2', sha256='62c2413f989965a9fa6395742a605004b736a27c24304e6ffaebf2134019ce18')
    version('1.17-0', sha256='39cd683ed7f41d8adc9e28af073d91b244aa1cf5ad966dfbb396ee3ee79f0922')
    version('1.15-0', sha256='90e07d730b6939f47f93c939afae10874b2c82bd402960ede4133de67dca2a0c')

    depends_on('r@3.3.0:', type=('build', 'run'))
