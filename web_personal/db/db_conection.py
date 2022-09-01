import pymysql

def get_conection():
    connection = pymysql.Connect(host='localhost',
                                       user='root',
                                       
                                       db='web_personal',
                                       
                                       cursorclass=pymysql.cursors.DictCursor)
    return connection