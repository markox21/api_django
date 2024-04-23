from django.core.mail import send_mail
from django.http import JsonResponse

def send_custom_email(request):
    subject = 'Recuperación de contraseña'
    message_html = """
        <html>
        <head>
            <style>
                .container {
                    text-align: center;
                    background-color: white;
                    padding: 20px;
                    border-radius: 10px;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                    width: 300px;
                    margin: 0 auto;
                }
                .title {
                    color: white;
                    background-color: #5bc0de;
                    padding: 10px;
                    border-radius: 10px 10px 0 0;
                }
                .message {
                    margin-top: 20px;
                    margin-bottom: 20px;
                }
                .button {
                    background-color: #5bc0de;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    padding: 10px 20px;
                    text-decoration: none;
                    cursor: pointer;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="title">Recuperación de contraseña</div>
                <div class="message">Contraseña:</div>
                <button class="button" onclick="alert('12345')">12345</button>
            </div>
        </body>
        </html>
    """

    # Envía el correo
    recipient_list = [
        'markogamarra94@gmail.com',
        'qryjeimpleis@gmail.com',
        'oscarvasquezroncal@gmail.com',
        'leninalvaradob25@gmail.com',
        'anivalmoraleshuanca@gmail.com'

    ]
    send_mail(
        subject,
        '',
        'colladodeveloper123@gmail.com',
        recipient_list,
        html_message=message_html
    )

    return JsonResponse({'success': True})
