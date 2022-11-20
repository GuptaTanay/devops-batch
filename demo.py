# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 23:02:29 2022

@author: tanay
"""

# package: is basically collection of python programs
# module: is  a collection of packages

import pandas as pd

data = pd.read_csv('bank.csv')
# print(data.columns)
# print(data.dtypes)
# print(data.select_dtypes('O'))


data.rename(columns= {'job': 'jobs'}, inplace= True)
data.drop(columns= ['jobs'], inplace= True)
df = data['age']

adults = data.loc[data['age']>18]

max_age = data.age.max()
min_age = data.age.min()
mean_age = data.age.mean()
median_age = data.age.median()


# h.w. --> read the csv file and tell me what are the diffrent job title in the data?
# how to solve this in python
# -----------------------------------------------------------------
a = {'age':21, 'name':'abc', 'marrital_status': 'single'}
print(a.keys())
print(a.items())
print(a.values())


a = {1,1,1,2,3,45,6,6}
print(a)
