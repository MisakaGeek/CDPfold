#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 11:25:12 2018

@author: zhangch
"""

from __future__ import division
import os
from PIL import Image 
import scipy.misc

source_path = '/home/zhangch/RSS/tRNA/train_labelpng2/'

aim_path = '/home/zhangch/RSS/train_set/'

if __name__ == "__main__":
    pathDir = os.listdir(source_path)
    for i in pathDir:
        #print source_path+i
        image = Image.open(source_path+i)
        image = image.resize((128,19))
        scipy.misc.imsave(aim_path+i, image)

