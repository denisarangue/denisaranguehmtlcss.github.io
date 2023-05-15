import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# Obtén los valores de los campos del formulario
nombre = request.POST.get('nombre', '')
empresa = request.POST.get('empresa', '')
email = request.POST.get('email', '')
mensaje = request.POST.get('mensaje', '')

# Construye el cuerpo del correo electrónico
html_content = f'<p><strong>Nombre:</strong> {nombre}</p>' \
               f'<p><strong>Empresa:</strong> {empresa}</p>' \
               f'<p><strong>Email:</strong> {email}</p>' \
               f'<p><strong>Mensaje:</strong></p>' \
               f'<p>{mensaje}</p>'

# Crea el mensaje de correo electrónico
message = Mail(
    from_email=email,
    to_emails='denisarangue18@gmail.com',
    subject='Formulario de contacto',
    html_content=html_content)

try:
    # Crea una instancia del cliente SendGrid con tu clave API
    sg = SendGridAPIClient(os.environ.get('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'))
    # Envía el correo electrónico usando el cliente SendGrid
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
