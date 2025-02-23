from PIL import Image, ImageDraw, ImageFont


def crear_imagen(familia, nombre, dia, hora, ubicacion, cremacion):
    # Crear una nueva imagen en blanco
    ancho, alto = 792, 612  # Tamaño carta en píxeles (8.5 x 11 pulgadas a 96 ppp)
    imagen = Image.new('RGB', (ancho, alto), 'white')
    draw = ImageDraw.Draw(imagen)

    # Fuentes predeterminadas
    fuente35 = ImageFont.load_default()
    fuente17 = ImageFont.load_default()
    fuente40 = ImageFont.load_default()
    fuente20 = ImageFont.load_default()

    # Dibujar círculos
    draw.ellipse((638, 2745, 638 + 604, 2745 + 595), outline="black", width=2)
    draw.ellipse((136, 169, 136 + 571, 169 + 394), outline="black", width=2)

    # Texto
    draw.text((ancho / 2, alto / 3.5), f"Familia {familia}", fill="black", anchor="mm")
    draw.text((ancho / 2, alto / 3), "Agradecen la asistencia a las", fill="black", anchor="mm")
    draw.text((ancho / 2, alto / 2.8), "honras fúnebres de:", fill="black", anchor="mm")
    draw.text((ancho / 2, alto / 2.2), nombre, fill="black", anchor="mm", size=40)
    draw.text((ancho / 2, alto / 1.8), f"Día: {dia}", fill="black", anchor="mm")
    draw.text((ancho / 2, alto / 1.7), f"Hora: {hora}", fill="black", anchor="mm")
    draw.text((ancho / 2, alto / 1.6), f"Ubicación: {ubicacion}", fill="black", anchor="mm")
    draw.text((ancho / 2, alto / 1.5), f"Cremación: {cremacion}", fill="black", anchor="mm")

    # Guardar la imagen
    imagen.save('cartel_funebre.png')


# Parámetros de ejemplo
familia = "Lopez Valencia"
nombre = "JUAN GUILLERMO SEPULVEDA ARISTIZABAL"
dia = "03/03/2021"
hora = "11:00 am"
ubicacion = "La Unión"
cremacion = "Rionegro"

crear_imagen(familia, nombre, dia, hora, ubicacion, cremacion)
