#! /usr/bin/env python3

'''
This script reads a raw data file, creates box plots, histograms, and scatter
plots of float and integer columns.
'''


from shutil import rmtree
from pathlib import Path


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/norfolk.csv',
                 parse_dates=True,
                 index_col='LAB_BOARD_DAT_COD')
print(df.shape)
print(df.size)
print(df.index)

df = df.dropna(how='all', axis=1)
df = df.dropna(how='all', axis=0)

pd.DataFrame(list(df)).to_csv('data/column_names.csv',
                              header=False,
                              index=False)

print(df.dtypes)
print(df.shape)

for column_name in df.columns:
    if df[column_name].dtype == object:
        print(column_name, df[df[column_name].
                              str.contains('[a-z]',
                              na=False)][column_name].unique())

try:
    rmtree('graphics')
except FileNotFoundError:
    pass
Path('graphics').mkdir(parents=True, exist_ok=True)

for column_name in df.columns:
    if df[column_name].dtype == float:
        ax = df.plot.line(y=column_name,
                          legend=False,
                          style='.')
        ax.set_ylabel(column_name)
        ax.figure.savefig(f'graphics/scatter_plot_{column_name}.png',
                          format='png')
    else:
        pass
plt.close('all')

for column_name in df.columns:
    if df[column_name].dtype == float:
        ax = df.plot.box(y=column_name,
                         notch=True)
        ax.set_ylabel(column_name)
        ax.figure.savefig(f'graphics/box_plot_{column_name}.png', format='png')
    else:
        pass
plt.close('all')

for column_name in df.columns:
    if df[column_name].dtype == float:
        ax = df.plot.hist(y=column_name,
                          legend=False)
        ax.set_xlabel(column_name)
        ax.figure.savefig(f'graphics/histogram_{column_name}.png',
                          format='png')
    else:
        pass
plt.close('all')
