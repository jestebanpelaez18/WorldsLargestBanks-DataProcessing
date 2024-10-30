# libraries needed for this project.
import pandas as pd 
import numpy as np 
from datetime import datetime
import requests
import sqlite3
from bs4 import BeautifulSoup

# Code for ETL operations on Country-GDP data

def log_progress(message):
    ''' This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing'''
    timestamp_format = '%Y-%h-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp_format)
    with open("./code_log.txt","a") as f:
        f.write(timestamp + ":" + message + '\n')

def extract(url, table_attribs):
    ''' This function aims to extract the required
    information from the website and save it to a data frame. The
    function returns the data frame for further processing. '''
    # First load the entire web page as HTML and parse the data 
    # in HTML format
    html_page = requests.get(url).text
    data = BeautifulSoup(html_page, 'html.parser')
    tables = data.find_all('tbody')
    rows = tables[0].find_all('tr')
    df = pd.DataFrame(columns=table_attribs)
    for row in rows:
        col = row.find_all('td')
        if len(col) != 0:
            data_dict = {"Name" : col[1].find_all("a")[1]["title"],
            'MC_USD_Billion' : float(col[2].contents[0][:-1])}
            df1 = pd.DataFrame(data_dict, index=[0])
            df1 = df1.dropna(axis=1, how='all') 
            df = pd.concat([df,df1],ignore_index=True)
    return df

def transform(df, csv_path):
    ''' This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies'''

    # Get the exchange rate from the csv file
    exchangerate_df = pd.read_csv(csv_path)
    exchange_rate = exchangerate_df.set_index('Currency').to_dict()['Rate']
    df['MC_GBP_Billion'] = [np.round(x*exchange_rate['GBP'],2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion'] = [np.round(x*exchange_rate['EUR'],2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [np.round(x*exchange_rate['INR'],2) for x in df['MC_USD_Billion']]
    return df

def load_to_csv(df, output_path):
    ''' This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing.'''
    df.to_csv(output_path)

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final data frame to a database
    table with the provided name. Function returns nothing.'''
    df.to_sql(table_name,sql_connection, if_exists='replace', index=False)

def run_query(query_statement, sql_connection):
    ''' This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. '''
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)

''' Here, you define the required entities and call the relevant
functions in the correct order to complete the project. Note that this
portion is not inside any function.'''

# Variables required in each fuction:
# url: This is the url where the table is content
# table_attribs: The firts headers of the final DataFrame
# exchange_rate_csv: This is where our exchange rate csv is allocated"
url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs = ['Name', 'MC_USD_Billion']
exchange_rate_csv = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv'
csv_path = './Largest_banks_data.csv'
db_name = 'Banks.db'
table_name = 'Largest_banks'
log_progress("Preliminaries complete. Initiating ETL process")

#ETL process

# Step 1: Extraction
df = extract(url,table_attribs)
log_progress("Data extraction complete. Initiating Transformation process")

# Step 2: Transformation
df = transform(df, exchange_rate_csv)
# 146.86
log_progress("Data transformation complete. Initiating Loading process")

# Step 3: Loading to csv

load_to_csv(df,csv_path)
log_progress("Data saved to CSV file")

#Step 4: Loading to Database
sql_connection = sqlite3.connect(db_name)
log_progress("SQL Connection initiated")
load_to_db(df,sql_connection,table_name)
log_progress("Data loaded to Database as a table, Executing queries")

# Step 5: Run Query
# Print the contents of the entire table
query_statement = f"SELECT * from {table_name}"
run_query(query_statement, sql_connection)

# Print the average market capitalization of all the banks in Billion GBP
query_statement = f"SELECT AVG(MC_GBP_Billion) FROM {table_name}"
run_query(query_statement, sql_connection)

# Print only the names of the top 5 banks
query_statement = f"SELECT Name from {table_name} LIMIT 5"
run_query(query_statement, sql_connection)

log_progress("Process Complete")

sql_connection.close()
log_progress("Server Connection closed")
