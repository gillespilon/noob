
# coding: utf-8

# # Saving a data file

# # Document
#
# <table align="left">
#     <tr>
#         <th class="text-align:left">Title</th>
#         <td class="text-align:left">Saving a data file</td>
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

# # Ideas
#
# - Save a dataframe to a csv file.
# - Save a dataframe to an Excel file with one worksheet.
# - Save several dataframe to an Excel file with multiple worksheets.

# In[ ]:


# Open a csv file and save it to a new file as csv.
import pandas as pd


# In[ ]:


df = pd.read_csv('cloquet_two_weeks_60_min.csv',
                 parse_dates=True,
                 index_col='Time')
df.head()


# In[ ]:


df.to_csv('data_files/another_file.csv')


# In[ ]:


df2 = pd.read_csv('data_files/another_file.csv')
df.head()


# In[ ]:


# Save a dataframe to an Excel file with one worksheet.
# Set index=False in order to prevent python from adding a new index column.
df2.to_excel('data_files/another_file.xlsx',
             sheet_name='two_weeks_60_min',
             index=False)


# In[ ]:


df3 = pd.read_excel('data_files/another_file.xlsx',
                    parse_dates=True,
                    index_col='Time')


# In[ ]:


df.head()


# In[ ]:


# Combine three data frames into three worksheets in an Excel workbook.
writer = pd.ExcelWriter('data_files/even_another_file.xlsx')
df.to_excel(writer, 'sheet_one')
df2.to_excel(writer, 'sheet_two')
df3.to_excel(writer, 'sheet_three')
writer.save()


# In[ ]:


df4 = pd.read_excel('data_files/even_another_file.xlsx',
                    sheet_name=None)
df4.keys()

