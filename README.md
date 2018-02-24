# EjercicioXML-Temperaturas

Ejercicio XML usando XPATH para mostrar la temperatura actual de un municipio de Sevilla
usando Python3.

## Prerequisitos

Instalar la librería lxml:

	sudo apt install python-lxml

## Uso del programa

En el fichero tempsevilla.py indicaremos que usaremos por ejemplo el fichero sevilla.xml
para encontrar el codigo perteneciente a un municipio, en esta línea:

	arbolsevilla=etree.parse("sevilla.xml")

Al ejecutar el fichero tempsevilla.py nos pedirá que insertemos un municipio y nos devolverá
la temperatura máxima y mínima si dicho municipio existe en el fichero sevilla.xml.

	python3 tempsevilla.py

En el fichero funciones.py se encuentran las funciones necesarias para ejecutar el fichero 
tempsevilla.py .

## Ayudas

En este [enlace](https://github.com/josedom24/xpath) encontramos un manual básico sobre XPATH.