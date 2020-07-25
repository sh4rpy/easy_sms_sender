# Easy sms sender

### Что ты такое?

Учебный проект в Яндекс.Практикуме, позволяющий на начальном этапе понять, как работать с api.

Идея проста: запрашиваем статус пользователя VK и присылаем sms-уведомление при помощи api сервиса Twilio, если пользователь появился в сети, если не появился - ждем некоторое время и запрашиваем статус снова.

### Как запустить?

Склонируйте репозиторий:

```bash
git clone https://github.com/sh4rpy/easy_sms_sender.git
```

Установите зависимости:

```bash
pip install -r requirements.txt
```