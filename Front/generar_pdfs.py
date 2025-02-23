import win32api
import win32print
from fpdf import FPDF
import os, sys
import time
import datetime


#def print_file(file):
#    win32api.ShellExecute(0,'print', file,win32print.GetDefaultPrinter(),'.',0)

def resolver_ruta(ruta_relativa):

    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, ruta_relativa)
    return os.path.join(os.path.abspath('.'), ruta_relativa)


def pdf_colilla(fecha_actual, socio, valor_total, fecha_desde, fecha_hasta, recibio, nombre_titular, cedula_titular):
    def resolver_ruta2(nombre_archivo):
        return os.path.join(r"Front", nombre_archivo)

    def generar_pdf_con_imagen_sello(incluir_sello):
        pdf = FPDF(orientation='P', unit='mm', format=(80, 140))
        pdf.add_page()

        pdf.set_font('Arial', 'B', 9)
        pdf.set_auto_page_break(auto=True, margin=5)
        pdf.image(resolver_ruta('ico2.png'), x=22, y=2, w=35)

        if incluir_sello:
            pdf.image(resolver_ruta('sellomarca.jpg'), x=13, y=45, w=55)

        pdf.set_y(25)
        pdf.cell(60, 5, txt="NIT: 39.191.604", ln=True, align='C')
        pdf.cell(60, 5, txt="314 677 4935 - 310 471 8651", ln=True, align='C')
        pdf.cell(60, 5, txt="COLILLA DE PAGO SERVICIO PROEXEQUIAL", ln=True, align='C')
        pdf.cell(60, 5, txt="__________________________________________________", ln=True, align='C')

        pdf.set_font('Arial', '', 9)
        pdf.cell(60, 5, txt=f"FECHA: {fecha_actual.strftime('%d/%m/%Y')}", ln=True, align='C')

        pdf.set_font('Arial', 'B', 11)
        pdf.multi_cell(60, 5, txt=f"SOCIO: {socio}", align='C')

        pdf.set_font('Arial', '', 9)
        pdf.multi_cell(60, 5, txt=f"NOMBRE TITULAR: {nombre_titular}", align='C')
        pdf.multi_cell(60, 5, txt=f"CÉDULA TITULAR: {cedula_titular}", align='C')

        pdf.set_font('Arial', 'B', 11)
        pdf.cell(60, 5, txt=f"VALOR: ${valor_total:,.2f}", ln=True, align='C')

        pdf.set_font('Arial', '', 9)
        pdf.cell(60, 5, txt=f"DESDE: {fecha_desde.strftime('%d/%m/%Y')}", ln=True, align='C')
        pdf.cell(60, 5, txt=f"HASTA: {fecha_hasta.strftime('%d/%m/%Y')}", ln=True, align='C')

        pdf.multi_cell(60, 5, txt=f"RECIBIÓ: {recibio}", align='C')

        pdf.cell(60, 5, txt="", ln=True, align='C')  # Espacio en blanco
        pdf.cell(60, 5, txt="FIRMA: _______________________________", ln=True, align='C')

        colillas_path = r"C:\Users\Ascension\Desktop\proyectoFuneraria\colillas"
        if not os.path.exists(colillas_path):
            os.makedirs(colillas_path)

        nombre_pdf = f"{socio}_{fecha_desde.strftime('%d_%m_%Y')}_{fecha_hasta.strftime('%d_%m_%Y')}.pdf"
        pdf_path = os.path.join(colillas_path, nombre_pdf)
        pdf.output(pdf_path)

        return pdf_path

    # Generar y guardar el PDF sin la imagen sellomarca
    pdf_path_sin_sello = generar_pdf_con_imagen_sello(incluir_sello=False)
    print_file(pdf_path_sin_sello)
    return pdf_path_sin_sello



def print_file(filepath):
    os.startfile(filepath, "print")

