#! /usr/bin/env python3
"""
Write a dataframe to a csv
Write a dataframe to an Excel workbook with one worksheet
Write several dataframs to an Excel workbook as several worksheets
"""

from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl import load_workbook
from openpyxl import Workbook
import datasense as ds
import pandas as pd


df = ds.read_file(
    file_name='data/cloquet_two_weeks_60_min.csv'
)
print(df.head())
print(df.dtypes)
ds.save_file(
    df=df,
    file_name='data/just_a_test.csv'
)
just_a_test = ds.read_file(
    file_name='data/just_a_test.csv'
)
print(just_a_test.head())
df2 = ds.read_file(
    file_name='data/cloquet_two_weeks_30_min.csv'
)
print(df2.head())
df3 = ds.read_file(
    file_name='data/cloquet_two_weeks_15_min.csv'
)
print(df3.head())
wb = Workbook()
ws = wb.active
ws.title = 'sheet_one'
for row in dataframe_to_rows(
    df=df,
    index=False,
    header=True
):
    ws.append(row)
wb.save(filename='data/even_another_file.xlsx')
ws2 = wb.create_sheet(
    title='sheet_two',
    index=1
)
for row in dataframe_to_rows(
    df=df2,
    index=False,
    header=True
):
    ws2.append(row)
ws3 = wb.create_sheet(
    title='sheet_three',
    index=2
)
for row in dataframe_to_rows(
    df=df3,
    index=False,
    header=True
):
    ws3.append(row)
wb.save(filename='data/even_another_file.xlsx')
wb = load_workbook(filename='data/even_another_file.xlsx')
print(wb.sheetnames)
df_one = pd.DataFrame(wb['sheet_one'].values)
print(df_one.head())
df_two = pd.DataFrame(wb['sheet_two'].values)
print(df_two.head())
df_three = pd.DataFrame(wb['sheet_three'].values)
print(df_three.head())
