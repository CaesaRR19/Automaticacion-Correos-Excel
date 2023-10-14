import openpyxl
import flet as ft


def comprobar_hoja_excel(archivo, nombre_hoja: list):
    try:
        workbook = openpyxl.load_workbook(archivo)
        return all(item in workbook.sheetnames for item in nombre_hoja)
    except Exception as e:
        print(f"Error al abrir el archivo Excel: {str(e)}")
        dlg = ft.AlertDialog(
            title=ft.Text(
                "Hay un error, asegurate de que el archivo seleccionado no esté abierto."
            )
        )
        dlg.open = True
        dlg.update()
