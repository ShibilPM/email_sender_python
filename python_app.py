from dotenv import load_dotenv
from email.message import EmailMessage
import os
import ssl
import smtplib

load_dotenv()

email_sender = 'shibilpm3232@gmail.com'
email_password = os.getenv('EMAIL_PASSWORD')

email_receiver = 'shibils2j3232@gmail.com'

subject = "Don't forget to learn"

body = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Donec eget consectetur arcu, ut gravida dui. Donec tempus magna eget mi dictum, 
non mollis risus hendrerit. Nam in diam scelerisque, laoreet lorem sit amet, 
blandit nibh. In dictum dui id tortor vehicula gravida. Phasellus in eros faucibus, 
pellentesque libero nec, sodales lectus. In eget pretium orci. Maecenas sit amet accumsan nulla. 
Aliquam quis ex dignissim, efficitur sem cursus, dignissim metus. 
Morbi lobortis tortor eu turpis volutpat, 
ac faucibus nibh semper. 
Nullam diam ex, placerat sit amet massa eu, fringilla finibus tellus.
Aenean non ex malesuada, aliquet metus sit amet, auctor erat. 
Proin eu mi eget odio egestas accumsan sed vel nibh. 
Vestibulum accumsan metus turpis, at posuere risus dictum ac. 
Vivamus placerat, eros eu commodo tincidunt, enim tellus laoreet quam, 
sed mattis nulla enim eget velit. Phasellus aliquet massa vel ullamcorper condimentum. 
Sed in pulvinar justo.
'''

em = EmailMessage()
em['From'] = email_sender
em["To"] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())






