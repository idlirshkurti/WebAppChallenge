import sqlite3
import csv

conn = sqlite3.connect('TestDB.db')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS TestDB')
cur.execute('''
CREATE TABLE "task_data"(
    "id"   INTEGER,
    "timestamp"   TEXT,
    "temperature"   REAL,
    "duration"  TEXT
)
''')

fname = input('Enter the csv file name to be loaded to the database:')

with open(fname) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
    for row in csv_reader:
        print(row)
        id = row[0]
        timestamp = row[1]
        temperature = row[2]
        duration = row[3]
        cur.execute('''INSERT INTO task_data(id ,timestamp ,temperature , duration)
        VALUES (?, ?, ?, ?)''', (id ,timestamp ,temperature , duration))
        conn.commit()
