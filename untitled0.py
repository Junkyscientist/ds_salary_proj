# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 10:29:19 2020

@author: MGilSoriano
"""

import glassdoor_scraper as gs
import pandas as pd 

path = "C:/Users/MGilSoriano/Documents/ds_salary_proj/chromedriver"


df = gs.get_jobs('data scientist', 15, False, path, 15)


