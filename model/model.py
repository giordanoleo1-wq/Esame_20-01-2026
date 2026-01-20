import networkx as nx
from database.dao import DAO

class Model:
    def __init__(self):
        self.G = nx.Graph()
        self._artists_list = []
        self.load_all_artists()
        self.lista_albums= DAO.read_all_albums()
        self.lista_genres= DAO.get_all_genres()
        self.lista_tracks= DAO.read_all_tracks()


        self.dic_artist_id= {}
        self.dic_album_id= {}
        self.dic_album_artist = {}
        self.dic_album_genre = {}
        self.dic_album_to_track = {}
        self.dic_artist_genre = {}

        self.lista_artisti_validi = []

    def load_all_artists(self):
        self._artists_list = DAO.get_all_artists()
        print(f"Artisti: {self._artists_list}")

    def build_graph(self, soglia):
        self.load_all_artists()
        self.G= nx.Graph()
        self.dic_artist_id= {}
        self.dic_album_id = {}
        self.dic_album_artist= {}
        self.dic_album_genre= {}
        self.dic_album_to_track = {}
        self.dic_artist_genre= {}

        self.lista_artisti_validi= []







        for a in self._artists_list:
            if a.id not in self.dic_artist_id:
                self.dic_artist_id[a.id] = a




        for a in self.lista_albums:
            if a.id not in self.dic_album_id:
                self.dic_album_id[a.id] = a

            if a.artist_id not in self.dic_album_artist:
                self.dic_album_artist[a.artist_id]= set()
            self.dic_album_artist[a.artist_id].add(a.id)





        for a in self._artists_list:
            if a.id in self.dic_album_artist:
                if len(self.dic_album_artist[a.id]) >= soglia:
                    self.lista_artisti_validi.append(a)



        for t in self.lista_tracks:
            if t.album_id not in self.dic_album_to_track:
                self.dic_album_to_track[t.album_id] = set()
            self.dic_album_to_track[t.album_id].add(t)

        for a_id, tracks in self.dic_album_to_track.items():
            if a_id not in self.dic_album_genre:
                self.dic_album_genre[a_id] = set()
            for t in tracks:
                self.dic_album_genre[a_id].add(t.genre_id)



        for art, albs in self.dic_album_artist.items():
            if len(albs) >= soglia:
                generi_artista= []
                for a in albs:
                    genre_id= self.dic_album_genre[a]
                    if genre_id not in generi_artista:
                        generi_artista.append(genre_id)

                    self.dic_artist_genre[art] = generi_artista
















        for a in self.lista_artisti_validi:
            self.G.add_node(a)

        for i in range(len(self.lista_artisti_validi)):
            for j in range(i + 1, len(self.lista_artisti_validi)):

                artist1 = self.lista_artisti_validi[i]
                artist2 = self.lista_artisti_validi[j]

                g1= self.dic_artist_genre[artist1.id]
                g2= self.dic_artist_genre[artist2.id]

                count= 0
                for a in g1:
                    for b in g2:
                        if a==b:
                            count += 1
                if count>0:
                    self.G.add_edge(artist1, artist2, weight= count)



    def trova_connessi(self, artist):

        lista= []
        connessa= nx.connected_components(self.G)
        for n in connessa:
            peso= self.G[artist][n]['weight']
            lista.append((n, peso))
        lista.sort(key=lambda x: x[1])
        return lista



















































