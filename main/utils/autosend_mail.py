from django.core import mail
from config import settings


class DistributionMessages:

    def __init__(self, message_title, message_body, message_user_name, message_email):
        self.message_title = message_title
        self.message_body = message_body
        self.message_user_name = message_user_name
        self.message_email = message_email

    def send_email_message(self):
        connection = mail.get_connection()
        connection.open()

        text_message = f'Здравствуйте, {self.message_user_name}!\n' + self.message_body
        message_1 = mail.EmailMessage(
            self.message_title,
            text_message,
            None,
            [self.message_email],
        )
        code_result = message_1.send()
        connection.close()
        return code_result
