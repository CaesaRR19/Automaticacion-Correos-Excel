import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from datetime import datetime
import os

from buscar_empleados import (
    buscar_nombres_empleados_renacimiento,
    buscar_nombres_empleados_lincoln,
)
from buscar_correos import (
    buscar_correos_empleados_renacimiento,
    buscar_correos_empleados_lincoln,
)


def enviar_correos_renacimiento(correo, contrasena, nombre_libro, hoja_libro):
    fecha_actual = datetime.now()
    dia_del_mes = fecha_actual.day
    quincena = "primera" if dia_del_mes <= 15 else "segunda"
    correos = buscar_correos_empleados_renacimiento(nombre_libro, hoja_libro)
    nombre_empleado = buscar_nombres_empleados_renacimiento(nombre_libro, hoja_libro)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(correo, contrasena)

        # Iterar a través de los destinatarios
        for i, destinatario in enumerate(correos):
            msg = MIMEMultipart()
            msg["From"] = correo
            msg["Subject"] = "Volante de pago Flor de café"
            msg["To"] = destinatario
            msg.attach(
                MIMEText(
                    f"Volante de pago de {nombre_empleado[i]} de la {quincena} quincena, del mes #{fecha_actual.month}.",
                    "plain",
                )
            )

            nombre_archivo = os.listdir("excels_renacimiento")[i]
            ruta_archivo = os.path.join("excels_renacimiento", nombre_archivo)

            with open(ruta_archivo, "rb") as file:
                attach = MIMEApplication(file.read(), _subtype="xlsx")
                attach.add_header(
                    "Content-Disposition", f"attachment; filename={nombre_archivo}"
                )
                msg.attach(attach)

                server.sendmail(correo, destinatario, msg.as_string())


def enviar_correos_lincoln(correo, contrasena, nombre_libro, hoja_libro):
    fecha_actual = datetime.now()
    dia_del_mes = fecha_actual.day
    quincena = "primera" if dia_del_mes <= 15 else "segunda"
    correos = buscar_correos_empleados_lincoln(nombre_libro, hoja_libro)
    nombre_empleado = buscar_nombres_empleados_lincoln(nombre_libro, hoja_libro)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(correo, contrasena)

        # Iterar a través de los destinatarios
        for i, destinatario in enumerate(correos):
            msg = MIMEMultipart()
            msg["From"] = correo
            msg["Subject"] = "Volante de pago Flor de café"
            msg["To"] = destinatario
            msg.attach(
                MIMEText(
                    f"Volante de pago de {nombre_empleado[i]} de la {quincena} quincena, del mes #{fecha_actual.month}.",
                    "plain",
                )
            )

            nombre_archivo = os.listdir("excels_lincoln")[i]
            ruta_archivo = os.path.join("excels_lincoln", nombre_archivo)

            with open(ruta_archivo, "rb") as file:
                attach = MIMEApplication(file.read(), _subtype="xlsx")
                attach.add_header(
                    "Content-Disposition", f"attachment; filename={nombre_archivo}"
                )
                msg.attach(attach)

            server.sendmail(correo, destinatario, msg.as_string())

