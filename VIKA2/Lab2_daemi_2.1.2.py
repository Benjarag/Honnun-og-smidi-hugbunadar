class MessagingSender (ABC) :
    @abstractmethod
    def send_message(self, message_from: str, message_to: str, message_subject: str, message_body: str):
        pass


class EmailSender (MessagingSender):
    def send_message(self, message_from: str, message_to: str, message_subject: str, message_body: str):
        msg = EmailMessage()
        msg.set_content(message_body)

        msg['Subject'] = f'The contents of {message_subject}'
        msg['From'] = message_from
        msg['To'] = message_to
        s = smtplib.SMTP('localhost')
        s.send_message(msg)
        s.quit()

class SmsSender(MessagingSender):
    def send_message(self, message_from: str, message_to: str, message_subject: str, message_body: str):
        account_sid = os. environ[ 'TWILIO_ACCOUNT_SID']
        auth_token = os. environ[ 'TWILIO_AUTH_TOKEN ']
        client = Client (account_sid, auth_token)
                
        client.messages.create(
            body=message_body,
            from_=message_from,
            to=message_to
        )


class AppNotificationSender(MessagingSender):
    def send_message(self, message_from: str, message_to: str, message_subject: str, message_body: str):
        message = messaging.Message(
            notification=messaging.Notification(
                title=message_subject, 
                body=message_body,
            ))