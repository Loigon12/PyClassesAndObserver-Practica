from observer_practice.suscriptores import SuscriptorEmail

ana = SuscriptorEmail("Ana")
ana.actualizar("Primera noticia")
print(ana.mensajes)
print(ana)