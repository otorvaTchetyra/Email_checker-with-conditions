sent_emails = []

def send_email(message, recipient, *, sender=None):
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return
    if sender is None:
        sender = "university.help@gmail.com"
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}")
    elif sender == "urban.teacher@mail.uk":
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}")
    
    # Логируем отправленное письмо
    sent_emails.append({
        'sender': sender,
        'recipient': recipient,
        'message': message
    })

# Примеры вызовов функции
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

# Выводим лог отправленных писем
print("\nЛог отправленных писем:")
for email in sent_emails:
    print(email)