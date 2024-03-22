import pdfkit
import win32api
from jinja2 import Template
import win32print
import os
import pdfkit
from jinja2 import Template
import time
from fpdf import FPDF
import PyPDF2
import os
import io
from PyPDF2 import PdfFileReader, PdfFileWriter
from reportlab.pdfgen import canvas
import requests
import subprocess

serial = ""
grados = "0"  # Múltiplo de 90 pero como cadena
impresora = "Microsoft Print to PDF"


import aspose.pdf as pdf


def print_file(file):
    win32api.ShellExecute(0,'print', file,win32print.GetDefaultPrinter(),'.',0)





def pdf_colilla(fecha_actual, socio, valor_total, fecha_desde, fecha_hasta, recibio, nombre_titular, cedula_titular):
    pdf = FPDF(orientation='P', unit='mm', format=(80, 140))
    pdf.add_page()

    # Configurar fuente y tamaño
    pdf.set_font('Arial', 'B', 9)
    pdf.set_auto_page_break(auto=True, margin=0)
    centro_x = pdf.w
    print(centro_x)
    pdf.image('ico.png', x=22, y=2, w=35)
    #pdf.image('sellomarca.jpg', x=13, y=45, w=55)

    # Agregar contenido al PDF
    pdf.set_y(25)
    pdf.cell(60, 5, txt="FUNERARIA LA ASCENSIÓN", align='C')
    pdf.cell(60, 5, txt="NIT: 39.191.604", ln=True, align='C')
    pdf.cell(60, 5, txt="COLILLA DE PAGO SERVICIO PROEXEQUIAL", ln=True, align='C')
    pdf.cell(60, 5, txt="__________________________________________________", ln=True, align='C')
    pdf.set_font('Arial', '', 9)
    pdf.cell(60, 5, txt="FECHA: " + fecha_actual.strftime("%d/%m/%Y"), ln=True, align='C')
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(60, 5, txt="SOCIO: " + str(socio), ln=True, align='C')
    pdf.set_font('Arial', '', 9)
    pdf.cell(60, 5, txt="NOMBRE TITULAR: " + str(nombre_titular), ln=True, align='C')
    pdf.cell(60, 5, txt="CÉDULA TITULAR: " + str(cedula_titular), ln=True, align='C')
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(60, 5, txt="VALOR: " + str(valor_total), ln=True, align='C')
    pdf.set_font('Arial', '', 9)
    pdf.cell(60, 5, txt="DESDE: " + fecha_desde.strftime("%d/%m/%Y"), ln=True, align='C')
    pdf.cell(60, 5, txt="HASTA: " + fecha_hasta.strftime("%d/%m/%Y"), ln=True, align='C')
    pdf.cell(60, 5, txt="RECIBIO: " + str(recibio), ln=True, align='C')
    pdf.cell(60, 5, txt="", ln=True, align='C')  # Espacio en blanco
    pdf.cell(60, 5, txt="FIRMA: _______________________________", ln=True, align='C')

    # Guardar el PDF en un archivo
    nombre_pdf = str(socio) + '.pdf'
    colillas_path = r"C:\Users\Jose\OneDrive - UCO\Desktop\proyecto funeraria\colillas"
    pdf_path2 = os.path.join(colillas_path, nombre_pdf)
    pdf.output(pdf_path2)
    print_file(pdf_path2)




def pdf_factura_caja(ciudad, fecha_actual, usuario_encargado, nombre_coprador,documento_comprador,descripcion, valor_restanate , valor_abonado, valor_total):
    html_style = """
<p style="text-align: center;"><strong>LA UNI&Oacute;N:</strong> 3104718651 - 3146774935&nbsp; &nbsp;<strong>SONS&Oacute;N:</strong> 8694654&nbsp;</p>
<p style="text-align: center;"><strong>ABEJORRAL:</strong> 8647631&nbsp; &nbsp;<strong>LA CEJA:</strong> 5532434</p>
<p style="text-align: center;"><strong>NARI&Ntilde;O:</strong> 3105462139</p>
<h2 style="text-align: center;"><strong>RECIBOS DE CAJA</strong></h2>
<p style="text-align: center;">_____________________________________________________</p>
<p style="text-align: center;"><strong>CIUDAD: </strong>{{ciudad}}</p>
<p style="text-align: center;"><strong>FECHA: </strong>{{fecha_actual}}</p>
<p style="text-align: center;"><strong>NOMBRE COMPRADOR: </strong>{{nombre_comprador}}</p>
<p style="text-align: center;"><strong>DOCUMENTO COMPRADOR: </strong>{{documento_comprador}}</p>
<p style="text-align: center;"><strong>POR CONCEPTO DE: </strong>{{descripcion}}</p>
<p style="text-align: center;"><strong>VALOR TOTAL: </strong>{{valor_total}}</p>
<p style="text-align: center;"><strong>VALOR ABONADO: </strong>{{valor_abonado}}</p>
<p style="text-align: center;"><strong>RESTA: </strong>{{valor_restante}}</p>
<p style="text-align: center;"><strong>RECIBIO: </strong>{{usuario_encargado}}</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;"><strong>FIRMA:_________________________________________</strong></p>
<p style="text-align: center;">&nbsp;</p>
<p>&nbsp;</p><p>"""
    # Datos de contexto
    context = {
        'fecha_actual': fecha_actual,
        'ciudad': str(ciudad),
        'usuario_encargado': str(usuario_encargado),
        'nombre_comprador': str(nombre_coprador),
        'descripcion': descripcion,
        'valor_abonado': str(valor_abonado),
        'valor_restante': str(valor_restanate),
        'documento_comprador': str(documento_comprador),
        'valor_total':str(valor_total)
    }

    # Renderizar el HTML con los datos de contexto
    template = Template(html_style)
    rendered_html = template.render(context)

    # Configuración de PDFKit
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    options = {'page-width': '80mm',
               'page-height': '200mm',
               'margin-top': '0',
               'margin-right': '0',
               'margin-bottom': '0',
               'margin-left': '0',
               }
    nombre_pdf = 'caja' +' '+ nombre_coprador + '.pdf'
    print(nombre_pdf)

    adicioanles_path = r"C:\Users\Jose\OneDrive - UCO\Desktop\proyecto funeraria\facturas caja"

    # Ruta completa del archivo PDF
    pdf_path = os.path.join(adicioanles_path, nombre_pdf)

    # Generar el PDF
    pdfkit.from_string(rendered_html, pdf_path, configuration=config, options=options)

    print_file(pdf_path)


