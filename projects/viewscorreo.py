from django.http import JsonResponse

def get_email_data(request):
    email_data = {
        'subject': 'Recuperación de contraseña',
        'message': '12345',
        'email_from': 'colladodeveloper123@gmail.com',
        'recipient_list': [
            'markogamarra94@gmail.com',
        ]
    }
    return JsonResponse(email_data)
