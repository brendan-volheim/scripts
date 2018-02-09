import json
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from datetime import datetime


params = {
  'database': 'DB_NAME',
  'user': 'DB_USER',
  'password': 'DB_PASS',
  'host': 'DB_HOST',
  'port': 5432
}
start_total_time = time.time()
conn = psycopg2.connect(**params)
cur = conn.cursor(cursor_factory=RealDictCursor)
file_name = 0
for i in range(0, 221):  # from 0 to count(*) of your table / 100000
    start_time = time.time()
    start = i*100000
    end = (i*100000) + 100000
    curTime = datetime.now().strftime('%H:%M:%S')
    print(curTime + ": Running " + str(start) + " to " + str(end))
    query = 'SELECT * FROM <TABLE_NAME> ORDER BY <table_id> LIMIT 100000 OFFSET ' + str(start) + ';'
    print(query)

    cur.execute(query)

    file = open("/home/ubuntu/dumps/dumps_" + str(file_name) + ".json", "w")
    file.write(json.dumps(cur.fetchall()))
    file.close()

    end_time = time.time()
    curTime = datetime.now().strftime('%H:%M:%S')
    print(curTime + ": Finished dumps_" + str(file_name) + ".json")
    print(time.strftime('%H:%M:%S', time.gmtime(end_time - start_time))+" \n")
    file_name += 1
print(time.strftime('%H:%M:%S', time.gmtime(end - start_total_time)))

