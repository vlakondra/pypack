import os, sys

sr= os.path.join(os.getcwd() ,'src')
sys.path.insert(0, sr)

print (sys.path)

from src.newlib import lib #OK
from newlib import lib as lb #OK

lb.print_table()

lib.print_table()

print(lib.scircle(2))

