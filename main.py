# import needed libraries
from sqlalchemy import create_engine

import pandas as pd
# this is imported from config folder

import os


pwd = 'your password'
uid = 'your name in postgres'
server = "localhost"
db = "db name"
port = "5432"
dir = r'/Users/grinderix/Desktop/Work/projects/tb-full-stack-prjct/backend'


# extract data from sql server
def extract():
    # starting directory
    directory = dir
    # iterate over files in the directory
    for filename in os.listdir(directory):
        # get filename without ext
        file_wo_ext = os.path.splitext(filename)[0]
        # only process excel files
        if filename.endswith(".xlsx"):
            f = os.path.join(directory, filename)
            # checking if it is a file
            if os.path.isfile(f):
                df = pd.read_excel(f)
                # call to load
                load(df, file_wo_ext)


# load data to postgres
def load(df, tbl):
    rows_imported = 0
    engine = create_engine(f'postgresql://{uid}:{pwd}@{server}:{port}/{db}')
    print(f'importing rows {rows_imported} to {rows_imported + len(df)}... ')
    # save df to postgres
    df.to_sql(f"stg_{tbl}", engine, if_exists='replace', index=False)
    rows_imported += len(df)
    # add elapsed time to final print out
    print("Data imported successful")


df = extract()
