
# coding: utf-8

# # Opening a data file

# # Document
# 
# <table align="left">
#     <tr>
#         <th class="text-align:left">Title</th>
#         <td class="text-align:left">Opening a data file</td>
#     </tr>
#     <tr>
#         <th class="text-align:left">Last modified</th>
#         <td class="text-align:left">2019-01-04</td>
#     </tr>
#     <tr>
#         <th class="text-align:left">Author</th>
#         <td class="text-align:left">Gilles Pilon <gillespilon13@gmail.com></td>
#     </tr>
#     <tr>
#         <th class="text-align:left">Status</th>
#         <td class="text-align:left">Active</td>
#     </tr>
#     <tr>
#         <th class="text-align:left">Type</th>
#         <td class="text-align:left">Jupyter notebook</td>
#     </tr>
#     <tr>
#         <th class="text-align:left">Created</th>
#         <td class="text-align:left">2018-12-21</td>
#     </tr>
#     <tr>
#         <th class="text-align:left">File name</th>
#         <td class="text-align:left">N/A</td>
#     </tr>
#     <tr>
#         <th class="text-align:left">Other files required</th>
#         <td class="text-align:left">N/A</td>
#     </tr>
# </table>

# # Files
# 
# The files for this notebook are here:
# 
# https://drive.google.com/open?id=1bA-phCp2FxNYLxU3YqcTh2w8e26BnCN1

# In[ ]:


# Open a csv file: cloquet_two_weeks_60_min.csv.
# This file has 30 columns.
# The first column is date and time in ISO 8601 format.
# The first row is the column label.
# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html


# In[ ]:


# Import the pandas library of data structures and data analysis tools.
import pandas as pd


# In[ ]:


# df is a variable in which we store the csv file as a dataframe.
# A dataframe is a two-dimensional labeled data structure with columns of potentially
# different types. Think of it as a worksheet in an Excel workbook.
df = pd.read_csv('cloquet_two_weeks_60_min.csv',
                 parse_dates=True,
                 index_col='Time')


# In[ ]:


# Look at the first few rows and columns.
df.head()


# In[ ]:


# Look at the last few rows and columns.
df.tail()


# In[ ]:


# Look at the first 10 rows and columns.
df.head(10)


# In[ ]:


# How many rows and columns?
df.shape


# In[ ]:


# Show the number of cells, that is, columns x rows.
df.size


# In[ ]:


# Show the Index column and the column labels.
df.axes


# In[ ]:


# Show the index column.
df.index


# In[ ]:


# show the column lables, excluding the Index
df.columns


# In[ ]:


# Show the column types
df.dtypes


# In[ ]:


# Open an Excel file: cloquet_two_weeks_60_min.xlsx.
# This is the same as the previous csv file.
df2 = pd.read_excel('cloquet_two_weeks_60_min.xlsx',
                    parse_dates=True,
                    index_col='Time')


# In[ ]:


# And the same operations as above can be performed.
df2.head()


# In[ ]:


# Open an Excel file with multiple worksheets.
# There are three worksheets:
# two_weeks_15_min
# two_weeks_30_min
# two_weeks_60_min
# The first four rows are variables user labels and notes.
# The column labels start in the fifth row.
df3 = pd.read_excel('cloquet_multiple.xlsx',
                    sheet_name='two_weeks_60_min',
                    parse_dates=True,
                    skiprows=4,
                    index_col='Time')


# In[ ]:


# You can do the same operations as before.
df3.head()


# In[ ]:


# What is your file is in a directory and not in the same place as this notebook?
df = pd.read_csv('data_files/just_another_file.csv',
                 parse_dates=True,
                 index_col='Time')


# In[ ]:


df.head()

