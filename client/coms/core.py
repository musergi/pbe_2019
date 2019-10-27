#Librerias que tengo que importar
#http get requests
#httplib / urllib (estándares de python) / requests
import urllib.request

class CommunicationManager:
    """
    La clase lo que hace es encapsular (contenedor) funciones de comunicaciones
    Función: Le paso una URL me conecto a una URL y devuelvo los datos 
    (paquetes http y extraer los datos) de esa URL 
    (Acceder a una web es algo que se hace muchas veces seguro que python tienen una libreria para eso)
    """
    def get(self, url):
        response = urllib.request.urlopen(url)
        data = response.read()
        return data.decode("utf-8")

if __name__ == "__main__":
    cm = CommunicationManager()
    data = cm.get("http://ardi.cat")
    print(data)