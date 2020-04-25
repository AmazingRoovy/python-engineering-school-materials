## Если используем объект bot, значит его надо как-то объявить и инициализировать до этого
## для этого подключим модуль 'telebot'
import telebot

## Здесь описать метод-конструктор для своего бота. Тут может быть ID, token, какие-либо параметры бота
## Подробнее - в документации по API!
bot = telebot.Telebot()


def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message("Привет, пользователь, если хочешь узнать, что я умею, напиши: /help ")
    elif message.text == "/help":
        bot.send_message("Напиши привет!")
    else:
        bot.send_message("Я тебя не понимаю. Напиши /help.")


def get_name(message):
    name = message.text
    bot.send_message('Приятно познакомиться, ' + name + '!')


def start(message):
    ## Проверяем поступил ли текст

    if message.text:
        if message.text == '/reg':
            bot.send_message("Как тебя зовут?")
        else:
            get_name(message)

        print('Введи любые три числа:')
        ## list как название - нельзя использовать, это одна из специальных инструкции языка. Вместо этого назовем список list_a
        ## Кроме того, правильно создать список с введенных с клавиатуры значений, лучше так:

        list_a = [int(x) for x in input().split()]

        ## Для сравнения, Ваша конструкция:
        # list = input('number_1, number_2, number_3')
        print(list_a.sort())  ## sort() - метод, а не атрибут, так что вызываем с круглыми скобками!
        print('Я отсортировал твою строку и если хочешь, могу добавить туда любой элемент, напиши /list2')
        if message.text == '/list2':
            ## Не забудем преобразовать число введенное с клавиатуры в численное значение!
            ## Обратим внимание - функция input() ожидает ввода с клавиатуры в КОНСОЛЕ, не в самом мессенджере!
            x = int(input())
            print(list_a.append(x))
            print('Я могу сказать сколько букв в твоей строчке: ', end='')
            print(len(list_a))


bot.polling()