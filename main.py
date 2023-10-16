import os
import flet as ft
from extras.filepicker import archivo_seleccionado
from comprobaciones.comprobar_hoja import comprobar_hoja_excel
from envio_correos.enviar_correos import (
    enviar_correos_lincoln,
    enviar_correos_renacimiento,
)
from envio_correos.comprobar_documentos import comprobar_documentos_empleados

# Constantes para tamaños de texto, alineaciones y colores
TEXTO_GRANDE = 40
TEXTO_MEDIANO = 30
TEXTO_PEQUENO = 20
TEXTO_CENTRADO = ft.TextAlign.CENTER
NOMBRES_HOJAS_NOMINAS = "Hoja Renacimiento, Hoja Lincoln"
COLOR_PRIMARIO = "#3498db"
COLOR_SECUNDARIO = "#ecf0f1"


def configurar_pagina(page: ft.Page):
    """Configura las propiedades estéticas de la página."""
    page.title = "Automatización de Volantes"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_maximized = True
    page.background_color = COLOR_SECUNDARIO


def crear_ui(page: ft.Page):
    """Crea la interfaz de usuario del programa."""
    configurar_pagina(page)
    filepicker_popup = ft.FilePicker(on_result=archivo_seleccionado)
    page.overlay.append(filepicker_popup)

    def manejar_filepicker():
        try:
            filepicker_popup.pick_files(
                allow_multiple=False, allowed_extensions=["xlsx"]
            )
        except PermissionError:
            mostrar_alerta(
                "Hay un error, asegúrate de que el archivo seleccionado no esté abierto."
            )

    def comprobar_hoja():
        nombre_hoja = obtener_nombre_hojas()
        archivo = obtener_archivo()
        if not archivo:
            mostrar_alerta("Debes seleccionar un archivo Excel primero.")
        else:
            hojas_formateadas = list(map(lambda x: x.strip(), nombre_hoja.split(",")))
            hoja1, hoja2 = hojas_formateadas[0], hojas_formateadas[1]
            if comprobar_hoja_excel(archivo, hojas_formateadas):
                mostrar_alerta(
                    f"Las hojas '{hoja1}' y '{hoja2}' se encuentran en el archivo Excel."
                )
            else:
                mostrar_alerta(
                    f"La hoja '{hoja1}' o '{hoja2}' no se encuentran en el archivo Excel."
                )

    def enviar_excels():
        nombre_hoja = list(map(lambda x: x.strip(), obtener_nombre_hojas().split(",")))
        archivo = obtener_archivo()
        try:
            enviar_correos_renacimiento(
                "cesarcorn19@gmail.com",
                "pumr gwbl vcvw xkel",
                archivo,
                nombre_hoja[0],
            )
            enviar_correos_lincoln(
                "cesarcorn19@gmail.com",
                "pumr gwbl vcvw xkel",
                archivo,
                nombre_hoja[1],
            )
            mostrar_alerta("¡Se enviaron los documentos!")
        except PermissionError:
            mostrar_alerta(
                "Hubo un error, reinicia la aplicación y realiza el proceso de nuevo."
            )

    def comprobar_documentos_volantes():
        nombre_hoja = list(map(lambda x: x.strip(), obtener_nombre_hojas().split(",")))
        archivo = obtener_archivo()
        if comprobar_hoja_excel(archivo, nombre_hoja):
            comprobar_documentos_empleados(archivo, nombre_hoja)
            mostrar_alerta("¡Se enviaron los documentos a su correo!")
        else:
            mostrar_alerta(
                "Ocurrió un error, asegúrate de que las hojas escritas son correctas."
            )

    def mostrar_alerta(mensaje):
        titulo_alerta = ft.Text(mensaje)
        dlg = ft.AlertDialog(title=titulo_alerta)
        page.dialog = dlg
        dlg.open = True
        page.update()

    def obtener_nombre_hojas():
        return nombre_hojas.value

    def obtener_archivo():
        for nombre in os.listdir(os.getcwd()):
            if nombre.endswith((".xlsx")):
                return nombre
        return None

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
        on_click=lambda _: enviar_excels(),
        style=estilo_boton,
    )

    confirmar_hojas = ft.ElevatedButton(
        "Confirmar hojas",
        icon=ft.icons.CHECK,
        on_click=lambda _: comprobar_hoja(),
        style=estilo_boton,
    )

    comprobar_documentos = ft.ElevatedButton(
        "Comprobar documentos",
        icon=ft.icons.CHECK,
        on_click=lambda _: comprobar_documentos_volantes(),
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
                value="3) Compruebe de que todos los volantes esten correctos.",
                text_align=TEXTO_CENTRADO,
                size=TEXTO_PEQUENO,
            ),
            comprobar_documentos,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    paso_cuatro = ft.Column(
        [
            ft.Text(
                value="4) ¡Con esto estaría listo! Solo queda darle al botón de enviar:",
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
        paso_cuatro,
    )


ft.app(target=crear_ui)