def pdf_factura_caja(ciudad, fecha_actual, usuario_encargado, nombre_comprador, documento_comprador, descripciones, valores_unitarios, valor_restante, valor_abonado, valor_total):
    pdf = FPDF(orientation='P', unit='mm', format=(140, 215))  # Media hoja carta
    pdf.add_page()

    # Configurar fuente
    pdf.set_font('Arial', 'B', 12)
    pdf.image(resolver_ruta('ico2.png'), x=50, y=5, w=40)  # Logo centrado

    # Información general
    pdf.set_y(45)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(0, 5, "NIT: 39.191.604", ln=True, align='C')
    pdf.cell(0, 5, "Teléfonos:", ln=True, align='C')
    pdf.set_font('Arial', '', 9)
    pdf.cell(0, 5, "LA UNIÓN: 310 471 8651 - 314 677 4935", ln=True, align='C')
    pdf.cell(0, 5, "SONSÓN: 320 759 4046 - 300 198 7059", ln=True, align='C')
    pdf.cell(0, 5, "ABEJORRAL: 864 7631", ln=True, align='C')
    pdf.cell(0, 5, "LA CEJA: 553 2434", ln=True, align='C')
    pdf.cell(0, 5, "NARIÑO: 310 546 2139", ln=True, align='C')
    pdf.cell(0, 5, "-" * 70, ln=True, align='C')
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(0, 5, "RECIBO DE CAJA", ln=True, align='C')
    pdf.cell(0, 5, "-" * 70, ln=True, align='C')

    # Datos de la transacción
    pdf.set_font('Arial', '', 10)
    pdf.cell(0, 5, f"Ciudad: {ciudad}", ln=True, align='L')
    pdf.cell(0, 5, f"Fecha: {fecha_actual.strftime('%d/%m/%Y')}", ln=True, align='L')
    pdf.cell(0, 5, f"Comprador: {nombre_comprador}", ln=True, align='L')
    pdf.cell(0, 5, f"Documento: {documento_comprador}", ln=True, align='L')

    # Tabla para descripciones y valores
    pdf.set_y(pdf.get_y() + 5)  # Espaciado antes de la tabla
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(90, 6, "Concepto", border=1, align='C')
    pdf.cell(30, 6, "Valor Unitario", border=1, ln=True, align='C')

    pdf.set_font('Arial', '', 10)
    for desc, valor in zip(descripciones, valores_unitarios):
        pdf.cell(90, 6, desc, border=1, align='C')
        pdf.cell(30, 6, f"${valor:,.2f}", border=1, ln=True, align='C')

    # Totales
    pdf.set_y(pdf.get_y() + 5)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 5, f"Valor Total: ${valor_total:,.2f}", ln=True, align='L')
    pdf.cell(0, 5, f"Valor Abonado: ${valor_abonado:,.2f}", ln=True, align='L')
    pdf.cell(0, 5, f"Resta: ${valor_restante:,.2f}", ln=True, align='L')

    # Firma
    pdf.set_y(pdf.get_y() + 10)
    pdf.set_font('Arial', '', 10)
    pdf.cell(0, 5, f"Recibió: {usuario_encargado}", ln=True, align='L')
    pdf.set_y(pdf.get_y() + 5) 
    pdf.cell(0, 5, "Firma: _______________________________", ln=True, align='L')

    # Guardar el PDF
    nombre_pdf = f'caja_{nombre_comprador}.pdf'
    carpeta_guardado = r"C:\Users\Ascension\Desktop\proyectoFuneraria\facturas caja"
    pdf_path = os.path.join(carpeta_guardado, nombre_pdf)
    pdf.output(pdf_path)

    print(f"PDF generado: {pdf_path}")



