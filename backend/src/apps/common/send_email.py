from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

def send_email(email):
    
    subject = "Prime Team Jamoasidan"

    email_bytes = urlsafe_base64_encode(force_bytes(email))
    message = "Siz shu emaildan ro'yxatdan o'tyapsiz\n\n"
    message += f"https://127.0.0.1:8000/activate/{email_bytes}"
    from_email = 'temurbekhamroyev41@gmail.com'

    send_mail(subject=subject, message=message,
                      from_email=from_email,  recipient_list=[email])
