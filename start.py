import os, sys

sr= os.path.join(os.getcwd() ,'src')
sys.path.insert(0, sr)

print (sys.path)

from src.cliapp import lib #OK
from cliapp import lib as lb #OK
from cliapp import CONST_PI



print(lib.scircle(2))

std =sys.stdout
with open ('file.txt', 'w') as f:
    sys.stdout = f
    lb.print_table()
    sys.stdout =std
