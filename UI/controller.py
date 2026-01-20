import flet as ft
from UI.view import View
from model.model import Model

class Controller:
    def __init__(self, view: View, model: Model):
        self._view = view
        self._model = model

    def handle_create_graph(self, e):
        self._view.txt_result.clean()
        try:
            soglia= int(self._view.txtNumAlbumMin.value)
        except Exception as exc:
            self._view.show_alert("Inserire una soglia valida")
            print(exc)
            return

        self._model.build_graph(soglia)
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato: {self._model.G.number_of_nodes()} nodi, {self._model.G.number_of_edges()} archi"))



        for a in self._model.G.nodes():
            self._view.ddArtist.options.append(ft.dropdown.Option(key= a.id, text=a.name))

        self._view.ddArtist.disabled = False
        self._view.btnArtistsConnected.disabled = False
        self._view.update_page()


    def handle_connected_artists(self, e):
        self._view.txt_result.clean()



        try:
            artist_id = int(self._view.ddArtist.value)
        except Exception as exc:
            self._view.show_alert("Inserire un artista valido")
            print(exc)
            return

        artist= self._model.dic_artist_id[artist_id]
        lista= self._model.trova_connessi(artist)

        self._view.txt_result.controls.append(ft.Text(f"Artisti direttamente collegati all'artista {artist.name}:"))
        for a, p in lista:
            self._view.txt_result.controls.append(ft.Text(f"{a.id}, {a.name}, Numero di generi in comune: {p}"))




        self._view.update_page()







