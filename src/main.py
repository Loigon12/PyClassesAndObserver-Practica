from canal import CanalNoticias
from suscriptor_email import SuscriptorEmail
from suscriptor_sms import SuscriptorSMS

# Crear un canal de noticias
canal = CanalNoticias()

# Crear suscriptores
suscriptor_email = SuscriptorEmail("usuario@example.com")
suscriptor_sms = SuscriptorSMS("+1234567890")

# Suscribir ambos al canal xd
canal.suscribir(suscriptor_email)
canal.suscribir(suscriptor_sms)

# Publicar un mensaje
canal.publicar("¡Última noticia! Evento importante ocurrido hoy.")

# Imprimir los mensajes recibidos
print("\n--- Mensajes Recibidos ---")
print(f"Email: {suscriptor_email.mensaje_recibido}")
print(f"SMS: {suscriptor_sms.mensaje_recibido}")
