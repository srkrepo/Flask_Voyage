# -*- coding: utf-8 -*-

"""
This file is part of voyage.
 __file__ : create_model.py
"""

__author__ = 'Sri Pandi, Satheesh Rathinakumar'

# Python Default Modules
import os

import pandas as pd
import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base

DB_NAME = os.environ['DB_NAME']
DB_USER = os.environ['DB_USER']
DB_PASS = os.environ['DB_PASS']
DB_SERVICE = os.environ['DB_SERVICE']
DB_PORT = os.environ['DB_PORT']

URI = 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(DB_USER, DB_PASS, DB_SERVICE, DB_PORT, DB_NAME)
engine = sa.create_engine(URI)

# Ship data
df = pd.read_csv(r'ship_data.csv', chunksize=100000)
Base = declarative_base()
Base.metadata.create_all(engine)

for row in df:
    row.to_sql(con=engine, index_label='id', name='ship', if_exists='replace')

# Sailing data
df = pd.read_csv(r'sailing_data.csv', chunksize=100000)
Base = declarative_base()
Base.metadata.create_all(engine)

for row in df:
    row.to_sql(con=engine, index_label='id', name='sailing', if_exists='replace')
