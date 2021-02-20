from setuptools import setup


setup(
    
    name = "calculosbasicosmatematicos",
    version= "1.0",
    description = "Paquete para cálculos básicos, suma, resta, multiplicación",
    author = "Eduardo",
    author_mail = "esanchezlugo91@gmail.com",
    package =["src/modulos/modulosMatematicos", "modulosMatematicos.calculosBasicos"]
        
)

# python setup.py sdist -> crear un archivo distribuido
# pip3 install calculosbasicosmatematicos-1.0.tar.gz -> enter para instalar el paquete.