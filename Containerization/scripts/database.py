import psycopg2 as sql
from pprint import pprint

conn = sql.connect(host="postgres", user="postgres", password="mypassword")

with conn.cursor() as cur:
    cur.execute("SELECT * FROM mytable;")
    results = cur.fetchall()

pprint(results)