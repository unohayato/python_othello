from dataclasses import field
import imp
from pprint import pprint
import numpy as np

def mk_field(f_size):
  f = [[0]*f_size for _ in range(f_size)]
  field = np.pad(
    f, [1,1], "constant", constant_values=(9)
  )
  print(field)

mk_field(8)