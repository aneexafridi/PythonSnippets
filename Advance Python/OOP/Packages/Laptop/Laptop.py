# method one = 1 to use packages
# Laptop main package
# import Dell.Dell_530
# import Dell.Dell_650
# import Hp.Hp_650
# import Hp.Hp_800
# import Hp.HpEliteBook.EliteBook_840
#--------------------------------------

# uncomment the code see the result

# Dell.Dell_530.Dell_Five()
# Dell.Dell_650.Dell_Six()
# Hp.Hp_650.HP_Six()
# Hp.Hp_800.Hp_Eight()
# Hp.HpEliteBook.EliteBook_840.HpEliteBook() 
#+++++++++++++++++++++++++++++++++++++++++++++
# Method two = 2  to use packages
# Laptop main package
# from Dell import Dell_530,Dell_650
# from Hp import Hp_650,Hp_800
# from Hp.HpEliteBook import EliteBook_840

# Dell_530.Dell_Five()
# Dell_650.Dell_Six()
# Hp_650.HP_Six()
# Hp_800.Hp_Eight()
# EliteBook_840.HpEliteBook() 
# +++++++++++++++++++++++++++++++++++++++++++++++
# Method Three = 3 to use packages
# Laptop main Package
# ________________________Note import *
# we use __all__ to assigned the modules name in a list
# in __init__ File

from Dell import *
from Hp import*
from Hp.HpEliteBook import* 

Dell_530.Dell_Five()
Dell_650.Dell_Six()
Hp_650.HP_Six()
Hp_800.Hp_Eight()
EliteBook_840.HpEliteBook()