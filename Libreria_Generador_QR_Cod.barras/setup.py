from setuptools import setup, find_packages

setup(
    name='Generador_Codigos_QR_Cod.barras',
    version='0.3',
    packages=find_packages(),
    install_requires=[
        'qrcode',
        'Pillow',
        'python-barcode',
    ],
    entry_points={
        'console_scripts': [
            'trabajo_grupal.py=Generador_Codigos_QR_Cod.barras.barras.trabajo_grupal.py:main',
        ],
    },
    author='Sara & Nahia',
    author_email='sara.crego@alumni.mondragon.edu',
    description='Libreria diseñada para la generación de QRs para páginas web, especialmente e-commerce, donde además tiene la posibilidad de generar códigos de barras para cada uno de los distintos productos que están a la venta en la tienda.',
    long_description=open('../../GuardarCodigo_Progra_bda4_Sara_Nahia/README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/nahiaunceta/GuardarCodigo_Progra_bda4_Sara_Nahia.git',
    classifiers=[
        'Programming Language :: Python :: 3',
        # Otros clasificadores...
    ]

)
