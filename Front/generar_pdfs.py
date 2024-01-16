import pdfkit
import win32api
from jinja2 import Template
import win32print
import os
import pdfkit
from jinja2 import Template
import os
def print_file(file):
    win32api.ShellExecute(0,'print', file,win32print.GetDefaultPrinter(),'.',0)

def pdf_colilla(fecha_actual, socio, valor_total, fecha_desde, fecha_hasta, recibio, nombre_titular, cedula_titular):
    html_style = """
    <p style="text-align: center;"><strong>FUNERARIA LA ASCENSI&Oacute;N</strong></p>
    <p style="text-align: center;"><strong>NIT: 39.191.604</strong></p>
    <p style="text-align: center;"><strong>COLILLA DE PAGO SERVICIO PROEXEQUIAL</strong></p>
    <p style="text-align: center;"><strong>__________________________________________________</strong></p>
    <p style="text-align: center;"><strong>FECHA:&nbsp;</strong>{{fecha_actual}}</p>
    <h2 style="text-align: center;"><strong>SOCIO: </strong>{{socio}}<strong><br /></strong></h2>
    <p style="text-align: center;"><strong>NOMBRE TITULAR: </strong>{{nombre_titular}}</p>
    <p style="text-align: center;"><strong>C&Eacute;DULA TITULAR:</strong> {{cedula_titular}}</p>
    <h2 style="text-align: center;"><strong>VALOR: </strong>{{valor_total}}<strong><br /></strong></h2>
    <p style="text-align: center;"><strong>DESDE: </strong>{{fecha_hasta_anterior}}<strong><br /></strong></p>
    <p style="text-align: center;"><strong>HASTA: </strong>{{feche_hasta}}<strong><br /></strong></p>
    <p style="text-align: center;"><strong>RECIBIO: </strong>{{usuario_encargado}}<strong><br /></strong></p>
    <p style="text-align: center;">&nbsp;</p>
    <p style="text-align: center;"><strong>FIRMA: _______________________________</strong></p>
    """

    # Datos de contexto
    context = {
        'fecha_actual': fecha_actual,
        'socio': str(socio),
        'nombre_titular':str(nombre_titular),
        'cedula_titular':str(cedula_titular),
        'valor_total': str(valor_total),
        'fecha_hasta_anterior': fecha_desde,
        'feche_hasta': fecha_hasta,
        'usuario_encargado': str(recibio)
    }

    # Renderizar el HTML con los datos de contexto
    template = Template(html_style)
    rendered_html = template.render(context)

    # Configuración de PDFKit con tamaño de página A4 (por ejemplo)
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    options = {'page-width': '80mm',
        'page-height': '140mm',
        'margin-top': '0',
        'margin-right': '0',
        'margin-bottom': '0',
        'margin-left': '0',
    }
    nombre_pdf = str(socio) + '.pdf'
    print(nombre_pdf)

    colillas_path = r"C:\Users\Jose\OneDrive - UCO\Desktop\proyecto funeraria\colillas"

    # Ruta completa del archivo PDF
    pdf_path = os.path.join(colillas_path, nombre_pdf)

    # Generar el PDF con opciones de tamaño de página
    pdfkit.from_string(rendered_html, pdf_path, configuration=config, options=options)

    print_file(pdf_path)



def pdf_factura_caja(ciudad, fecha_actual, usuario_encargado, nombre_coprador,descripcion, valor_restanate , valor_abonado):
    html_style = """
       <p style="text-align: center;"><strong>LA UNION:</strong> 3104718651 - 3146774935&nbsp; &nbsp;<strong>SONS&Oacute;N:</strong> 8694654&nbsp;</p>
<p style="text-align: center;"><strong>ABEJORRAL:</strong> 8647631&nbsp; &nbsp;<strong>LA CEJA:</strong> 5532434</p>
<p style="text-align: center;"><strong>NARI&Ntilde;O:</strong> 3105462139</p>
<h2 style="text-align: center;"><strong>RECIBOS DE CAJA</strong></h2>
<p style="text-align: center;">_____________________________________________________</p>
<p style="text-align: center;"><strong>CIUDAD: </strong>{{ciudad}}</p>
<p style="text-align: center;"><strong>FECHA: </strong>{{fecha_actual}}</p>
<p style="text-align: center;"><strong>RECIBIMOS DE: </strong>{{nombre_comprador}}</p>
<p style="text-align: center;"><strong>RECIBIO: </strong>{{usuario_encargado}}</p>
<p style="text-align: center;"><strong>POR CONCEPTO DE: </strong>{{descripcion}}</p>
<p style="text-align: center;"><strong>VALOR ABONADO: </strong>{{valor_abonado}}</p>
<p style="text-align: center;"><strong>RESTA: </strong>{{valor_restante}}</p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;"><strong>FIRMA:_________________________________________</strong></p>
<p style="text-align: center;">&nbsp;</p>
<p>&nbsp;</p>


        """

    # Datos de contexto
    context = {
        'fecha_actual': fecha_actual,
        'ciudad': str(ciudad),
        'usuario_encargado': str(usuario_encargado),
        'nombre_comprador': str(nombre_coprador),
        'descripcion': descripcion,
        'valor_abonado': str(valor_abonado),
        'valor_restante': str(valor_restanate)
    }

    # Renderizar el HTML con los datos de contexto
    template = Template(html_style)
    rendered_html = template.render(context)

    # Configuración de PDFKit
    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
    nombre_pdf = 'caja' +' '+ nombre_coprador + '.pdf'
    print(nombre_pdf)

    adicioanles_path = r"C:\Users\Ascension\Desktop\proyecto_funeraria\proyecto funeraria\facturas caja"

    # Ruta completa del archivo PDF
    pdf_path = os.path.join(adicioanles_path, nombre_pdf)

    # Generar el PDF
    pdfkit.from_string(rendered_html, pdf_path, configuration=config)

    print_file(pdf_path)


