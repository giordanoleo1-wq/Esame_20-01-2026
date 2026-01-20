from database.DB_connect import DBConnect
from model.album import Album
from model.artist import Artist
from model.genre import Genre
from model.track import Track


class DAO:

    @staticmethod
    def get_all_artists():

        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """
                SELECT *
                FROM artist a
                """
        cursor.execute(query)
        for row in cursor:
            artist = Artist(id=row['id'], name=row['name'])
            result.append(artist)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def get_all_genres():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = "select * from genre"
        cursor.execute(query)
        for row in cursor:
            result.append(Genre(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_all_albums():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * \
                    FROM album """

        cursor.execute(query)

        for row in cursor:
            result.append(Album(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def read_all_tracks():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        query = """ SELECT * \
                    FROM track """

        cursor.execute(query)

        for row in cursor:
            result.append(Track(**row))

        cursor.close()
        conn.close()
        return result
