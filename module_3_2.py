def is_correct (email):
    return 0 < email.index("@") < len(email) - 4 and email.count("@") == 1

def send_email(message, recipient, sender  = "university.help@gmail.com"):
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
    elif not(recipient.endswith(".com") or recipient.endswith(".net") or recipient.endswith(".ru")
         and sender.endswith(".com") or recipient.endswith(".net") or sender.endswith(".ru")):
             print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    elif not (is_correct(sender) and is_correct(recipient)):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    else:
        if sender == "university.help@gmail.com":
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        else:
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru',
                   sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
