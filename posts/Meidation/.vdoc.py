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
import time;import pandas as pd;import numpy as np ;import datetime
from datetime import datetime;from datetime import timedelta;import stata_setup
stata_setup.config('/Applications/Stata', 'mp')
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

clear all
set maxvar 120000, permanently
set more off

import delimited "/Users/shaokangyang/Library/CloudStorage/GoogleDrive-shaokang@vt.edu/My Drive/Nethealth/Data/CNSA/combine/7/df7_22-5.csv"
gen date2 = date(date, "YMD")
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
#
#
#
#
