import mysql.connector

config = {
    "user":"root",
    "password":"",
    "host":"127.0.0.1",
    "port":3306,
    "database":"journal_backend",
    'raise_on_warnings': True
}

connection = None
cursor = None

try:
    connection = mysql.connector.connect(**config)

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("MySQL Server version : ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select * from user")
        rows = cursor.fetchall()
        for row in rows:
            print(row)

except mysql.connector.Error as e:
    print(f"Error while connecting to db: {e}")

finally:
    if cursor is not None:
        cursor.close()

    if connection is not None and connection.is_connected():
        connection.close()
        print("MySQL connection is closed")