from lxml import etree
import time
from funciones import municipio_existe,cod_municipio,get_url

arbolsevilla=etree.parse("sevilla.xml")

if not municipio_existe(municipio,arbol):
	print("Error")
else:
	print(municipio_existe(municipio,arbol))
