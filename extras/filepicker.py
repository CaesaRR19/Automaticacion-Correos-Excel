"""Este modulo tiene la funcion archvo seleccionado, la cual me permite crear una copia del archivo seleccionado.
"""
import os
import shutil
import flet as ft


def archivo_seleccionado(e: ft.FilePickerResultEvent):
    """
    Esta función elimina todos los archivos con extensiones .xlsx en el directorio actual
    y luego copia el archivo seleccionado al directorio actual.

    Args:
        e (ft.FilePickerResultEvent): El evento de resultado del FilePicker que contiene
        información sobre el archivo seleccionado.
    """
    if e.files is not None:
        directorio_actual = os.getcwd()
        for archivo in os.listdir(directorio_actual):
            if archivo.endswith((".xlsx")):
                archivo_borrado = os.path.join(directorio_actual, archivo)
                os.remove(archivo_borrado)

        archivo_subido = e.files[0]

        # Accede a los atributos del objeto FilePickerFile utilizando el operador de punto
        ruta_archivo = archivo_subido.path
        nombre_archivo = os.path.basename(ruta_archivo)

        print(nombre_archivo)

        # Define la ubicación de destino (en el directorio actual)
        destino_archivo_subido = os.path.join(directorio_actual, nombre_archivo)

        # Copia el archivo seleccionado al directorio de destino
        shutil.copyfile(ruta_archivo, destino_archivo_subido)
