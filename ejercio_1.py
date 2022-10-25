'''
Realizar un programa que conste de una clase llamada Alumno que tenga como atributos de instancia el nombre
y la nota del alumno. Definir los metodos para inicializar sus atributo, imprimirlos
y mostrar un mensaje con el resultado de la nota y si ha aprobado o no

NOTA: El alumno aprueba una nota si esta por encima de 3.0
NOTA: Los alumnos no pueden cambiar su nota ni eliminarla, al igual que sus nombres
'''
class Alumno:
    def __init__(self,nota,nombre):
        self._nota = nota
        self._nombre = nombre
    
    # Metodo mostrar resultado
    def resultado(self):
        if self._nota >= 3:
            print(f"Aprobo su nota")
        else:
            print(f"No aprobo su nota")

    # Definición de propiedades      
    def setnota(self,nota):
        raise Exception("No puede cambiar su nota")
    def getnota(self):
        return self._nota
    def delnota(self):
        raise Exception("No puede eliminar su nota")
        
    nota = property(getnota,setnota,delnota, "Obtención de notas")
    
    # Definición de propiedades mediante decoradores
    @property
    def nombre(self):
        """Obtencion de notas """
        return self._nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self._nombre = nombre
    
if __name__ == '__main__':
    alumno = Alumno(3,"Sebas")
    alumno.resultado()
    print(f' la nota que obtuvo fue de: {alumno.nota}')
    
    
    
        
    
        