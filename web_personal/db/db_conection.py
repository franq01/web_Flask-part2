import pymysql

def get_conection():
    connection = pymysql.Connect(host='localhost',
                                       user='root',
                                       password='example',
                                       db='platzi_blog',
                                       
                                       cursorclass=pymysql.cursors.DictCursor)
    return connection