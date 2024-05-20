'''
ex4.4 RDS is up and running and we also have the endpoint for it. We can 
now create the first table and add records.
'''
import boto3
import json
import datetime
import pymysql as mariadb

from private_variables import rds_identifier, db_name, user_name, user_password
from private_variables import rds_endpoint


# Step 1 - Connect to the database to create the table.
db_connection = mariadb.connect(
    host=rds_endpoint,
    user=user_name,
    password=user_password,
    database=db_name
)

cursor = db_connection.cursor()
try:
    cursor.execute("CREATE TABLE Users (\
        user_id INT NOT NULL AUTO_INCREMENT, user_fname VARCHAR(100) NOT NULL, user_Lname VARCHAR(100) NOT NULL, \
        user_email VARCHAR(175) NOT NULL, PRIMARY KEY (user_id))")
    print('Table created')
except mariadb.Error as e:
    print('Error: {}'.format(e))
finally:
    db_connection.close()


# Step 2 Connect to the database to add users to the table.
db_connection = mariadb.connect(host=rds_endpoint, user=user_name,
    password=user_password, database=db_name)

cursor = db_connection.cursor()
try:
    sql = "INSERT INTO Users (user_fname, user_Lname, user_email) VALUES (%s, %s, %s)"
    cursor.execute(sql, ('CJ', 'Smith', 'blabl@agag.com'))
    cursor.execute(sql, ('fString', 'Coreioanon', 'emailonbga@aga.com'))
    cursor.execute(sql, ('nor', 'ifano', 'qrop@gag.com'))

    db_connection.commit()
    print('Inserted, ovi')
except mariadb.Error as e:
    print('Error: {}'.format(e))
    print('Sorry, something is bad')
finally:
    db_connection.close()

