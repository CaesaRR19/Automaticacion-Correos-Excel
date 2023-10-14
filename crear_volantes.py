import os
import openpyxl
from openpyxl.styles import protection
from buscar_empleados import buscar_nombres_empleados_lincoln

def crear_volante_empleados_renacimiento(nombre_archivo, nombre_hoja):
    wb = openpyxl.load_workbook(nombre_archivo)
    empleados = buscar_nombres_empleados_lincoln(nombre_archivo, nombre_hoja)
    if not os.path.exists("excels"):
        os.mkdir("excels")
    for datos in empleados:
        ws = wb['Volante Renacimiento']
        ws['D3'] = datos
        nombre_archivo_excel = f'excels/{datos}_Volante.xlsx'
        
        # Proteger la hoja de trabajo con una contraseña
        password = "FlorDeCafe141023"  # Reemplaza "tu_contraseña" con la contraseña que desees
        ws.protection.set_password(password)
        ws.protection.sheet = True  # Esto protegerá toda la hoja
        
        for hoja in wb.sheetnames:
            if hoja != "Volante":
                wb[hoja].sheet_state = "hidden"
        wb.save(nombre_archivo_excel)
    wb.close()
    return None
