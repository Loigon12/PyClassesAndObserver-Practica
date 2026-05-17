try:
    from canal import CanalNoticias
    from suscriptor import SuscriptorEmail, SuscriptorSMS
except ImportError:
    try:
        from canal_noticias import CanalNoticias
        from suscriptor_email import SuscriptorEmail
        from suscriptor_sms import SuscriptorSMS
    except ImportError:
        from CanalNoticias import CanalNoticias
        from SuscriptorEmail import SuscriptorEmail
        from SuscriptorSMS import SuscriptorSMS


def subscribe(canal, subscriber):
    if hasattr(canal, "suscribir"):
        canal.suscribir(subscriber)
    elif hasattr(canal, "subscribe"):
        canal.subscribe(subscriber)
    elif hasattr(canal, "agregar_suscriptor"):
        canal.agregar_suscriptor(subscriber)
    elif hasattr(canal, "attach"):
        canal.attach(subscriber)
    else:
        raise AttributeError("No se pudo suscribir al canal")


def publish(canal, mensaje):
    if hasattr(canal, "publicar"):
        canal.publicar(mensaje)
    elif hasattr(canal, "publish"):
        canal.publish(mensaje)
    elif hasattr(canal, "notificar"):
        canal.notificar(mensaje)
    elif hasattr(canal, "notify"):
        canal.notify(mensaje)
    else:
        raise AttributeError("No se pudo publicar el mensaje")


def print_received_messages(subscriber):
    if hasattr(subscriber, "mensajes"):
        print(f"{subscriber.__class__.__name__}: {subscriber.mensajes}")
    elif hasattr(subscriber, "mensajes_recibidos"):
        print(f"{subscriber.__class__.__name__}: {subscriber.mensajes_recibidos}")
    elif hasattr(subscriber, "received_messages"):
        print(f"{subscriber.__class__.__name__}: {subscriber.received_messages}")
    elif hasattr(subscriber, "messages"):
        print(f"{subscriber.__class__.__name__}: {subscriber.messages}")
    elif hasattr(subscriber, "get_mensajes"):
        print(f"{subscriber.__class__.__name__}: {subscriber.get_mensajes()}")
    elif hasattr(subscriber, "get_received_messages"):
        print(f"{subscriber.__class__.__name__}: {subscriber.get_received_messages()}")
    else:
        print(f"{subscriber.__class__.__name__}: {vars(subscriber)}")


def main():
    canal = CanalNoticias()
    email_subscriber = SuscriptorEmail("usuario@example.com")
    sms_subscriber = SuscriptorSMS("+34123456789")

    subscribe(canal, email_subscriber)
    subscribe(canal, sms_subscriber)

    mensaje = "Últimas noticias: se ha publicado un nuevo artículo."
    publish(canal, mensaje)

    print_received_messages(email_subscriber)
    print_received_messages(sms_subscriber)


if __name__ == "__main__":
    main()
