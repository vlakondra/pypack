import os, sys
from cliapp.datacomm import grp

grp(filename='./data/data.csv')

grp.commands['show']()

# sr= os.path.join(os.getcwd() ,'src')
# sys.path.insert(0, sr)

# print (sys.path)

