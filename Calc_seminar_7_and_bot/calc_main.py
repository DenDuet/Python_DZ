from config import TOKEN
import calculator as calcul
import logs

from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

numbers = []

# Определяем константы этапов разговора
CALC, NUMBER_COMPL, NUMBER, SIGN = range(4)

# функция обратного вызова точки входа в разговор
def start(update, _):

    logs.logger('Для выбора калькулятора рациональных чисел нажмите 1, для комплексных - 2: ', 'Ждем ответ.')
    update.message.reply_text('Для выбора калькулятора рациональных чисел нажмите 1, для комплексных - 2: ')
    return CALC

# Обрабатываем выбор калькулятора
def calc(update, _):
    text = update.message.text
    if text.isdigit():
        number = int(text)
        if number == 1:
            logs.logger('Введено значение: ', number)
            update.message.reply_text('Введите первое рациональное число: ')
            return NUMBER
        elif number == 2:
            logs.logger('Введено значение: ', number)
            update.message.reply_text('Введите первое комплексное число (через пробел): ')
            return NUMBER_COMPL
    logs.logger(f'Сделан неверный выбор - {text}. Повторный запрос. ', 'False')
    update.message.reply_text('Вы сделали неверный выбор. Выберите правильно: ')
    return CALC

# Обрабатываем ввод рационального числа
def number_f(update, _):
    global numbers
    text = update.message.text
    try:
        if text == '0' or float(text):
            numbers.append(float(text))
            if len(numbers) == 1:
                logs.logger(f'Введено {len(numbers)} рациональное число: ', 'Ok')
                update.message.reply_text('Введите второе рациональное число: ')
                return NUMBER
            else:
                logs.logger(f'Введено {len(numbers)} рациональное число: ', 'Ok')
                update.message.reply_text('Введите операцию над числами: ')
                calcul.init_ratio(numbers[0], numbers[1])
                return SIGN

    except ValueError as verr:
        logs.logger(f'Сделан неверный выбор. Повторный запрос. ', 'False')
        update.message.reply_text('Вы сделали неверный выбор. Выберите правильно: ')
    return NUMBER
        

def number_cpl(update, context):
    global numbers
    text = update.message.text
    arg = text.split(' ')

    try:
        if (arg[-2] == '0' and arg[-2] == '0') or (arg[-2] == '0' and float(arg[-1])) or (float(arg[-2]) and arg[-1] =='0') or float(arg[-2]) and float(arg[-1]):
            if len(numbers)<= 2: 
                numbers.append(float(arg[-2]))
                numbers.append(float(arg[-1]))
                logs.logger(f'Введено {len(numbers)} комплексное число: ', numbers)
                if len(numbers)< 4: 
                    update.message.reply_text('Введите второе комплексное число (через пробел): ')
                    return NUMBER_COMPL
            if len(numbers) == 4:
                logs.logger(f'Введено {len(numbers)} комплексное число: ', numbers)
                update.message.reply_text('Введите операцию над числами: ')
                calcul.init_compl(numbers[0], numbers[1], numbers[2], numbers[3])
                return SIGN            
    except ValueError as verr:
        logs.logger(f'Сделан неверный выбор. Повторный запрос. ','False')
        update.message.reply_text('Вы сделали неверный выбор. Выберите правильно: ')        
        return NUMBER_COMPL
        
def sign(update, _):
    global numbers
    text = update.message.text
    if text == '+':
        result = calcul.sum()
    elif text == '-':
        result = calcul.sub()
    elif text == '*':
        result = calcul.mult()
    elif text == '/':
        result = calcul.div()
        
    else:
        logs.logger(f'Нужно ввести знак операции ','False')
        update.message.reply_text('Вы сделали неверный выбор. Выберите правильно: ')        
        return SIGN
    data_log = str(calcul.x) + ' ' + text + ' ' + str(calcul.y)
    update.message.reply_text(f'Решение примера: {str(calcul.x)} {text} {str(calcul.y)} = {result}')
    logs.logger(data_log, result)
    numbers = []
    return ConversationHandler.END



# Обрабатываем команду /cancel если пользователь отменил разговор
def cancel(update, _):
   
    logs.logger(f'Процесс прервали...')
    # Заканчиваем разговор.
    return ConversationHandler.END


if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(TOKEN)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Определяем обработчик разговоров `ConversationHandler` 
    # с состояниями CALC, NUMBER, NUMBER_COMPL, SIGN
    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        entry_points=[CommandHandler('start', start)],
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            CALC: [MessageHandler(Filters.text, calc)],
            NUMBER: [MessageHandler(Filters.text, number_f)],
            NUMBER_COMPL: [MessageHandler(Filters.text, number_cpl)],
            SIGN: [MessageHandler(Filters.text, sign)],
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()