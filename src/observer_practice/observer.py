from typing import Protocol


class Observador(Protocol):
    def notificar(self, mensaje):
        for observador in self.observadores:
            observador.actualizar(mensaje)

    def publicar(self, mensaje):
        self.ultimo_mensaje = mensaje
        self.notificar(mensaje)
        
    
    