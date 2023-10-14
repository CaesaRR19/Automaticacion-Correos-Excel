"""Este módulo es el que se encarga de la parte visual del programa.
"""

import flet as ft
import os
from filepicker import archivo_seleccionado
from comprobar_hoja import comprobar_hoja_excel

# Constantes para tamaños de texto, alineaciones y colores
TEXTO_GRANDE = 40
TEXTO_MEDIANO = 30
TEXTO_PEQUENO = 20
TEXTO_CENTRADO = ft.TextAlign.CENTER
NOMBRES_HOJAS_NOMINAS = "Hoja Renacimiento, Hoja Lincoln"
COLOR_PRIMARIO = "#3498db"
COLOR_SECUNDARIO = "#ecf0f1"


def configurar_pagina(page: ft.Page):
    """Es la que le da las configuraciones esteticas a una pagina.
    Args:
        page (ft.Page): Pagina a la que será aplicada
    """
    page.title = "Automatización de Volantes"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_maximized = True
    page.background_color = COLOR_SECUNDARIO


def crear_ui(page: ft.Page):
    """Esta función es la que crea toda la interfaz de usuario del programa.
    Args:
        page (ft.Page): _description_
    """
    configurar_pagina(page)
    filepicker_popup = ft.FilePicker(on_result=archivo_seleccionado)
    page.overlay.append(filepicker_popup)

    def manejar_filepicker():
        try:
            # Intenta ejecutar el filepicker
            filepicker_popup.pick_files(
                allow_multiple=False, allowed_extensions=["xlsx", "xls"]
            )
        except Exception as e:
            # En caso de error, muestra una alerta con el mensaje de error
            print("error", e)
            dlg = ft.AlertDialog(
                title=ft.Text(
                    "Hay un error, asegurate de que el archivo seleccionado no esté abierto."
                )
            )
            page.dialog = dlg
            dlg.open = True
            page.update()

    def comprobar_hoja():
        nombre_hoja = nombre_hojas.value.split(",")
        hojas_formateadas = list(map(lambda x: x.strip(),nombre_hoja))
        hoja1, hoja2 = hojas_formateadas[0], hojas_formateadas[1]
        nombre = None

        for nombre in os.listdir(os.getcwd()):
            if nombre.endswith((".xls", ".xlsx")):
                archivo = nombre

        if not archivo:
            titulo_alerta = ft.Text("Debes seleccionar un archivo Excel primero.")
            dlg = ft.AlertDialog(title=titulo_alerta)
        else:
            if comprobar_hoja_excel(archivo, hojas_formateadas):
                titulo_alerta = ft.Text(
                    f"Las hojas '{hoja1}' y '{hoja2}' se encuentran en el archivo Excel."
                )
                dlg = ft.AlertDialog(title=titulo_alerta)
            else:
                titulo_alerta = ft.Text(
                    f"La hoja '{hoja1}' o '{hoja2}' no se encuentran en el archivo Excel."
                )
                dlg = ft.AlertDialog(title=titulo_alerta)
        page.dialog = dlg
        dlg.open = True
        page.update()
        

    estilo_boton = ft.ButtonStyle(
        bgcolor=COLOR_PRIMARIO,
        color="white",
        padding=10,
    )

    titulo = ft.Text(
        value="Automatización de Volantes de pago Flor de Café",
        text_align=TEXTO_CENTRADO,
        size=TEXTO_GRANDE,
        color=COLOR_PRIMARIO,
    )

    funcionamiento = ft.Text(
        value="¿Cómo funciona este programa?",
        text_align=TEXTO_CENTRADO,
        size=TEXTO_MEDIANO,
        color=COLOR_PRIMARIO,
    )

    agregar_archivos = ft.ElevatedButton(
        "Seleccionar archivo",
        icon=ft.icons.UPLOAD_FILE,
        on_click=lambda _: manejar_filepicker(),
        style=estilo_boton,
    )

    nombre_hojas = ft.TextField(
        label="Nombre de hojas",
        hint_text=NOMBRES_HOJAS_NOMINAS,
        text_align=ft.TextAlign.CENTER,
        color=COLOR_PRIMARIO,
    )

    enviar_documentos = ft.ElevatedButton(
        "Enviar documentos",
        icon=ft.icons.UPLOAD_FILE,
        on_click="hola",
        style=estilo_boton,
    )

    confirmar_hojas = ft.ElevatedButton(
        "Confirmar hojas",
        icon=ft.icons.CHECK,
        on_click=lambda _: comprobar_hoja(),
        style=estilo_boton,
    )

    paso_uno = ft.Column(
        [
            ft.Text(
                value="1) Ingrese el excel de la nómina:",
                text_align=TEXTO_CENTRADO,
                size=TEXTO_PEQUENO,
            ),
            agregar_archivos,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    paso_dos = ft.Column(
        [
            ft.Text(
                value="2) Ingrese el nombre de las hojas donde se encuentren las nóminas:",
                text_align=TEXTO_CENTRADO,
                size=TEXTO_PEQUENO,
            ),
            nombre_hojas,
            confirmar_hojas,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    paso_tres = ft.Column(
        [
            ft.Text(
                value="3) ¡Con esto estaría listo! Solo queda darle al botón de enviar:",
                text_align=TEXTO_CENTRADO,
                size=TEXTO_PEQUENO,
            ),
            enviar_documentos,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    page.add(
        ft.Row([titulo], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row([funcionamiento], alignment=ft.MainAxisAlignment.CENTER),
        paso_uno,
        paso_dos,
        paso_tres,
    )


ft.app(target=crear_ui)
