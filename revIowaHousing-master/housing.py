#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 23:44:51 2020

@author: srwight
"""
import pandas as pd
import os, importlib

modules = []
for module in os.listdir(os.getcwd()):
    if '.py' in module:
        modules.append(importlib.import_module(module.replace('.py', '')))

def main():
    #read our training data
    df_init = pd.read_csv('train.csv')
    
    #apply feature engineering
    df_ext = modules[0].feature_extract(df_init)
    for module in modules:
        if module == modules[0] or module.__name__ == 'housing':
            continue
        print(module.__name__)
        df_ext = pd.concat([df_ext, module.feature_extract(df_init)], axis=1)
    
    #see what we did
    print(df_ext)
    
if __name__ == '__main__':
    main()