#! /usr/bin/env python3

'''
This script reads a raw data file, creates box plots, histograms, and scatter
plots of float and integer columns.
'''


from shutil import rmtree
from pathlib import Path


import pandas as pd
import matplotlib.axes as axes
import matplotlib.pyplot as plt


def despine(ax: axes.Axes) -> None:
    '''
    Remove the top and right spines of a graph.

    Used to enforce standard and *correct* style. There is only one x, and one
    y axis, left and bottom, therefore there should only be these axes.
    '''
    for spine in 'right', 'top':
        ax.spines[spine].set_color('none')


def plot_scatter(column_name: str) -> None:
    '''
    Scatter plot of column_name data versu index.
    '''
    ax = df.plot.line(y=column_name,
                      legend=False,
                      style='.',
                      figsize=(9, 6))
    ax.set_ylabel(column_name,
                  fontweight='bold')
#     ax.set_title(f'{column_name} versus index',
#                  fontweight='bold')
#     ax.autoscale(tight=False)
    despine(ax)
    ax.figure.savefig(f'graphics/scatter_plot_{column_name}.png',
                      format='png')
    plt.close('all')


df = pd.read_csv('data/norfolk.csv',
                 parse_dates=True,
                 index_col='LAB_BOARD_DAT_COD')
print(df.shape)
print(df.size)
print(df.index)

df = df.dropna(how='all', axis=1)
df = df.dropna(how='all', axis=0)

not_null_floats = sorted({
    column_name
    for column_name
    in df.columns
    if (df[column_name].dtype in (float, int) and not
        df[column_name].isnull().all())
})

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
        plot_scatter(column_name)
    else:
        pass
# plt.close('all')

for column_name in df.columns:
    if df[column_name].dtype == float:
        ax = df.plot.box(y=column_name,
                         notch=True)
        ax.set_ylabel(column_name)
        despine(ax)
        ax.figure.savefig(f'graphics/box_plot_{column_name}.png', format='png')
    else:
        pass
plt.close('all')

for column_name in df.columns:
    if df[column_name].dtype == float:
        ax = df.plot.hist(y=column_name,
                          legend=False)
        ax.set_xlabel(column_name)
        despine(ax)
        ax.figure.savefig(f'graphics/histogram_{column_name}.png',
                          format='png')
    else:
        pass
plt.close('all')
