import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import os

from crear_volantes import (
    crear_volante_empleados_renacimiento,
    crear_volante_empleados_lincoln,
)

def comprobar_documentos_empleados(nombre_libro, renacimiento_hoja, lincoln_hoja):
    crear_volante_empleados_renacimiento(nombre_libro, renacimiento_hoja)
    crear_volante_empleados_lincoln(nombre_libro, lincoln_hoja)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login("cesarcorn19@gmail.com", "pumr gwbl vcvw xkel")

        msg = MIMEMultipart()
        msg["From"] = "cesarcorn19@gmail.com"
        msg["Subject"] = "Comprobación volante de pago Flor de café"
        msg["To"] = "coramosnolasco@gmail.com"

        # Adjuntar archivos de la carpeta excels_renacimiento
        excel_renacimiento_folder = "excels_renacimiento"
        for nombre_archivo in os.listdir(excel_renacimiento_folder):
            ruta_archivo = os.path.join(excel_renacimiento_folder, nombre_archivo)
            with open(ruta_archivo, "rb") as file:
                attach = MIMEApplication(file.read(), _subtype="xlsx")
                attach.add_header("Content-Disposition", f"attachment; filename={nombre_archivo}")
                msg.attach(attach)

        # Adjuntar archivos de la carpeta excels_lincoln
        excel_lincoln_folder = "excels_lincoln"
        for nombre_archivo in os.listdir(excel_lincoln_folder):
            ruta_archivo = os.path.join(excel_lincoln_folder, nombre_archivo)
            with open(ruta_archivo, "rb") as file:
                attach = MIMEApplication(file.read(), _subtype="xlsx")
                attach.add_header("Content-Disposition", f"attachment; filename={nombre_archivo}")
                msg.attach(attach)

        server.sendmail("cesarcorn19@gmail.com", "coramosnolasco@gmail.com", msg.as_string())
        return None
