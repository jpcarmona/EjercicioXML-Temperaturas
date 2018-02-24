import time
from lxml import etree
from funciones import municipio_existe,cod_municipio,get_url,get_temp

arbolsevilla=etree.parse("sevilla.xml")
dia_hoy=time.strftime("%Y-%m-%d")

print("TEMPERATURAS EN SEVILLA {}\n".format(dia_hoy))

municipio=input("Introduce un municipio de Sevilla (\"0\" para salir): ")

while municipio!="0":
	if not municipio_existe(municipio,arbolsevilla):
		print("Este municipio no existe en Sevilla")
	else:
		municipio=municipio_existe(municipio,arbolsevilla)
		arboltemp=etree.parse(get_url(cod_municipio(municipio,arbolsevilla)))
		temperaturas=get_temp(arboltemp,dia_hoy)
		print("La temperatura máxima en {} es de {}º".format(temperaturas[0],municipio))
		print("La temperatura mínima en {} es de {}º".format(temperaturas[1],municipio))
	municipio=input("Introduce un municipio de Sevilla (\"0\" para salir): ")