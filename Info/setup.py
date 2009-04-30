# /*---------------------------------------------------------------------*\
# * Copyright (c) 2005, Alexander Kreschenko (e-mail: akr<at>berlios.de). *
# * All rights reserved. This file may be redistributed under GPL ver. 2. *
# \*---------------------------------------------------------------------*/

rcsid="$Id:$";

"""Info API core and Python wrappers.

Note: current version tested on Windows and Linux platforms.
"""

from distutils.core import setup, Extension
from Cython.Distutils import build_ext

import sys

sys_comp_opts = {'win32' : ['/Od', '/MDd', '/RTC1'], #/ZI (/Z7 should be enough), /RTC1 (run-time checks) == /GZ, /GX == /EHsc
            'linux2' : ['-O0', '-ggdb', '-g3', '-Wall', '-pedantic', '-MMD', '-dD', '-std=c9x', '-ftabstop=2', '-H']}
# '-coverage' cause ImportError: /root/Info/info.so: undefined symbol: __gcov_merge_add 
# '-save-temps', - kills Cont.i, see also -fpch-preprocess and -fpreprocessed, work if TMPDIR is set

sys_link_opts = {'win32' : ['/DEBUG'],
                 'linux2' : ['--noinhibit-exec', '--warn-common', '--warn-once', '--export-all-symbols']}

sys_defs = {'win32' : [],
            'linux2' : []}

#sys_swig_opts = {'win32' : ['-Fmicrosoft'],
#                 'linux2' : []}

log_srcs = ('../Log/' + src for src in ('Log.c',))
cont_srcs = ('../Cont/' + src for src in ('Cont.c', 'ContCet.c', 'Clash.c', 'ContInit.c', 'MemMan.c')) #, 'CyCont.pyx' cause doule init_info() definition from ../Cont/CyCont.c
srcs = ['Info.c', 'InfoEx.c']
srcs.extend(cont_srcs)
srcs.extend(log_srcs)
#srcs.append('Info.i')
srcs.append('CyInfo.pyx')

setup(name = 'akr',
      version = '0.3.0',
      description = "AKR`s AIR Info sub-project Python wrappers",
      #long_description = '',
      author = 'Alexander Kreschenko',
      author_email = 'akr<at>berlios.de',
      url = 'http://air.berlios.de/python/',
      cmdclass = {'build_ext': build_ext},
      package_dir = {'akr': ''},
      ext_package = 'akr',
      ext_modules = [Extension('info', srcs,
                               #module_pkg = 'akr',
                               define_macros=[('CONT_API', ''), ('INFO_API', '')],
                               extra_compile_args = sys_comp_opts['linux2'], # linux2 is for -c mingw32, was: sys.platform
                               extra_link_args = sys_link_opts['linux2'], # linux2 is for -c mingw32, was: sys.platform
                               #library_dirs = ['/usr/lib/gcc/i386-redhat-linux/4.3.0'],
                               include_dirs = ['../Cont', '.']
                               #libraries = ['libgcov'],
                               #swig_opts = ['-O', '-nodirvtable', '-Wall', '-v', '-noproxy', '-nodefaultctor', '-nodefaultdtor', '-modern'] + sys_swig_opts[sys.platform] #hang on '-noproxy', only for Version 1.3.28 (February 12, 2006)
# does not work for MSVC: runtime_library_dirs = ['../Cont/Debug'],
                              )
                    ])
