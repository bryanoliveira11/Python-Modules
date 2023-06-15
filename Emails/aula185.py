import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import getenv
from pathlib import Path
from string import Template

from dotenv import load_dotenv

load_dotenv()

# remetente e destinatário
remetente = getenv('EMAIL', '')
destinatario = remetente

# SMPT
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_user = getenv('EMAIL', '')
smtp_password = getenv('SENHA', '')


# mensagem de texto
ARQUIVO_HTML = Path(__file__).parent / 'aula185.html'

with open(ARQUIVO_HTML, 'r', encoding='utf-8') as arquivo:
    texto_arquivo = arquivo.read()
    template = Template(texto_arquivo)
    texto_email = template.substitute(nome="Teste")


# transformar mensagem em MIMEMultipart

mime_multipart = MIMEMultipart()
mime_multipart['from'] = remetente
mime_multipart['to'] = destinatario
mime_multipart['subject'] = "Assunto email aqui"

corpo_email = MIMEText(texto_email, 'html', 'utf-8')
mime_multipart.attach(corpo_email)

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(smtp_user, smtp_password)
    server.send_message(mime_multipart)
    print('Email Enviado !')
