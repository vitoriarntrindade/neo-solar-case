

class EmailService:

    def send(self, to_email: str, subject: str, body: str = "", cc: list = []):
        #Apenas uma classe para ilustrar o serviço de envio de email

        print(
            f"Enviando email para {to_email} \n Assunto: {subject} \n Conteúdo: {body} \n cc: {cc}"
        )
