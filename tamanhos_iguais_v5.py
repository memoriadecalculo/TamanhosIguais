#!/usr/bin/env python3
# coding: utf-8
'''
@project: TamanhosIguais <https://github.com/memoriadecalculo/TamanhosIguais>
@copyright: Memória de Cálculo (c) 2022 <memoriadcalculo@gmail.com>
'''

import sys, os

# =============================================================================
# Cria a lista de extensões desejadas ExtDes.
# TODO: possibilidade de passar as extensões como parâmetro do script.
ListExtDes = (".jpg",".png",".gif",".bmp")

# =============================================================================
# Cria listagem de arquivos duplicados ListArqDup com extensões desejadas.
# Utiliza a relação de arquivos Arqs presentes no diretório DirAtual,
# a lista de extensões ListExtDes e a lista temporária ListArqDupTmp.
# Definição da ListArqDup e ListArqDupTmp:
# key:  nome do arquivo sem o caminho
# 1o campo ao n campo: vetores com dois subcampos cada, conforme abaixo:
#   1o subcampo: nome do arquivo com o caminho completo
#   2o subcampo: tamanho do arquivo
ListArqDup = {}
ListArqDupTmp = {}
# Cria a lista dos arquivos informando se o tamanho de dois ou mais coincidem.
# Definição:
# 1o campo: tamanhos de dois ou mais arquivos coincidem? (True/False)
ListArqDupTam = {}
def CriaListArqDup(ListArqsDups, DirAtual, Arqs):
    for Arq in Arqs:
        DirArq = os.path.join(DirAtual, Arq)
        ExtArq = os.path.splitext(Arq)[1]
        TamArq = os.path.getsize(DirArq)
        if os.path.isfile(DirArq) and ExtArq in ListExtDes:
            if ListArqDupTmp.has_key(Arq):
                if ListArqsDups.has_key(Arq):
                    ListArqsDups[Arq] = ListArqsDups[Arq] + ((DirArq, TamArq),)
                else:
                    ListArqsDups[Arq] = (False, ListArqDupTmp[Arq], (DirArq, TamArq))
                for ind in range(1, len(ListArqsDups[Arq])-1, 1):
                    if TamArq == ListArqsDups[Arq][ind][1]:
                        ListArqsDups[Arq][0] = True
            else:
                ListArqDupTmp[Arq] = (DirArq, TamArq)

# =============================================================================
# Cria a variável DirVer com diretório a ser verificado.
# TODO: possibilidade de passar o diretório como parâmetro do script.
DirVer = os.path.join(os.getenv('HOME'),'Picasa')

# =============================================================================
# Percorre o diretório DirVer, executando CriaListArqDes em cada subdiretório
# e passando o parâmetro ListArqDup.
#import glob
#glob.glob(lookdir)
os.path.walk(DirVer, CriaListArqDup, ListArqDup)


resultdir = os.path.join(lookdir,'dupfiles')
ofile = open(os.path.join(resultdir,'resume.txt'), 'w')
for item in DuplicatedFilesList.keys():
    itemdir = os.path.join(resultdir,os.path.splitext(item)[0])
    os.makedirs(itemdir)
    for index in range(0, len(DuplicatedFilesList[item]), 1):
        os.link(DuplicatedFilesList[item][index][0],os.path.join(itemdir,"dupfile"+str(index)))
        
        if index == 0:
            ofile.write('%s' % (item))
        ofile.write('%s;%s' % (DuplicatedFilesList[item][index][0],DuplicatedFilesList[item][index][1]))
        if index == len(DuplicatedFilesList[item]):
            ofile.write('\n')
        
            
    
ofile.close()

#TODO:
# Separar em grandes chances de serem iguais e talvez pelo tamanho
# Fazer listagem de resumo
