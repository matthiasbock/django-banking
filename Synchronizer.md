# _synchronize.py_ #

## Codeflow ##

  * read settings from _[synchronize.conf](synchronize_conf.md)_
  * import database setting from _settings.py_
  * make MySQL connection
    * how to make a MySQL connection in Python: http://mysql-python.sourceforge.net/MySQLdb.html
  * import _aqbanking.py_, the AqBanking Python binding
  * establish HBCI connection
  * get account list
    * create new accounts in DB as neccessary
    * trigger event, if applicable
  * for every account:
    * get transaction list
    * for every transaction:
      * is it present in the DB ?
        * no: upload it
        * trigger event, if applicable
  * close DB connection

## Event notification ##

  * setup notification events in _synchronize.py_ (not ready, planned)

## Automatic daily sync ##

  * install _synchronize.py_ as a cronjob