# -*- coding: iso-8859-15 -*-
#!/usr/bin/python

read settings from synchronize.conf
import database setting from settings.py
make MySQL connection
how to make a MySQL connection in Python: http://mysql-python.sourceforge.net/MySQLdb.html
import aqbanking.py, the AqBanking Python binding
establish HBCI connection
get account list
create new accounts in DB as neccessary
trigger event, if applicable
for every account:
get transaction list
for every transaction:
is it present in the DB ?
no: upload it
trigger event, if applicable
close DB connection