def generar_pdf_proexequial(fecha, documentos, nombres, fechas_nacimiento, fechas_afiliacion, socio, ciudad):
    # Validar formato de las listas
    try:
        fechas_nacimiento = [fecha.strftime("%d/%m/%Y") if isinstance(fecha, datetime.date) else str(fecha) for fecha in fechas_nacimiento]
        fechas_afiliacion = [fecha.strftime("%d/%m/%Y") if isinstance(fecha, datetime.date) else str(fecha) for fecha in fechas_afiliacion]
        documentos = [str(doc) for doc in documentos]
        nombres = [str(nom) for nom in nombres]
    except Exception as e:
        print(f"Error al formatear los datos: {e}")
        return

    # Configurar PDF
    pdf = FPDF(orientation='P', unit='mm', format=(210, 297))  # Tamaño A4
    pdf.add_page()
    pdf.set_font('Arial', '', 10)

    # Logo
    pdf.image(resolver_ruta('ico2.png'), x=10, y=10, w=60)

    # Información de contacto
    pdf.set_xy(100, 10)
    direcciones = [
        "La Ceja Ed. Tahami local 103 Tel: 553 2434}",
        "La Unión Calle 13 No. 9-80 Cel: 314 677 4935 - 310 471 8651",
        "Sonsón Parque Principal Tel: 320 759 4046 - 300 198 7059",
        "Abejorral (Ant.) Media cuadra del parque principal Tel: 864 7631",
        "Nariño - Calle Real Cel: 310 546 2139"
    ]
    for direccion in direcciones:
        pdf.cell(0, 5, direccion, ln=True, align='L')
        pdf.set_x(100)

    # Título del formulario
    pdf.set_xy(10, 60)
    pdf.set_font('Arial', 'B', 20)
    pdf.cell(190, 10, "PROEXEQUIAL LA ASCENSIÓN", ln=True, align='C')
    pdf.set_font('Arial', '', 18)
    pdf.cell(190, 10, f"PROMESA EXEQUIAL N° {socio}", ln=True, align='C')

    # Fecha
    pdf.set_font('Arial', '', 12)
    pdf.ln(5)
    pdf.cell(190, 5, f"Fecha: {fecha}", ln=True, align='L')

    # Texto principal
    texto = (f"Yo, {nombres[0]}, mayor de edad, vecino de {ciudad}, identificado con N.I. {documentos[0]}, nacido el {fechas_nacimiento[0]}, afiliado el {fechas_afiliacion[0]}; solicito a FUNERARIA LA ASCENSIÓN el servicio exequial en caso de mi fallecimiento o de mis parientes directos que se detallan a continuación.")
    pdf.multi_cell(190, 5, texto, align='L')

    # Tabla de beneficiarios
    pdf.ln(5)
    pdf.set_font('Arial', 'B', 10)
    pdf.cell(38, 8, "Cédula o NIT", border=1, align='C')
    pdf.cell(77, 8, "Nombres y Apellidos", border=1, align='C')
    pdf.cell(38, 8, "Fecha de Nacimiento", border=1, align='C')
    pdf.cell(38, 8, "Fecha de Afiliación", border=1, ln=True, align='C')

    pdf.set_font('Arial', '', 10)
    for doc, nombre, fecha_nac, fecha_afiliacion in zip(documentos[1:], nombres[1:], fechas_nacimiento[1:], fechas_afiliacion[1:]):
        pdf.cell(38, 8, doc, border=1, align='C')
        pdf.cell(77, 8, nombre, border=1, align='C')
        pdf.cell(38, 8, fecha_nac, border=1, align='C')
        pdf.cell(38, 8, fecha_afiliacion, border=1, ln=True, align='C')

    # Firma
    pdf.ln(10)
    pdf.cell(190, 12, "Firma del Titular: _______________________________________", ln=True, align='L')
    pdf.cell(190, 12, "Firma del Vendedor: ______________________________________", ln=True, align='L')

         
    # Agregar nueva página con texto adicional
    pdf.add_page()

    # Logo
    pdf.image(resolver_ruta('ico2.png'), x=10, y=10, w=40)

    # Título de la última página
    pdf.set_xy(10, 50)
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(190, 10, "CONDICIONES DEL PROEXEQUIAL", ln=True, align='C')

    pdf.set_font('Arial', '', 9.5)
    pdf.multi_cell(190, 5, """
    1. REQUISITOS:
    1.1 Para suscribir al programa la persona no podrá estar padeciendo grave enfermedad; en caso de verificar lo contrario, los servicios a los que se refiere este programa, no serán prestados y tanto el titular como los beneficiarios, renuncian a cualquier reclamación judicial o extrajudicial.
    1.2 En caso de fallecer cualquiera de las personas inscritas por causas naturales, podrá solicitar el servicio siempre y cuando hayan transcurrido como mínimo, treinta (30) días después de la inscripción.
    2. SERVICIOS:
    2.1 Los servicios los prestará únicamente Funeraria LA ASCENSIÓN u otra entidad funeraria por nosotros autorizada. De no hacerlo perderá todos los derechos a reclamar, es decir se exonera de cualquier responsabilidad a la Funeraria.
    3. PLAN BÁSICO (P.B.): Derechos Parroquiales, servicio de coche fúnebre, cofre fúnebre, alumbrado, útiles para velación, tanatopraxia (preservación del cuerpo), personal para el cortejo, (dos grupos: damas y caballeros), carteles, trámites civiles y eclesiásticos.
    4. SERVICIOS ADICIONALES (S.A.):
    4.1 Sala de velación hasta por doce (12) horas, siempre y cuando esté disponible.
    4.2 En caso de cremación, se prestará el servicio sin costo adicional.
    5. ÁREA DE PRESTACIÓN DE SERVICIOS:
    El servicio se prestará solo dentro del área metropolitana de la ciudad de Medellín y en área urbana de los siguientes Municipios: Santuario, Sonsón, La Ceja, La Unión, Marinilla, Rionegro, Guarne, El Retiro y El Carmen de Viboral, en caso de requerirse un servicio en un municipio diferente se deberá pagar por servicios adicionales en caso de que existan.
    6. VIGENCIA:
    La vigencia de la presente afiliación es de un año prorrogable por las partes, previos pagos periódicos, los cuales serán reajustados el 01 de Enero de cada año.
    7. CONDICIONES DE REHABILITACIÓN:
    Si el titular de la presente se atrasa en los pagos más de sesenta (60) días, quedará inhabilitada la póliza, la cual se habilitará nuevamente después de ocho (8) días de ponerse a paz y salvo con sus compromisos; si la póliza se encuentra inhabilitada, el presente compromiso no tiene validez por incumplimiento del titular.
    8. CONDICIONES ESPECIALES:
    8.1 Si al momento de la firma del compromiso, el titular o cualquiera de los beneficiarios es mayor de (65 a 70) años tendrán que pagar el valor del destino final y misa de Exequias, y si es mayor de (70) años, será reconocido el cincuenta por ciento (50%) del valor de la póliza.
    8.2 La funeraria solo se compromete con la prestación de servicios funerarios y en ningún caso hará devolución de dinero.
    8.3 Si la persona fallecida se encuentra afiliada en dos contratos o más de esta Funeraria, se le prestará el servicio con uno de los contratos, el que escoja de acuerdo al plan adquirido, por los otros no se hace devolución de dinero.
    8.4 Si en el momento de prestar el servicio exequial se comprueba que los datos consignados en el contrato no concuerdan con la realidad, en cuanto a edad, nombres, apellidos, salud u otros que se comprueben en ese momento como falsedad, se perderá el derecho a reclamar y se exonera de responsabilidad a la funeraria.
    8.5 Si en el momento de prestar el servicio exequial por cualquier motivo no utiliza uno de los servicios aquí estipulados, no se dará dinero en cambio, ni se admitirá canjes, los dineros recibidos por concepto de mensualidades en ningún momento serán devueltos.
    8.6 Si el titular o cualquiera de los beneficiarios fallece, podrá ser reemplazado después de un año de suscrita la póliza.
    """, align='L')

    # Guardar PDF
    pdf_path = rf"C:\Users\Ascension\Desktop\proyectoFuneraria\polizas\{socio}.pdf"
    pdf.output(pdf_path)
    print(f"PDF generado correctamente: {pdf_path}")
    

