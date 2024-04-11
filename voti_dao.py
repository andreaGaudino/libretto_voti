import mysql.connector
import db_connect
from voti_dto import VotoDto
from db_connect import DBConnect


class VotiDao:
    def get_voti(self):
        cnx = db_connect.DBConnect().get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT *
                FROM voti"""
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(VotoDto(row["nome"],
                                      row["CFU"],
                                      row["punteggio"],
                                      bool(row["lode"]),
                                      row["data"]))
        return result
        cursor.close()
        cnx.close()
    def add_voti(self, voto:VotoDto):
        cnx = db_connect.DBConnect().get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """INSERT INTO voti
                        (nome, CFU, punteggio, lode, data)
                        VALUES(%s, %s, %s, %s, %s)
                        """
        cursor.execute(query, (voto.nome, voto.CFU, voto.punteggio, voto.lode, voto.data))
        cnx.commit()
        cursor.close()
        cnx.close()



if __name__ == "__main__":
    voti_dao = VotiDao()
    voti_dao.get_voti()