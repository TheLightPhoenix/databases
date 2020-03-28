# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 18:25:59 2020

@author: maciej
"""

from sqlalchemy import create_engine

db_string = "postgresql://wbauer_adb:adb2020@pgsql-196447.vipserv.org:5432/wbauer_adb"

db = create_engine(db_string)