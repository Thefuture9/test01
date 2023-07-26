import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math
from typing import Union
from scipy.integrate import solve_ivp
from collections import OrderedDict

self = {          # 组分i
                'SI'    : 0,      # 溶解性不可降解有机物
                'SS'    : 0,      # 快速可生物降解有机物
                'XI'    : 0,      # 颗粒性不可生物降解有机物
                'XS'    : 1e-6,      # 慢速可生物降解有机物
                'XBH'   : 1e-6,   # 异养菌生物量
                'XBA'   : 1e-6,   # 自养菌生物量
                'XP'    : 0,      # 生物固体衰减而产生的惰性物质
                'SO'    : 0,      # 溶解氧
                'SNO'   : 0,      # 硝酸盐和亚硝酸盐形式的氮
                'SNH'   : 0,      # 氨和铵根离子态的氮
                'SND'   : 0,      # 溶解性可生物降解有机氮
                'XND'   : 0,      # 颗粒性可生物降解有机氮
                'SALK'  : 0,      # 碱度
        }
comp = self.copy()
comp['SI']=1
print(comp)
print(self)