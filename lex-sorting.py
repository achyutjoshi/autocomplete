__author__ = 'achyutjoshi'

'''This file is to sort the data in lexographical order'''


import mysql.connector
from collections import OrderedDict

'''***********************************************************'''

def database_connect(db):
    cursor = db.cursor()
    query = ("SELECT * FROM search_tree_data")

    cursor.execute(query)

    dic = {}


    for (id ,text, weight) in cursor :
        #arr.append(data)
        dic[text] = weight

    cursor.close()

    db.close()
    return dic

'''*********************************************************'''

def sorting(dic):
    od = OrderedDict(sorted(dic.items(), key=lambda t: t[0]))
    return od

'''*********************************************************'''

def update_dic(dic,update_array):
    for items in update_array :
        flag = 0
        for key in dic.keys():
            if(key == items):
                flag = 1
                buff = dic.get(key)
                buff = buff + 1
                dic[key] = buff
        if(flag == 0) :
            dic[items] = 1
'''************************************************************'''


db = mysql.connector.connect(user = 'root',
      password = '',
      host = '127.0.0.1',
      database = 'autocomplete_db')

diction = database_connect(db)
sorted_diction =sorting(diction)
print sorted_diction




