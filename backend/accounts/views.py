from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer
from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema

#django_rest_passwordreset
from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse

from django_rest_passwordreset.signals import reset_password_token_created

@swagger_auto_schema(method='delete')
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def user_delete(request):
    request.user.delete()
    return HttpResponse(status=200)

## django rest passowrreset
@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    """
    Handles password reset tokens
    When a token is created, an e-mail needs to be sent to the user
    :param sender: View Class that sent the signal
    :param instance: View Instance that sent the signal
    :param reset_password_token: Token Model Object
    :param args:
    :param kwargs:
    :return:
    """
    # send an e-mail to the user
    context = {
        'current_user': reset_password_token.user,
        'username': reset_password_token.user.username,
        'email': reset_password_token.user.email,
        'reset_password_url': reset_password_token.key,
    }

    # render email text
    email_html_message = render_to_string('accounts/user_reset_password.html', context)
    email_plaintext_message = render_to_string('accounts/user_reset_password.txt', context)

    msg = EmailMultiAlternatives(
        # title:
        "Password Reset for <찾을 고양? 찾을개!>",
        # message:
        email_plaintext_message,
        # from:
        's03p23a204@gmail.com',
        # to:
        [reset_password_token.user.email]
    )
    msg.attach_alternative(email_html_message, "text/html")
    msg.send()