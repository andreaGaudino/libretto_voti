import voto
from voto import Libretto
from view import View
from voto import Voto
import flet as ft


class Controller(object):
    def __init__(self,view: View):
        self._view=view
        self._model=Libretto()
        self.startupLibretto()

    def handleAdd(self, e):
        nomeEsame = self._view._txtIn.value
        if nomeEsame=="":
            self._view._lvOut.controls.append(ft.Text("Il campo nome non può essere vuoto", color="red"))
            self._view.update()
            return
        strCfu = self._view._txtCFU.value
        try:
            strCfu = int(strCfu)
        except ValueError:
            self._view._lvOut.controls.append(ft.Text("Il campo cfu deve essere un intero", color="red"))
            self._view.update()
            return

        punteggio = self._view._ddVoto.value
        if punteggio==None:
            self._view._lvOut.controls.append(ft.Text("Il campo punteggio non può essere vuoto", color="red"))
            self._view.update()
            return
        if punteggio=="30L":
            punteggio=30
            lode = True
        else:
            punteggio=int(punteggio)
            lode = False

        data = self._view._datePicker.value
        if data==None:
            self._view._lvOut.controls.append(ft.Text("Seleziona una data", color="red"))
            self._view.update()
            return

        self._model.append(voto.Voto(nomeEsame, strCfu, punteggio, lode, f"{data.year}-{data.month}-{data.day}" ))
        self._view._lvOut.controls.append(ft.Text("Voto aggiunto correttamente"))
        self._view.update()



    def handlePrint(self, e):
        outList = self._model.stampaGUI()
        for elem in outList:
            self._view._lvOut.controls.append(ft.Text(elem))
        self._view.update()




    def startupLibretto(self):
        self._model.append((Voto("Fisica I", 10, 25, False, '2022-07-12')))
        self._model.append(Voto("Analisi 1", 10, 18, False, '2020-01-01'))
        self._model.append(Voto("Chimica", 8, 30, False, '2020-01-02'))
        self._model.append(Voto("Informatica", 8, 30, True, '2020-01-03'))
        self._model.append(Voto("Algebra Lineare", 10, 24, False, '2020-06-01'))
        self._model.append(Voto("Fisica 1", 10, 21, False, '2020-06-02'))
        self._model.stampa()