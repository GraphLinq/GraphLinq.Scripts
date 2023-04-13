import json
import pymysql
import sys
#from decouple import config
from prettytable import PrettyTable

# PrettyTable
x = PrettyTable()
x.field_names = ["Total", "Already Exists", "Record Created"]

# Counters
COUNT = 0
UPDATED = 0
SAME = 0

# DB Config
#HOST = config('HELPER_HOST')
#USER = config('HELPER_USER')
#PASS = config('HELPER_PASS')
#DB = config('HELPER_DB')

# DB Manual Config
HOST = ""
USER = ""
PASS = ""
DB = ""

# DB Connect
conn = pymysql.connect(host=HOST,
    database=DB,
    user=USER,
    password=PASS)
cur  = conn.cursor()

# Generic No Additional Help Available Message
h = "<hr><p><b>No additional help available for this block.</b></p>"

# Direct Link to Help Document
l = "https://https://docs.graphlinq.io"

# Begin loop
with open('node_schema.json',) as data_file:
    data = json.load(data_file)
    for v in data:
        t = v['NodeType'].strip()
        n = v['FriendlyName'].strip()
        g = v['NodeGroupName'].strip()
        n = v['NodeBlockType'].strip()
        d = v['NodeDescription'].strip()
        print(t)

        query = f"INSERT IGNORE INTO helper (nodetype, nodehelp, nodelink) VALUES ('{t}', '{h}', '{l}')"
        cur.execute(query)
        print(f"{cur.rowcount} details inserted")

        if (cur.rowcount == 0):
            SAME += 1
        else:
            UPDATED =+ cur.rowcount

        COUNT += 1
        print()

conn.commit()
conn.close()
print("COMPLETE")
print()
x.add_row([COUNT, SAME, UPDATED])
print(x)
print()
