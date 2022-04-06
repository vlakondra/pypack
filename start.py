import os, sys
sr= os.path.join(os.getcwd() ,'src')
print('sr',sr)
sys.path.insert(0, sr)

from src.newlib import lib
from newlib import lib as lb

# import src.newlib.lib

lib.print_table()
print(sys.path)

lb.print_table()