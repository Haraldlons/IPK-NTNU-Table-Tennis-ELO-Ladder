from elo import *

exp  = expected(1613, 1609)
exp += expected(1613, 1477)
exp += expected(1613, 1388)
exp += expected(1613, 1586)
exp += expected(1613, 1720)
print(exp)
elo(1613, 2.867, 2.5, k=32) 
print("=================")
print(elo)

