from allauth.account.models import EmailAddress
from allauth.account.utils import send_email_confirmation
from django.contrib.auth import get_user_model
from django.core.mail import send_mail  # Import send_mail
from rest_framework import status
from rest_framework.response import Response

User = get_user_model()

def send_otp_via_email(request,otp):
    user = request.user

    # Update or create the user's email address (using Allauth)
    email, created = EmailAddress.objects.get_or_create(user=user, email=user.email)
    if not email.verified:
        send_email_confirmation(request, email)

    # Send the OTP
    subject = 'Your OTP Code'
    body = f'Your OTP is: {otp}'
    send_mail(subject, body, 'your_email@gmail.com', [user.email])
