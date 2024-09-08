import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

def send_email():
    # Configurações do servidor de e-mail local
    smtp_server = "10.3.81.100"  # ou o IP do seu servidor SMTP local
    smtp_port = 25  # Porta padrão para SMTP

    # Configurações do e-mail
    remetente = "vinicius.mendes@valemobi.com.br"
    destinatario = "destinatario@provedor.com"
    
    # Obter a data atual e formatar
    data_hoje = datetime.now().strftime("%d/%m/%Y")
    assunto = f"CHECK-LIST FECHAMENTO DO DIA {data_hoje}"

    corpo = "Aqui vai o corpo do e-mail."

    # Criação da mensagem
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = assunto

    # Anexar corpo do e-mail
    msg.attach(MIMEText(corpo, 'plain'))

    # Envio do e-mail
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.sendmail(remetente, destinatario, msg.as_string())
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Falha ao enviar e-mail: {e}")

# Chama a função para enviar o e-mail
send_email()
