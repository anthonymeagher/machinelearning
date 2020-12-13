import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
#
# opel_corsa_01 data
#       
nRowsRead = 1000 # specify 'None' if want to read whole file
# opel_corsa_01.csv has 7392 rows in reality, but we are only loading/previewing the first 1000 rows
df1 = pd.read_csv('../input/mldrivingstyles/opel_corsa_01.csv', delimiter=';', nrows = nRowsRead)
df1.dataframeName = 'opel_corsa_01.csv'
nRow, nCol = df1.shape
print(f'There are {nRow} rows and {nCol} columns')

#
# opel_corsa_02 data
#
nRowsRead = 1000
df2 = pd.read_csv('../input/mldrivingstyles/opel_corsa_02.csv', delimiter=';', nrows = nRowsRead)
df2.dataFrame = 'opel_corsa_02.csv'
nrow, nCol = df2.shape
print(f'There are {nRow} rows and {nCol} columns')

#
# peugeot_207_01 data
#
nRowsRead = 1000
df3 = pd.read_csv('../input/mldrivingstyles/peugeot_207_01.csv', delimiter=';', nrows = nRowsRead)
df3.dataFrame = 'peugeot_207_01'
nRow, nCol = df3.shape
print(f'There are {nRow} rowsand {nCol} columns')

#
# peugeot_207_02.csv data
#
nRowsRead = 1000
df4 = pd.read_csv('../input/mldrivingstyles/peugeot_207_02.csv', delimiter=';', nrows = nRowsRead)
df4.dataFrame = 'peugeot_207_02.csv'
nRow, nCol = df4.shape
print(f'There are {nRow} rows and {nCol} columns')
