import sqlite3
import csv
import pandas as pd
import os

fname = 'input/task_data.csv'

#if os.path.exists('example.db'):
#    os.remove('example.db')

conn = sqlite3.connect('example.db', check_same_thread=False)
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS example')
cur.execute('''
CREATE TABLE IF NOT EXISTS "task_data"(
    "id"   INTEGER,
    "timestamp"   TEXT,
    "temperature"   REAL,
    "duration"  TEXT
)
''')

cur.execute('''
CREATE TABLE IF NOT EXISTS "logs"(
    "query"   TEXT,
    "timestamp"   TEXT
)
''')

with open(fname) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    next(csv_reader)
    for row in csv_reader:
        print(row)
        id = row[0]
        timestamp = row[1]
        temperature = row[2]
        duration = row[3]
        cur.execute('''INSERT INTO task_data(id ,timestamp ,temperature , duration)
        VALUES (?, ?, ?, ?)''', (id ,timestamp ,temperature , duration))
        conn.commit()


conn.row_factory = sqlite3.Row

# Make a convenience function for running SQL queries
def sql_query(query):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def sql_edit_insert(query,var):
    cur = conn.cursor()
    cur.execute(query,var)
    conn.commit()

def sql_input_query(query,var):
    cur = conn.cursor()
    cur.execute(query,var)
    conn.commit()
    rows = cur.fetchall()
    return rows

def sql_delete(query,var):
    cur = conn.cursor()
    cur.execute(query,var)

def sql_query2(query,var):
    cur = conn.cursor()
    cur.execute(query,var)
    rows = cur.fetchall()
    return rows
