import mariadb
from types import SimpleNamespace

# connection parameters
config = SimpleNamespace(
    DB_NAME='bitnami_opencart',
    TABLE='oc_country',
    HOST='192.168.100.9',
    PORT=3306,
    USER='bn_opencart',
    PASSWORD='')

# Establish a connection
db_connection = mariadb.connect(
    host=config.HOST,
    port=config.PORT,
    user=config.USER,
    password=config.PASSWORD
)

# Getting cursor object from connection
cursor = db_connection.cursor()

cursor.execute(f"show databases")
# Fetch results as list
# print(cursor.fetchall())

# Won't work if data was fetched
for row in cursor.fetchall():
    print(row)

# Switch to created database
cursor.execute(f"USE {config.DB_NAME}")

if __name__ == '__main__':
    # execute the query
    cursor.execute(f"SELECT * FROM {config.TABLE}")

    # Getting first entry
    print("\n", cursor.fetchone(), sep='')

    # Getting all available rows
    for row in cursor.fetchall():
        print(row)
