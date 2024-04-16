# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import send_mail

class SendEmailAPI(APIView):
    def post(self, request):
        subject = request.data.get('subject')
        message = request.data.get('message')
        email_from = request.data.get('email_from')
        recipient_list = request.data.get('recipient_list')

        send_mail(subject, message, email_from, recipient_list)
        return Response({"message": "Email sent successfully."})