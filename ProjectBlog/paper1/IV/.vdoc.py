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
#| echo: false
#| warning: false
#| output: true
import time;import pandas as pd;import numpy as np;import datetime
from datetime import datetime;from datetime import timedelta;import sqlite3;import warnings
import matplotlib.pyplot as plt;import seaborn as sns;warnings.filterwarnings('ignore')

df=pd.read_csv("/Users/shaokangyang/Library/CloudStorage/OneDrive-Personal/Nethealth/Data/CNSA/combine/7/bt7_1.5r.csv")

df[['egoid','count_begin90', 'time_fallsleep','battery','battery_time','charging','binterval']]
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
#| output: true

df[['egoid','count_begin90', 'time_fallsleep','battery','charging','battery_time','binterval']].describe()
#
#
#
#
#
#
#
#| echo: false
#| warning: false
#| output: true
df=pd.read_csv("/Users/shaokangyang/Library/CloudStorage/OneDrive-Personal/Nethealth/Data/CNSA/combine/7/df7_22-5s.csv")
df[['egoid','screen_time', 'unlock','message','count_begin90', 'time_fallsleep','battery','charging','battery_time','binterval']].describe()
#
#
#
#
#
#| echo: false
#| warning: false
#| output: true
df=pd.read_csv("/Users/shaokangyang/Library/CloudStorage/OneDrive-Personal/Nethealth/Data/CNSA/combine/7/df7_22-5b.csv")
df[['egoid','screen_time', 'unlock','message','count_begin90', 'time_fallsleep','battery','charging','battery_time','binterval']].describe()
#
#
#
#| echo: false
#| warning: false
#| output: false
import time;import pandas as pd;import numpy as np ;import datetime
from datetime import datetime;from datetime import timedelta;import stata_setup
stata_setup.config('/Applications/Stata', 'mp')
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
#| code-fold: false
#| code-overflow: wrap
%%stata
#| echo: true
clear all
set maxvar 120000, permanently
set more off

import delimited "/Users/shaokangyang/Library/CloudStorage/OneDrive-Personal/Nethealth/Data/CNSA/combine/7/df7_22-5s.csv"
gen date2 = date(date, "YMD")
#
#
#
#
#
#| echo: true
#| warning: false
#| output: false
#| code-fold: false
#| code-overflow: wrap
%%stata

global id egoid
global t date2
global ylist sleep_debt
global mainIV  c.screen_time##c.screen_time iimessage unlock
global Call_Control call duration length bytes
global Fitness_Control steps100 floors sedentaryminutes lightlyactiveminutes fairlyactiveminutes veryactiveminutes lowrangecal100 fatburncal100 cardiocal100 peakcal100
global Other_Control naps naps_dur light_exposure insession##weekday##time_wakeuphour c.studyweeks#id
global fe i.studyweeks

*Set data as panel data
sort $id $t
xtset $id $t

regress screen_time charging battery $fe $Fitness_Control $Other_Control $Call_Control message unlock i.egoid

#
#
#
#| echo: true
#| warning: false
#| output: true
#| code-fold: false
#| code-overflow: wrap
%%stata

esttab, keep(charging battery message unlock) stats(N r2 F p, labels("Observations" "R-squared" "F statistic" "Prob > F")) replace
#
#
#
#
#
#
#
#| echo: true
#| warning: false
#| output: false
#| code-fold: false
#| code-overflow: wrap
%%stata

ivregress 2sls sleep_debt (screen_time = charging) $fe $Fitness_Control $Other_Control $Call_Control i.egoid message unlock

#
#
#
#| echo: true
#| warning: false
#| output: true
#| code-fold: false
#| code-overflow: wrap
%%stata

esttab, keep(screen_time battery message unlock) stats(N r2 F p, labels("Observations" "R-squared" )) replace
#
#
#
#
