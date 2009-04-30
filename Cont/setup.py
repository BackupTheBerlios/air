# /*---------------------------------------------------------------------*\
# * Copyright (c) 2005, Alexander Kreschenko (e-mail: akr<at>berlios.de). *
# * All rights reserved. This file may be redistributed under GPL ver. 2. *
# \*---------------------------------------------------------------------*/

rcsid="$Id:$";

"""Cont API core and Python wrappers.

Note: current version tested on Windows and Linux platforms.
"""

from distutils.core import setup, Extension
import sys

sys_comp_opts = {'win32' : ['/Od', '/MDd', '/RTC1'], #/ZI (/Z7 should be enough), /RTC1 (run-time checks) == /GZ, /GX == /EHsc
            'linux2' : ['-O0', '-ggdb', '-g3', '-coverage', '-Wall', '-pedantic', '-MMD', '-dD', '-std=c9x', '-ftabstop=2', '-H']}
# '-save-temps', - kills Cont.i, see also -fpch-preprocess and -fpreprocessed, work if TMPDIR is set

sys_link_opts = {'win32' : ['/DEBUG'],
                 'linux2' : ['--noinhibit-exec', '--warn-common', '--warn-once', '--export-all-symbols']}

sys_defs = {'win32' : [],
            'linux2' : []}

sys_swig_opts = {'win32' : ['-Fmicrosoft'],
                 'linux2' : []}

setup(name = 'akr',
      version = '0.2.0',
      description = "AKR`s AIR Cont sub-project Python wrappers",
      #long_description = '',
      author = 'Alexander Kreschenko',
      author_email = 'akr<at>berlios.de',
      url = 'http://air.berlios.de/python/',
      package_dir = {'akr': ''},
      ext_package = 'akr',
      ext_modules = [Extension('cont',
                               ['Cont.c', 'ContCet.c', 'Clash.c', 'ContInit.c', 'MemMan.c', '../Log/Log.c', 'Cont.i'], 
                               #module_pkg = 'akr',
                               # better place swig.exe in c:\swig1.3: swig = r'\swig\swig.exe',
                               #define_macros=[('LOGGING', None), ('CONT_DBG', None), ('_POSIX_', None), ('CONT_API', '')],
                               # None value expands to 1, whereas '' to empty.
                               define_macros=[('CONT_API', '')], #WITH_CET
                               extra_compile_args = sys_comp_opts[sys.platform],
                               extra_link_args = sys_link_opts[sys.platform],
                               #include_dirs = [r'C:\Python24\include'],
                               #library_dirs = [r'C:\Python24\libs'],
                               swig_opts = ['-O', '-nodirvtable', '-Wall', '-v', '-noproxy', '-nodefaultctor', '-nodefaultdtor', '-modern'] + sys_swig_opts[sys.platform] #hang on '-noproxy', only for Version 1.3.28 (February 12, 2006)
                              )
                    ])
# does not work for MSVC: runtime_library_dirs = ['..\Cont\Debug'],
#libraries = ['Cont']
