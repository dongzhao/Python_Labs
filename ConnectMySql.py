import mysql.connector

ctx = mysql.connector.connect(
    user = "root",
    password = "root123",
    host = "127.0.0.1",
    database = "myTestDB"
)
print(ctx)



ctx.close()