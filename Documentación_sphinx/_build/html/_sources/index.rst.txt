.. Generador Codigo documentation master file, created by
   sphinx-quickstart on Thu Nov  9 17:47:29 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Generador Codigo's documentation!
============================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

GuardarCodigo
==============

.. py:class:: GuardarCodigo

   Clase base para guardar códigos generados como imágenes.

   .. py:method:: guardar_imagen(img, name, carpeta, extension)

      Guarda una imagen en una carpeta específica con un nombre y extensión dados.

      :param img: La imagen a guardar.
      :type img: PIL.Image
      :param name: El nombre del archivo de imagen.
      :type name: str
      :param carpeta: La carpeta donde se guardará la imagen.
      :type carpeta: str
      :param extension: La extensión del archivo de imagen.
      :type extension: str

      :raises OSError: Si hay un error al guardar la imagen.

GeneradorDominioYQR
====================

.. py:class:: GeneradorDominioYQR

   Clase para generar dominios web a partir de nombres dados y códigos QR a partir de esos dominios.

   .. py:method:: __init__(nombre_sitio_web)

      Inicializa una instancia del generador de códigos QR.

      :param nombre_sitio_web: El nombre del sitio web para el que se generará el dominio.
      :type nombre_sitio_web: str

   .. py:method:: generar_dominio()

      Genera un URL de dominio a partir del nombre del sitio web.

      :returns: El URL de dominio generado.
      :rtype: str

   .. py:method:: generar_qr(carpeta_guardado='QRs', extension_guardado='png', tamano_cuadrado=10, tamano_borde=4)

      Genera un código QR a partir del dominio y lo guarda como una imagen.

      :param carpeta_guardado: La carpeta donde se guardará la imagen del código QR.
      :type carpeta_guardado: str
      :param extension_guardado: La extensión del archivo de imagen.
      :type extension_guardado: str
      :param tamano_cuadrado: El número de los cuadros en el código QR.
      :type tamano_cuadrado: int
      :param tamano_borde: El tamaño del borde del código QR.
      :type tamano_borde: int

      :raises ValueError: Si se produce un error en la generación del código QR.

GeneradorCodigosDeBarras
=========================

.. py:class:: GeneradorCodigosDeBarras

   Clase para generar códigos de barras EAN-13.

   .. py:method:: generar_codigo_de_barras(producto, codigo, carpeta_guardado='codigos_barras', extension_guardado='png')

      Genera un código de barras EAN-13 y lo guarda como una imagen.

      :param producto: El nombre del producto asociado al código de barras.
      :type producto: str
      :param codigo: El código de barras de 12 dígitos o una cadena vacía para generar uno aleatorio.
      :type codigo: str
      :param carpeta_guardado: La carpeta donde se guardará la imagen del código de barras.
      :type carpeta_guardado: str
      :param extension_guardado: La extensión del archivo de imagen.
      :type extension_guardado: str

      :raises ValueError: Si el código de barras no tiene 12 dígitos.
      :raises ValueError: Si se produce un error en la generación del código de barras.


