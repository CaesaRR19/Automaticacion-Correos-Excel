import flet as ft

# Constantes para tamaños de texto, alineaciones y colores
TEXT_SIZE_LARGE = 40
TEXT_SIZE_MEDIUM = 30
TEXT_SIZE_SMALL = 20
TEXT_ALIGN_CENTER = ft.TextAlign.CENTER
DEFAULT_SHEET_NAMES = "Hoja Renacimiento, Hoja Lincoln"
PRIMARY_COLOR = "#3498db"
BACKGROUND_COLOR = "#ecf0f1"


def configure_page(page: ft.Page):
    page.title = "Automatización de Volantes"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.window_maximized = True
    page.background_color = BACKGROUND_COLOR


def create_ui(page: ft.Page):
    configure_page(page)
    pick_files_dialog = ft.FilePicker()
    page.overlay.append(pick_files_dialog)

    button_style = ft.ButtonStyle(
        bgcolor=PRIMARY_COLOR,
        color="white",
        padding=10,
    )

    titulo = ft.Text(
        value="Automatización de Volantes de pago Flor de Café",
        text_align=TEXT_ALIGN_CENTER,
        size=TEXT_SIZE_LARGE,
        color=PRIMARY_COLOR,
    )

    funcionamiento = ft.Text(
        value="¿Cómo funciona este programa?",
        text_align=TEXT_ALIGN_CENTER,
        size=TEXT_SIZE_MEDIUM,
        color=PRIMARY_COLOR,
    )

    agregar_archivos = ft.ElevatedButton(
        "Seleccionar archivo",
        icon=ft.icons.UPLOAD_FILE,
        on_click=lambda _: pick_files_dialog.pick_files(
            allow_multiple=False, allowed_extensions=["xlsx", "xls"]
        ),
        style=button_style,
    )

    nombre_hojas = ft.TextField(
        label="Nombre de hojas",
        hint_text=DEFAULT_SHEET_NAMES,
        text_align=ft.TextAlign.CENTER,
        color=PRIMARY_COLOR,
    )

    subir_documentos = ft.ElevatedButton(
        "Subir documentos",
        icon=ft.icons.UPLOAD_FILE,
        on_click=print("helo"),
        style=button_style,
    )

    paso_uno = ft.Column(
        [
            ft.Text(
                value="1) Ingrese el excel de la nómina:",
                text_align=TEXT_ALIGN_CENTER,
                size=TEXT_SIZE_SMALL,
            ),
            agregar_archivos,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    paso_dos = ft.Column(
        [
            ft.Text(
                value="2) Ingrese el nombre de las hojas donde se encuentren las nóminas:",
                text_align=TEXT_ALIGN_CENTER,
                size=TEXT_SIZE_SMALL,
            ),
            nombre_hojas,
        ],
        alignment=ft.MainAxisAlignment.CENTER,
    )

    paso_tres = ft.Column(
        [
            ft.Text(
                value="3) ¡Con esto estaría listo! Solo queda darle al botón de enviar:",
                text_align=TEXT_ALIGN_CENTER,
                size=TEXT_SIZE_SMALL,
            ),
            subir_documentos,
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


ft.app(target=create_ui)
