import time
import MySQLdb
from MySQLdb import OperationalError

while True:
    try:
        conn = MySQLdb.connect(
            host="db",
            user="django_user",
            passwd="password",
            db="django_db",
            port=3306
        )
        conn.close()
        break
    except OperationalError:
        print("Database unavailable, waiting 1 second...")
        time.sleep(1)
