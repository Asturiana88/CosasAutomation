from xml.dom import minidom

class XmlReader():
    def __init__(self):
        self.documento = minidom.parse('/.config/configuracion.xml')

    def obtener_datos(self, dato): 
        item = self.documento.getElementsByTagName(dato)[0].firstChild.nodeValues)
        return item