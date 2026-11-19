import flet as ft
from UI.controller import Controller
from UI.view import View
from model.model import Model

def main(page: ft.Page):
    model = Model()
    view = View(page)
    controller = Controller(view, model)
    view.set_controller(controller)
    view.load_interface()


ft.app(target=main)
