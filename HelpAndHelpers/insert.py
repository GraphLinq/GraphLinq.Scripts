import json
#import pymysql
import sys
from decouple import config

HOST = config('HELPER_HOST')
USER = config('HELPER_USER')
PASS = config('HELPER_PASS')
DB = config('HELPER_DB')

conn = pymysql.connect(host=HOST,
                        database=DB,
                        user=USER,
                        password=PASS)
cur  = conn.cursor()

h = "<hr><p><b>No additional help available for this block.</b></p>"

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
conn.commit()
conn.close()

