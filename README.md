# Отправка емейлов из Django через SMTP Yandex

## Настройки settings.py

- RECIPIENT_ADDRESS = 'youremail@gmail.com' - емейл, на который вы хотите получать сообщения. Можно перечислить несколько в виде списка.
- EMAIL_HOST = 'smtp.yandex.ru'
- EMAIL_PORT = 465
- EMAIL_USE_SSL = True
- DEFAULT_FROM_EMAIL = 'youremail@yandex.ru' - емейл, который будет указан в поле "От кого".
- EMAIL_HOST_USER = 'youremail@yandex.ru' - ваш емейл на Яндексе. Как правило, идентичен предыдущему пункту. 
- EMAIL_HOST_PASSWORD = 'yourownpassword' - пароль **ПРИЛОЖЕНИЯ**, который нужно создать в настройках Яндекса заранее. **Это не пароль от вашего емейла!**
- EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

## Настройки аккаунта на Яндексе

![Screenshot (21)](https://user-images.githubusercontent.com/85797091/211198218-d1c2d452-6539-46dd-a927-583e3df190aa.png)

## Как отправить емейл из Django через Yandex

Информация, которую пользователь вводит в контактную форму, отправляется на емейл(ы) из списка **RECIPIENT_ADDRESS**:

![Screenshot (19)](https://user-images.githubusercontent.com/85797091/211197804-fb1cdd7f-7e31-4b88-bad5-1ffbc08cc6a8.png)

После отправки появляется уведомление о доставке:

![Screenshot (20)](https://user-images.githubusercontent.com/85797091/211198135-44086932-00c6-48c2-a5da-ab2f05967577.png)

Полученное сообщение в ящике **RECIPIENT_ADDRESS**:

![Screenshot (22)](https://user-images.githubusercontent.com/85797091/211198160-6ce8e645-0c65-426c-bb89-8fa4d1830a1a.png)
