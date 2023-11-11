import qrcode
import os
import random
from barcode import EAN13
from barcode.writer import ImageWriter 

class GuardarCodigo:
    """
    Clase base para guardar códigos generados como imágenes.
    """
    def guardar_imagen(self, img, name, carpeta, extension):
        """
        Guarda una imagen en una carpeta específica con un nombre y extensión dados.

        Args:
            img (PIL.Image): La imagen a guardar.
            name (str): El nombre del archivo de imagen.
            carpeta (str): La carpeta donde se guardará la imagen.
            extension (str): La extensión del archivo de imagen.

        Raises:
            OSError: Si hay un error al guardar la imagen.
        """
        try:
            if not os.path.exists(carpeta):
                os.makedirs(carpeta)
            img.save(str(carpeta)+'/'+str(name) + '.' + str(extension))
        except OSError as e:
            raise e

        
class GeneradorDominioYQR(GuardarCodigo):
    """
    Clase para generar dominios web a partir de nombres dados 
    y códigos QR a partir de esos dominios.
    """
    def __init__(self, nombre_sitio_web):
        """
        Inicializa una instancia del generador de códigos QR.

        Args:
            nombre_sitio_web (str): El nombre del sitio web para el que se generará el dominio.
        """
        self.nombre_sitio_web = nombre_sitio_web

    def generar_dominio(self):
        """
        Genera un URL de dominio a partir del nombre del sitio web.

        Returns:
            str: El URL de dominio generado.
        """
        return f"https://www.{self.nombre_sitio_web}.com"

    def generar_qr(self, carpeta_guardado = 'QRs', extension_guardado='png', tamano_cuadrado=10, tamano_borde=4):
        """
        Genera un código QR a partir del dominio y lo guarda como una imagen.

        Args:
            carpeta_guardado (str): La carpeta donde se guardará la imagen del código QR.
            extension_guardado (str): La extensión del archivo de imagen.
            tamano_cuadrado (int): El número de los cuadros en el código QR.
            tamano_borde (int): El tamaño del borde del código QR.
        
        Raises:
        ValueError: Si se produce un error en la generación del código QR.

        """
        dominio = self.generar_dominio()
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=tamano_cuadrado,
            border=tamano_borde,
        )
        qr.add_data(dominio)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        self.guardar_imagen(img, self.nombre_sitio_web, carpeta_guardado, extension_guardado)

class GeneradorCodigosDeBarras(GuardarCodigo):
    """
    Clase para generar códigos de barras EAN-13.
    """
    def generar_codigo_de_barras(self, producto, codigo, carpeta_guardado = 'codigos_barras', extension_guardado = 'png'):
        """
        Genera un código de barras EAN-13 y lo guarda como una imagen.

        Args:
            producto (str): El nombre del producto asociado al código de barras.
            codigo (str): El código de barras de 12 dígitos o una cadena vacía para generar uno aleatorio.
            carpeta_guardado (str): La carpeta donde se guardará la imagen del código de barras.
            extension_guardado (str): La extensión del archivo de imagen.
        
        Raises:
            ValueError: Si el código de barras no tiene 12 dígitos.
            ValueError: Si se produce un error en la generación del código de barras.

        """
        try:
            if not codigo.isdigit() or len(codigo) != 12:
                raise ValueError("El código de barras debe ser una cadena de 12 dígitos.")
            else:
                if codigo:
                    codigo_barras = EAN13(codigo, writer=ImageWriter())
                    img = codigo_barras.render()
                    self.guardar_imagen(img, producto, carpeta_guardado, extension_guardado)
                else:
                    codigo = ''.join(str(random.randint(0, 9)) for _ in range(12))
                    codigo_barras = EAN13(codigo, writer=ImageWriter())
                    img = codigo_barras.render()
                    self.guardar_imagen(img, producto, carpeta_guardado, extension_guardado)

        except ValueError as e:
            print(f"Error al generar código de barras para {producto}: {e}")

# Ejemplo de uso de las clases
if __name__ == "__main__":
    generador_dominio_qr = GeneradorDominioYQR("mi_tienda")
    generador_dominio_qr.generar_qr()

    generador_codigos_de_barras = GeneradorCodigosDeBarras()
    productos = {"Producto1": "123456789012", "Producto2": "987654321098"}
    
    for producto, codigo in productos.items():
        generador_codigos_de_barras.generar_codigo_de_barras(producto, codigo)
