from django.http import JsonResponse

def get_email_data(request):
    email_data = {
        'subject': 'creo que ya esta',
        'message': 'pene',
        'email_from': 'colladodeveloper123@gmail.com',
        'recipient_list': [
            'markogamarra94@gmail.com',
            'oscarvasquezroncal@gmail.com',
            'qryjeimpleis@gmail.com',
            'leninalvaradob25@gmail.com',
            'anivalmoraleshuanca@gmail.com'
        ]
    }
    return JsonResponse(email_data)
