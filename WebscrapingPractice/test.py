import pandas as pd
import numpy as np
#index Levels

outside=['G1','G1','G1','G2','G2','G2']
inside=[1,2,3,1,2,3]

hier_index=list(zip(outside,inside))

heir_index=pd.MultiIndex.from_tuples(heir_index)

print(heir_index)

