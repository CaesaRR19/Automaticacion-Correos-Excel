import os
import shutil
import flet as ft


def archivo_seleccionado(e: ft.FilePickerResultEvent):
    """
    Esta función elimina todos los archivos con extensiones .xlsx y .xls en el directorio actual
    y luego copia el archivo seleccionado al directorio actual.

    Args:
        e (ft.FilePickerResultEvent): El evento de resultado del FilePicker que contiene
        información sobre el archivo seleccionado.
    """
    directorio_actual = os.getcwd()
    for archivo in os.listdir(directorio_actual):
        if archivo.endswith((".xlsx", ".xls")):
            archivo_borrado = os.path.join(directorio_actual, archivo)
            os.remove(archivo_borrado)
    archivo_subido = e.files[0]

    # Accede a los atributos del objeto FilePickerFile utilizando el operador de punto
    ruta_archivo = archivo_subido.path
    nombre_archivo = os.path.basename(ruta_archivo)

    print(ruta_archivo)

    # Define la ubicación de destino (en el directorio actual)
    destino_archivo_subido = os.path.join(directorio_actual, nombre_archivo)

    # Copia el archivo seleccionado al directorio de destino
    shutil.copyfile(ruta_archivo, destino_archivo_subido)
