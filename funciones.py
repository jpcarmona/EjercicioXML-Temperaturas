def municipio_existe(municipio,arbol):
	"""Dado un municipio(str)
	y el arbol(lxml.etree)
	de 'sevilla.xml',
	verifica si existe(bool)"""
	municipios=arbol.xpath('//municipio/text()')

	for muni in municipios:
		if muni.upper()==municipio.upper():
			return True
		else:
			return False

def cod_municipio(municipio,arbol):
	"""Dado un municipio(str)
	y el arbol(lxml.etree)
	de 'sevilla.xml',
	devuelve codigo(str)"""
	cod=arbol.xpath('//municipio[contains(text(),municipio)]/@value')
	codigo=cod[0][-5:]
	return codigo

def get_url(codigo):
	"""Dado un codigo(str),
	devuelve url(str)"""
	url="http://www.aemet.es/xml/municipios/localidad_"+codigo+".xml"
	return url

def get_temp(url):
	"""Dado un url(str),
	devuelve url(str)"""
	dia_hoy=time.strftime("%Y-%m-%d")
	arbol=etree.parse(url)
	tempmax=arbol.xpath('/root/prediccion/dia[@fecha=dia_hoy]/temperatura/maxima/text()')
	tempmin=arbol.xpath('/root/prediccion/dia[@fecha=dia_hoy]/temperatura/minima/text()')
	return tempmax,tempmin


