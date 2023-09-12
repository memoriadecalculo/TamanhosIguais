#!/usr/bin/env python3
# coding: utf-8
'''
@project: TamanhosIguais <https://github.com/memoriadecalculo/TamanhosIguais>
@copyright: Memória de Cálculo (c) 2022 <memoriadcalculo@gmail.com>
'''

import sys, os
#import glob

def CheckDuplicatedFiles(dupfiles, dir, files):
    for file in files:
        filepath = os.path.join(dir, file)
        fileext = os.path.splitext(file)[1]
        if os.path.isfile(filepath) and fileext in imgext:
            if buffl.has_key(file):
                if dupfiles.has_key(file):
                    dupfiles[file] = dupfiles[file] + ((filepath, os.path.getsize(filepath)),)
                else:
                    dupfiles[file] = (buffl[file], (filepath, os.path.getsize(filepath)))
            else:
                buffl[file] = (filepath, os.path.getsize(filepath))
    

#glob.glob(lookdir)
buffl = {}
imgext = (".jpg",".png",".gif",".bmp")
lookdir = os.path.join(os.getenv('HOME'),'Imagens')
DuplicatedFilesList = {}
os.path.walk(lookdir, CheckDuplicatedFiles, DuplicatedFilesList)
resultdir = os.path.join(lookdir,'dupfiles')
ofile = open(os.path.join(resultdir,'resume.txt'), 'w')
for item in DuplicatedFilesList.keys():
    itemdir = os.path.join(resultdir,os.path.splitext(item)[0])
    os.makedirs(itemdir)
    for index in range(0, len(DuplicatedFilesList[item]), 1):
        print 
        print os.path.join(itemdir,"dupfile"+str(index))
        os.link(DuplicatedFilesList[item][index][0],os.path.join(itemdir,"dupfile"+str(index)))
        
        if index == 0:
            ofile.write('%s' % (item))
        ofile.write('%s;%s' % (DuplicatedFilesList[item][index][0],DuplicatedFilesList[item][index][1]))
        if index == len(DuplicatedFilesList[item]):
            ofile.write('\n')
        
            
    

#TODO:
# Separar em grandes chances de serem iguais e talvez pelo tamanho
# Fazer listagem de resumo
