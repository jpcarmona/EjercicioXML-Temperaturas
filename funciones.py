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