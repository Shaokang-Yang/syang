# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#| echo: false
#| warning: false
#| output: false
import time;import pandas as pd;import numpy as np;import datetime
from datetime import datetime;from datetime import timedelta;import sqlite3
import warnings;warnings.filterwarnings('ignore')
vt=pd.read_csv("/Users/shaokangyang/Library/CloudStorage/OneDrive-Personal/Nethealth/Data/overlap_rate.csv")
#
#
#
#
#| echo: false
#| warning: false
#| output: true
vt10237=vt[vt['egoid']==10237]
cols = list(vt.columns)
# Move the 'egoid' column to the start of the list
cols.insert(0, cols.pop(cols.index('egoid')))
# Reindex the DataFrame with the new column order
vt10237 = vt10237.reindex(columns=cols)
# Display the DataFrame
vt10237
#
#
#
#| echo: false
#| warning: false
#| output: true
cols = list(vt.columns)
# Move the 'egoid' column to the start of the list
cols.insert(0, cols.pop(cols.index('egoid')))
# Reindex the DataFrame with the new column order
vt = vt.reindex(columns=cols)
# Display the DataFrame
#
#
#
