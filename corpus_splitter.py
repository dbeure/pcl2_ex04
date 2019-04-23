#!/usr/bin/env python3
#-*- coding: utf-8 -*-


import gzip as gz
from lxml import etree

def split_corpus(infile, targetdir, n):   #, targetdir, n
    training_path = targetdir + "/abstracts.txt.training.gz"
    test_path = targetdir + "/abstracts.txt.test.gz"
    dev_path = targetdir + "/abstracts.txt.development.gz"
    f_training = gz.open(training_path, 'wt')
    f_test = gz.open(test_path, 'wt')
    f_dev = gz.open(dev_path, 'wt')
    doc = etree.iterparse(infile)
    i = 0
    for action, elem in doc:
        if elem.tag == 'title':
            printing = ''
            sentence = next(doc)[1]
            while sentence.tag != 'document':
                if sentence.tag != 'sentence':
                    sentence = next(doc)[1]
                elif sentence.tag == 'sentence':
                    printing += sentence.text + ' '
                    sentence = next(doc)[1]
            printing += '\n'

            if i < n:
                f_dev.write(printing)
            elif i < 2*n-1:
                f_test.write(printing)
            else:
                f_training.write(printing)
            i += 1



infile = gz.open('abstracts.xml.gz')
split_corpus(infile, '/Users/debora/Desktop/Uni_Zurich/2019FS/Computerlinguistik/PCLII/Ubungen/pcl2_ex4/pcl2_ex4', 1000)

"""for i, line in enumerate(infile):
    line.decode('utf-8')
    print(line)"""






