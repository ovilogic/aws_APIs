'''
ex4.5 Query the RDS table just created.
'''

import boto3
import json
import datetime
import pymysql as mariadb

from private_variables import rds_identifier, db_name, user_name, user_password, rds_endpoint

db_connection = mariadb.connect(
    host=rds_endpoint,
    user=user_name,
    password=user_password,
    database=db_name
)

cursor = db_connection.cursor()

try:
    sql = "SELECT * FROM Users"
    cursor.execute(sql)
    query_resutl = cursor.fetchall()
    print('Querying the Users Table... wait, Ovi')
    print(query_resutl)
except mariadb.Error as e:
    print('Error: {}'.format(e))
    print('Sorry, it did not go according to plan.')
finally:
    db_connection.close()