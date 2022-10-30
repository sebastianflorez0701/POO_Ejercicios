"""
Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre,
telefono y email. Además deberá mostrar un menú con las siguientes opciones.

1) Añadir contacto
2) Lista de contactos
3) Buscar Contacto y mostrar nombre del contacto, telefono y email
4) Editar Contacto
5) Cerrar Agenda

"""
class Agenda:
    
    lista_contactos = []
    
    def __init__(self,nombre_agenda):
        self.nombre_agenda = nombre_agenda
    
    def _añadir_contacto(cls,nombre,telefono=None,email=None):
        cls.lista_contactos.append(Contacto(nombre,telefono,email))
    
    def _lista_contacto(cls):
        for list_contacto in cls.lista_contactos:
            print(list_contacto)
    def __str__(self):
        return f'Agenda {self.nombre_agenda}'
    
            
        
class Contacto:
    """
    Clase encargada de crear un concato para la agenda (Clase agenda).
    """
    _cantidad_contactos = 0
    
    def __new__(cls,nombre,telefono,email):
        """
        Invocacion del metodo especial y estatico __new__ para agregar cantidad de contactos
        y numero de contacto.
        """
        cls._cantidad_contactos += 1
        instancia = super(Contacto,cls).__new__(cls)
        instancia.__init__(nombre,telefono,email)
        instancia.num_contacto = cls._cantidad_contactos
        return instancia
        
    def __init__(self,nombre,telefono,email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    @property
    def get_nombre(self):
        return self.nombre
    
    @property
    def get_telefono(self):
        return self.telefono
    
    @property
    def get_email(self):
        return self.email
    
    def __str__(self):
        return f'Contacto {self.nombre}, {self.telefono}, {self.email}'
    

if __name__ == '__main__':
    agenda = Agenda("Historias de Sebas")
    print(agenda)
    agenda._añadir_contacto("sebastian","3006023827")
    agenda._lista_contacto()