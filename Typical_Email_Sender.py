from email.message import EmailMessage
# from password import password
import ssl
import smtplib

email_sender = 'yourmeil@gmail.com'
# password is in a difference file
email_password = password
your_name = input('What\'s your name: ')
email_receiver = input('Enter the email to which I send the message: ')
rekruter_name = input('Recruiter name (only name): ')

subject = "Recruitment"
body = f"""
Hello, {rekruter_name}

My name is {your_name} and I am a computer science student at 'university name'.
I heard about the opportunity during the Talent Days.
We spoke there and you mentioned that I should send an email.

I would like to ask if it would be possible for you to take a look at my CV and evaluate whether my skills and experience could be a fit for any of the currently available positions in your company.
Alternatively, I was wondering if there is a possibility of joining as an intern or for an internship to gain experience.

Best regards,
{your_name}
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
