#! /usr/bin/env python3

'''
This script reads a raw data file, creates box plots, histograms, and scatter
plots of float and integer columns.

time -f '%e' ./09_script.py > 09_script.txt
./09_script.py > 09_script.txt
./09_script.py | tee 09_script.txt
'''


from shutil import rmtree
from pathlib import Path
from multiprocessing import Pool


import pandas as pd
import matplotlib.axes as axes
import matplotlib.pyplot as plt


def read_data():
    df = pd.read_csv('data/norfolk.csv',
                     parse_dates=True,
                     index_col='LAB_BOARD_DAT_COD')
    print(df.shape)
    print(df.size)
    print(df.index)
    print(df.dtypes)
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
    return df


def prepare_data(df):
    df = df.dropna(how='all', axis=1)
    df = df.dropna(how='all', axis=0)
    pd.DataFrame(list(df)).to_csv('data/column_names.csv',
                                  header=False,
                                  index=False)
    not_null = sorted({
        column_name
        for column_name
        in df.columns
        if (df[column_name].dtype in (float, int) and not
            df[column_name].isnull().all())
    })
    return df, not_null


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
    ds.despine(ax)
    ax.figure.savefig(
        fname=f'graphics/scatter_plot_{column_name}.png',
        format='png'
    )
    plt.close('all')


def plot_box_plot(column_name: str) -> None:
    ax = df.plot.box(y=column_name,
                     notch=True)
    ax.set_ylabel(column_name)
    ds.despine(ax)
    ax.figure.savefig(
        fname=f'graphics/box_plot_{column_name}.png',
        format='png'
    )
    plt.close('all')


def plot_histogram(column_name: str) -> None:
    pass


if __name__ == '__main__':
    df = read_data()
    df, not_null = prepare_data(df)
    # for column_name in df.columns:
    #     if df[column_name].dtype == float:
    #         plot_scatter(column_name)
    #     else:
    #         pass
    # plt.close('all')

#     for column_name in df.columns:
#         if df[column_name].dtype == float:
#             ax = df.plot.box(y=column_name,
#                              notch=True)
#             ax.set_ylabel(column_name)
#             ds.despine(ax)
#             ax.figure.savefig(
#                 fname=f'graphics/box_plot_{column_name}.png',
#                 format='png'
#             )
#         else:
#             pass
#     plt.close('all')

    for column_name in df.columns:
        if df[column_name].dtype == float:
            ax = df.plot.hist(y=column_name,
                              legend=False)
            ax.set_xlabel(xlabel=column_name)
            ds.despine(ax)
            ax.figure.savefig(
                fname=f'graphics/histogram_{column_name}.png',
                format='png'
            )
        else:
            pass
    plt.close('all')

    with Pool() as pool:
        for _ in pool.imap_unordered(plot_scatter, not_null):
            pass
        for _ in pool.imap_unordered(plot_box_plot, not_null):
            pass
