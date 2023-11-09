# GuardarCodigo_Progra_bda4_Sara_Nahia

README: Explicación del Código

### Clase GuardarCodigo

La clase `GuardarCodigo` sirve como clase base para guardar códigos generados como imágenes. Incluye un método `guardar_imagen` para almacenar imágenes en una carpeta específica con un directorio, nombre y extensión dados.

### Clase GeneradorDominioYQR

La clase `GeneradorDominioYQR`, que hereda de `GuardarCodigo`, genera dominios web a partir de nombres dados y códigos QR a partir de esos dominios. Contiene los siguientes métodos:

- `init(nombre_sitio_web)`: Inicializa una instancia con el nombre del sitio web proporcionado.
- `generar_dominio()`: Genera un URL de dominio a partir del nombre del sitio web.
- `generar_qr(carpeta_guardado='QRs', extension_guardado='png', tamano_cuadrado=10, tamano_borde=4)`: Genera un código QR a partir del dominio y lo guarda como una imagen con las características introducidas.

### Clase GeneradorCodigosDeBarras

La clase `GeneradorCodigosDeBarras`, también heredando de `GuardarCodigo`, genera códigos de barras EAN-13. Contiene el siguiente método:

- `generar_codigo_de_barras(producto, codigo, carpeta_guardado='codigos_barras', extension_guardado='png')`: Genera un código de barras EAN-13 y lo guarda como una imagen. Toma un nombre de producto y un código de barras de 12 dígitos o genera uno aleatorio si no se proporciona.

### Ejemplo

Hay un ejemplo al final que demuestra cómo usar estas clases. Crea instancias de `GeneradorDominioYQR` y `GeneradorCodigosDeBarras`, genera un código QR para una tienda ficticia ("mi_tienda") y códigos de barras EAN-13 para dos productos ("Producto1" y "Producto2") con códigos predefinidos o generados aleatoriamente.

Para ejecutar el ejemplo, ejecuta el script, y creará códigos QR e imágenes de códigos de barras en las carpetas especificadas. Asegúrate de tener instaladas las bibliotecas necesarias (`qrcode`, `os`, `random`, `barcode`) antes de ejecutar el script.

Siéntete libre de adaptar e integrar estas clases en tus proyectos para generar códigos QR y códigos de barras.