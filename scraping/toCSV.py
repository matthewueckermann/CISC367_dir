# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 23:27:09 2021

@author: matth
"""

import pandas as pd

df = pd.read_json("delegates.json")
df.to_csv("delegates.csv",index=False)