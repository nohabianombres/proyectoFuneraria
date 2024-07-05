import win32api
import win32print
from fpdf import FPDF
import os, sys



#def print_file(file):
#    win32api.ShellExecute(0,'print', file,win32print.GetDefaultPrinter(),'.',0)

def resolver_ruta(ruta_relativa):

    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, ruta_relativa)
    return os.path.join(os.path.abspath('.'), ruta_relativa)


def pdf_colilla(fecha_actual, socio, valor_total, fecha_desde, fecha_hasta, recibio, nombre_titular, cedula_titular):

    def generar_pdf_con_imagen_sello(incluir_sello):
        pdf = FPDF(orientation='P', unit='mm', format=(80, 140))
        pdf.add_page()

        # Configurar fuente y tamaño
        pdf.set_font('Arial', 'B', 9)
        pdf.set_auto_page_break(auto=True, margin=0)
        centro_x = pdf.w
        print(centro_x)
        print('ejemplo')
        pdf.image(resolver_ruta('ico2.png'), x=22, y=2, w=35)

        if incluir_sello:
            # Añadir la imagen sellomarca
            pdf.image(resolver_ruta('sellomarca.jpg'), x=13, y=45, w=55)

        # Agregar contenido al PDF
        pdf.set_y(25)
        pdf.cell(60, 5, txt="NIT: 39.191.604", ln=True, align='C')
        pdf.cell(60, 5, txt="310 471 8651 - 314 677 4935", ln=True, align='C')
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
        nombre_pdf = str(socio) + ('.pdf' if incluir_sello else '.pdf')
        colillas_path = r"C:\Users\Jose\OneDrive - UCO\Desktop\proyecto funeraria\colillas"
        pdf_path2 = os.path.join(colillas_path, nombre_pdf)
        pdf.output(pdf_path2)

        return pdf_path2

    # Generar y guardar el PDF sin la imagen sellomarca
    pdf_path_sin_sello = generar_pdf_con_imagen_sello(incluir_sello=False)

    # Imprimir el PDF guardado sin la imagen sellomarca
    print_file(pdf_path_sin_sello)

    # Generar y guardar el PDF con la imagen sellomarca
    pdf_path_con_sello = generar_pdf_con_imagen_sello(incluir_sello=True)

    # Imprimir el PDF guardado con la imagen sellomarca si es necesario
    print_file(pdf_path_con_sello)


def print_file(filepath):
    os.startfile(filepath, "print")

def pdf_factura_caja(ciudad, fecha_actual, usuario_encargado, nombre_comprador, documento_comprador, descripcion, valor_restante, valor_abonado, valor_total):

    pdf = FPDF(orientation='P', unit='mm', format=(80, 200))
    pdf.add_page()

    # Configurar fuente y tamaño
    pdf.set_font('Arial', 'B', 9)
    pdf.set_auto_page_break(auto=True, margin=0)
    descripciones = ", ".join(map(str, descripcion))
    # Agregar contenido al PDF
    pdf.image(resolver_ruta('ico2.png'), x=22, y=2, w=35)
    pdf.set_y(25)
    pdf.cell(60, 5, txt="NIT: 39.191.604", ln=True, align='C')
    pdf.cell(60, 5, txt="LA UNIÓN: 310 471 8651 - 314 677 4935", ln=True, align='C')
    pdf.cell(60, 5, txt="SONSÓN: 869 4654", ln=True, align='C')
    pdf.cell(60, 5, txt="ABEJORRAL: 864 7631", ln=True, align='C')
    pdf.cell(60, 5, txt="LA CEJA: 553 2434", ln=True, align='C')
    pdf.cell(60, 5, txt="NARIÑO: 310 546 2139", ln=True, align='C')
    pdf.cell(60, 5, txt="--------------------------------------------------", ln=True, align='C')
    pdf.cell(60, 5, txt="RECIBOS DE CAJA", ln=True, align='C')
    pdf.cell(60, 5, txt="--------------------------------------------------", ln=True, align='C')
    pdf.set_font('Arial', '', 9)
    pdf.cell(60, 5, txt="CIUDAD: " + str(ciudad), ln=True, align='C')
    pdf.cell(60, 5, txt="FECHA: " + fecha_actual.strftime("%d/%m/%Y"), ln=True, align='C')
    pdf.cell(60, 5, txt="NOMBRE COMPRADOR: \n " + str(nombre_comprador), ln=True, align='C')
    pdf.cell(60, 5, txt="DOCUMENTO COMPRADOR: " + str(documento_comprador), ln=True, align='C')
    pdf.cell(60, 5, txt="POR CONCEPTO DE: " + descripciones, ln=True, align='C')
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(60, 5, txt="VALOR TOTAL: " + str(valor_total), ln=True, align='C')
    pdf.cell(60, 5, txt="VALOR ABONADO: " + str(valor_abonado), ln=True, align='C')
    pdf.cell(60, 5, txt="RESTA: " + str(valor_restante), ln=True, align='C')
    pdf.set_font('Arial', '', 9)
    pdf.cell(60, 5, txt="RECIBIO: " + str(usuario_encargado), ln=True, align='C')
    pdf.cell(60, 5, txt="", ln=True, align='C')  # Espacio en blanco
    pdf.cell(60, 5, txt="FIRMA: _______________________________", ln=True, align='C')

    # Guardar el PDF en un archivo
    nombre_pdf = 'caja ' + nombre_comprador + '.pdf'
    adicioanles_path = r"C:\Users\Jose\OneDrive - UCO\Desktop\proyecto funeraria\facturas caja"
    pdf_path = os.path.join(adicioanles_path, nombre_pdf)
    pdf.output(pdf_path)

    print_file(pdf_path)