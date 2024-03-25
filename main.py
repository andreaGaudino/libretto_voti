import flet as ft
from view import View
from controller import Controller

def main(page: ft.Page):
    v=View(page)
    c=Controller(View)
    v.setController(c)
    v.caricaInterfaccia()


ft.app(target=main)