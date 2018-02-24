from lxml import etree
import time
from funciones import municipio_existe,cod_municipio,get_url,get_temp

arbolsevilla=etree.parse("sevilla.xml")

print("TEMPERATURAS EN SEVILLA")

municipio=input("Introduce un municipio de Sevilla ("0" para salir): ")

while municipio!="0":
	if not municipio_existe(municipio,arbol):
		print("Este municipio no existe en Sevilla")
	else:
		municipio=municipio_existe(municipio,arbol)
		temperaturas=get_temp(get_url(cod_municipio(municipio,arbol)))
		print("La temperatura máxima en {} es de {}º".format(temperaturas[0],municipio))
		print("La temperatura mínima en {} es de {}º".format(temperaturas[1],municipio))
	municipio=input("Introduce un municipio de Sevilla ("0" para salir): ")