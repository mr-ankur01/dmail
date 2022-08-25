from django.core.mail import send_mail



def send_forget(email,token):
    
    subject = 'Your forget password link'
    message = f'hi , click on the link to forget your password http://127.0.0.1:8000/change-password/{token}/'
    email_from = 'testingfor2002@gmail.com'
    to = [email]
    send_mail(subject,message,email_from,to)
    return True