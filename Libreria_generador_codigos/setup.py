from setuptools import setup, find_packages

setup(
    name='Libreria_generador_codigos',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'qrcode',
        'Pillow',
        'python-barcode',
    ],
    entry_points={
        'console_scripts': [
            'trabajo_grupal.py=Libreria_generador_codigos.trabajo_grupal.py:main',
        ],
    },
    author='Sara & Nahia',
    author_email='sara.crego@alumni.mondragon.edu',
    description='Libreria diseñada para la generación de QRs para paginas web, especialmente e-commerce, donde además tiene la posibilidad de generar códigos de barras para cada uno de los distintos productos que están a la venta en la tienda.',
    long_description=open('README.rst').read(),  # Ajusta el nombre del archivo según tu caso
    long_description_content_type='text/markdown',
    url='https://github.com/nahiaunceta/GuardarCodigo_Progra_bda4_Sara_Nahia.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        # Otros clasificadores...
    ],

)
