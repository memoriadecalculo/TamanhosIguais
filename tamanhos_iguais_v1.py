#!/usr/bin/env python3
# coding: utf-8
'''
@project: TamanhosIguais <https://github.com/memoriadecalculo/TamanhosIguais>
@copyright: Memória de Cálculo (c) 2022 <memoriadcalculo@gmail.com>
'''

import sys, os
#import glob

def checkfile(fl, dir, files):
    imgext = (".jpg",".png",".gif",".bmp")
    for file in files:
        filepath = os.path.join(dir, file)
        fileext = os.path.splitext(file)[1]
        if os.path.isfile(filepath) and fileext in imgext:
            if fl.has_key(file):
                fl[file] = fl[file] + ((filepath, os.path.getsize(filepath)))
            else:
                fl[file] = ((filepath, os.path.getsize(filepath)),)

#glob.glob(lookdir)
lookdir = os.path.join(os.getenv('HOME'),'Imagens')
filelist = {}
os.path.walk(lookdir, checkfile, filelist)
