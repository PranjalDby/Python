from genericpath import exists
from operator import truediv
import re
from select import select
import sqlite3
from unittest import result;
sqliteConnect = sqlite3.connect('Password.db')
cursor = sqliteConnect.cursor()
def create_db(pin):
    try:
            # queryTable = '''CREATE TABLE `Userpin` (Pin INT(4) NOT NULL);'''
            # if(cursor.execute(queryTable)):
            #     print('table Created')
            # alter = 'ALTER TABLE `Userpin` ADD ID INT(1)'
            # cursor.execute(alter)
            insert = f'INSERT INTO `Userpin` VALUES({pin},{1})'
            cursor.execute(insert)
            dat = 'select * from `Userpin`;'
            d = cursor.execute(dat)
            sqliteConnect.commit()
    except sqlite3.Error as error:
        print(error)

def DeletePin(pin):
    dele = f'DELETE FROM `Userpin` WHERE pin == {pin}'
    cursor.execute(dele)
    sqliteConnect.commit()
def checkpin(pin):
    quet = f'SELECT `Pin` FROM `Userpin`;'
    d = cursor.execute(quet)
    sqliteConnect.commit()
    for i in d.fetchone():
       if(pin==i):
        return True;
    return False
    # for i in range(len(d)):
    #     print(list(i))
    #     if(pin == d[i]):
    #         return True;
    #     else:
    #         return False;


