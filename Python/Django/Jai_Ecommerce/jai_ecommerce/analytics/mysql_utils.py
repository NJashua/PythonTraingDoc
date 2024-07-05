# import snowflake.connector

# def get_snowflake_connection():
#     return snowflake.connector.connect(
#         user='NITHIN',
#         password='Nithin@2024',
#         account='ctkbbdn-xc60080'
#     )

# analytics/mysql_utils.py

import MySQLdb
from django.conf import settings

def get_mysql_connection():
    return MySQLdb.connect(
        host=settings.DATABASES['default']['HOST'],
        user=settings.DATABASES['default']['USER'],
        passwd=settings.DATABASES['default']['PASSWORD'],
        db=settings.DATABASES['default']['NAME']
    )
