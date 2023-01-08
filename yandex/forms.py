from django import forms
from django.conf import settings
from django.core.mail import send_mail

class ContactForm(forms.Form):
    Имя = forms.CharField(max_length=120)
    Email = forms.EmailField()
    Тема = forms.CharField(max_length=70)
    Сообщение = forms.CharField(widget=forms.Textarea)

    def get_message(self):
        cl_data = super().clean()
        name = cl_data.get('Имя').strip()
        from_email = cl_data.get('Email')
        subject = cl_data.get('Тема')
        msg = f'Пользователь {name} с email {from_email} сообщает:'
        msg += f'\n"{subject}"\n\n'
        msg += cl_data.get('Сообщение')

        return subject, msg

    def send(self):
        subject, msg = self.get_message()
        send_mail(
            subject=subject,
            message=msg,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.RECIPIENT_ADDRESS]
        )