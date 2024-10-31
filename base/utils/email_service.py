from postmarker.core import PostmarkClient
from django.conf import settings

class EmailService:
    def __init__(self):
        self.client = PostmarkClient(server_token=settings.POSTMARK_API_TOKEN)

    def send_email(self, to, subject, text_body, html_body):
        try:
            response = self.client.emails.send(
                From=settings.DEFAULT_FROM_EMAIL,
                To=to,
                Subject=subject,
                TextBody=text_body,
                HtmlBody=html_body
            )
            return response
        except Exception as e:
            # Handle exception (logging or error handling)
            print(f"Email sending failed: {e}")
            return None