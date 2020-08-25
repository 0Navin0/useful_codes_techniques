import numpy as np
import sys

for ii in range(1,10):
    for jj in range(1,10):
        print(ii,jj)
        try: 
            tt=5/(jj-5)
        except:
            print(f"expected exception at ii,jj={ii,jj}")
            sys.exit(1)

