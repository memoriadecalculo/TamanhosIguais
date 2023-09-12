#!/usr/bin/env python3
# coding: utf-8
'''
@project: TamanhosIguais <https://github.com/memoriadecalculo/TamanhosIguais>
@copyright: Memória de Cálculo (c) 2022 <memoriadcalculo@gmail.com>
'''

import sys, os
#import glob

def CheckDuplicatedFiles(dupfiles, dir, files):
    buffl = {}
    imgext = (".jpg",".png",".gif",".bmp")
    for file in files:
        filepath = os.path.join(dir, file)
        fileext = os.path.splitext(file)[1]
        if os.path.isfile(filepath) and fileext in imgext:
            if buffl.has_key(file):
                if dupfiles.has_key(file):
                    dupfiles[file] = dupfiles[file] + ((filepath, os.path.getsize(filepath)))
                else:
                    dupfiles[file] = buffl[file] + ((filepath, os.path.getsize(filepath)))
            else:
                buffl[file] = ((filepath, os.path.getsize(filepath)),)

#glob.glob(lookdir)
lookdir = os.path.join(os.getenv('HOME'),'Imagens')
DuplicatedFilesList = {}
os.path.walk(lookdir, CheckDuplicatedFiles, DuplicatedFilesList)
