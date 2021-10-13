import random

from django.core.mail import send_mail, BadHeaderError

def generate_code(length=23):
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    digits = '1234567890'
    letters_upper = letters.upper()
    blank = list(letters + digits + letters_upper)
    random.shuffle(blank)
    code = ''.join([random.choice(blank) for x in range(length)])
    return code

def send_email(email, code):

    subject = 'Код подтверждения Django Academy'
    message = 'Введите этот код подтверждения email: {}'.format(code)
    try:
        send_mail(subject, message, 'emailsenddjango@gmail.com', [email])
        return True
    except BadHeaderError:
        return False
