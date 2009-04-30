# /*---------------------------------------------------------------------*\
# * Copyright (c) 2009, Alexander Kreschenko, alexander.kross @ gmail.com *
# * All rights reserved. This file may be redistributed under GPL ver. 2. *
# \*---------------------------------------------------------------------*/

include "../Cont/CyCont.pyx"

#from CyCont cimport *

cdef extern from "InfoDef.h":
    ctypedef struct Cell:
        Ident Id
        Index BIdx

    enum:
        c_IntBits    "INTBITS"
        c_DataBits   "DATABITS"
        c_DataMax    "INT_MAX"
        c_NA         "NA"      #DATA_MAX
        c_BaseBits   "BASEBITS"
        c_WgtMin     "WGT_MIN"
        c_WgtMax     "WGT_MAX"
        c_WgtNorm    "WGT_NORM"
        c_WgtBase    "WGT_BASE"
        c_FncSpecMax "FNC_SPEC_MAX"

        c_IntBits    "INTBITS"
        c_DataBits   "DATABITS"
        c_BaseBits   "BASEBITS"
        c_WgtMin     "WGT_MIN"
        c_WgtMax     "WGT_MAX"
        c_WgtNorm    "WGT_NORM"
        c_WgtBase    "WGT_BASE"
        c_FncSpecMax "FNC_SPEC_MAX"


IntBits = c_IntBits
