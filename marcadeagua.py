from fpdf import FPDF
import os

def pdf_colilla(fecha_actual, socio, valor_total, fecha_desde, fecha_hasta, recibio, nombre_titular, cedula_titular):
    # Crear instancia de FPDF
    pdf = FPDF(orientation='P', unit='mm', format=(80, 140))
    pdf.add_page()

    # Configurar fuente y tamaño
    pdf.set_font('Arial', 'B', 9)
    pdf.set_auto_page_break(auto=True, margin=0)
    centro_x = pdf.w
    print(centro_x)
    pdf.image('ico.png', x=22, y=2, w=35)
    pdf.image('sellomarca.jpg', x=13, y=45, w=55)

    # Agregar contenido al PDF
    pdf.set_y(25)
    pdf.cell(60, 5, txt="FUNERARIA LA ASCENSIÓN", align='C')
    pdf.cell(60 , 5, txt="NIT: 39.191.604", ln=True, align='C')
    pdf.cell(60, 5, txt="COLILLA DE PAGO SERVICIO PROEXEQUIAL", ln=True, align='C')
    pdf.cell(60, 5, txt="__________________________________________________", ln=True, align='C')
    pdf.set_font('Arial', '', 9)
    pdf.cell(60, 5, txt="FECHA: " + fecha_actual, ln=True, align='C')
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(60, 5, txt="SOCIO: " + str(socio), ln=True, align='C')
    pdf.set_font('Arial', '', 9)
    pdf.cell(60, 5, txt="NOMBRE TITULAR: " + nombre_titular, ln=True, align='C')
    pdf.cell(60, 5, txt="CÉDULA TITULAR: " + str(cedula_titular), ln=True, align='C')
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(60, 5, txt="VALOR: " + str(valor_total), ln=True, align='C')
    pdf.set_font('Arial', '', 9)
    pdf.cell(60, 5, txt="DESDE: " + fecha_desde, ln=True, align='C')
    pdf.cell(60, 5, txt="HASTA: " + fecha_hasta, ln=True, align='C')
    pdf.cell(60, 5, txt="RECIBIO: " + str(recibio), ln=True, align='C')
    pdf.cell(60, 5, txt="", ln=True, align='C')  # Espacio en blanco
    pdf.cell(60, 5, txt="FIRMA: _______________________________", ln=True, align='C')

    # Guardar el PDF en un archivo
    nombre_pdf = str(socio) + '.pdf'
    colillas_path = r"C:\Users\Jose\OneDrive - UCO\Desktop\proyecto funeraria\colillas"
    pdf_path = os.path.join(colillas_path, nombre_pdf)
    pdf.output(pdf_path)

# Llamar a la función con datos de ejemplo
pdf_colilla("2024-02-25", 12345678, 500.00, "2024-02-01", "2024-02-28", "Juan Perez", "John Doe", "123456789")
