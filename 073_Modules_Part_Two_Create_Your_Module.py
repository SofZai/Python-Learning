# --------------------------------------
# -- Modules ==> Create your Module -- 
# --------------------------------------

# import sys
# sys.path.append (r"D:\Games")
# print (sys.path)

import KosMos
# print (dir(KosMos))

KosMos.sayHello ("Sofiane")
KosMos.sayHowAreYou ("Asma")

# Alias

import KosMos as aa

aa.sayHello ("Sofiane")
aa.sayHowAreYou ("Asma")

from KosMos import sayHello as bb

bb ("Sofiane")
bb ("Asma")