from django.core.mail import send_mail



def send_forget(email,token):
    try:
        subject = 'Your forget password link'
        message = f'<strong>hi , click on the link to forget your password</strong> :<a target="_blank" href="http://127.0.0.1:8000/change-password/{token}/">forgot link<a>'
        email_from = 'disposablemail469@gmail.com'
        to = [email]
        send_mail(subject=subject,from_email=email_from,recipient_list=to,html_message=message,message=None)
        print('mail sent')
    except Exception as e:
        print('mail:',e)
    return True