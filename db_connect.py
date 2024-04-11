import mysql.connector


class DBConnect:
    def __init__(self):
        pass


    def get_connection(self):
        try:
            cnx = mysql.connector.connect(user="root",
                                          password="password",
                                          host="127.0.0.1",
                                          database="libretto")
            return cnx
        except mysql.connector.Error as err:
            print(err)
            return None

