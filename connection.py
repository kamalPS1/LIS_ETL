#!/usr/bin/env python
import snowflake.connector
from validation import auth


# Establishing the connection and setting up cursor
ctx = snowflake.connector.connect(
    user=auth['user'],
    password=auth['password'],
    account=auth['account'],
    database= 'BHATBHATENI',
    warehouse= 'COMPUTE_WH'
)
cs = ctx.cursor()


