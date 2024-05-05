from django.core.mail import send_mail
from django.conf import settings

from volv_dashboard_backend.log_conf import Logger
LOGGER = Logger.get_logger(__name__)


def send_reset_email(user_email, reset_link):
    subject = 'Password Reset Request | Volv Dashboard'
    message = f'Hi,\n\nPlease click the following link to reset your password:\n\n{reset_link}\n\nIf you did not request this, please ignore this email.'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['dipakrathod258@gmail.com']
    LOGGER.info(f"from_email: {from_email} recipient_list: {recipient_list}")
    send_mail(subject, message, from_email, recipient_list, fail_silently=False)


import secrets
import string

def generate_token(length=20):
    alphabet = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(alphabet) for _ in range(length))
    return token
