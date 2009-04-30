# /*---------------------------------------------------------------------*\
# * Copyright (c) 2009, Alexander Kreschenko, alexander.kross @ gmail.com *
# * All rights reserved. This file may be redistributed under GPL ver. 2. *
# \*---------------------------------------------------------------------*/

cdef extern from "ContDef.h":
    enum:
        c_DataMax    "DATA_MAX"
        c_NA         "NA"

    ctypedef int  Data
    ctypedef Data Ident
    ctypedef Data Index
