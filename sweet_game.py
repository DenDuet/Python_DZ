from config import TOKEN
import logging
from random import randint

from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
)

# Включим ведение журнала
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

sweets=0
sweet_per_time=0
first_move=0
mv_0 = 0
mv_1 = 0
sweet = 1
game_move = 0    
game_sw = [sweets, sweet_per_time, first_move, game_move, sweet, mv_0, mv_1]

logger = logging.getLogger(__name__)

# Определяем константы этапов разговора
SWEETS, SWEET_PER_TIME, GAME = range(3)

# функция обратного вызова точки входа в разговор
def start(update, _):

    # Начинаем разговор с вопроса
    update.message.reply_text(
        'Привет! Давай поиграем в игру с конфетами. Есть кучка конфет.'
        ' Из неё за один раз можно брать несколько конфет.'
        ' Проиграет тот, кто забирает последнюю конфету.'
        ' Команда /cancel, чтобы прекратить игру.\n\n'
        'Введи общее количество конфет: ')
    return SWEETS

def sweets_all(update, _):
    global game_sw
    word = update.message.text
    if word.isdigit():
        game_sw[0]=int(word)
    else:
        game_sw[0]=30
    logger.info("Количество конфет: %s", game_sw[0])
    update.message.reply_text('Теперь введи количество конфет, которое можно брать за один раз (не больше 1/3): ')
    return SWEET_PER_TIME


def check(game_sw, mv, update) -> int:
    '''
    Функция проверяет ход игры и выявляет победителя.
    '''
    
    if game_sw[4] < game_sw[0]:
        game_sw[0] = game_sw[0] - game_sw[4]
        mv+=1
        return mv, game_sw[0]
    elif game_sw[4] >= game_sw[0]:
        game_sw[0]=0
        if game_sw[3] == 0:
            update.message.reply_text(f"В этой игре Вы проиграли!")
            return -1, -1
        elif game_sw[3] == 1:
            update.message.reply_text(f"В этой игре проиграл я!")
            return -1, -1
   
def sweets_per_time(update, _):
    global game_sw
    word = update.message.text
    if word.isdigit() and int(word) <= int(game_sw[0]/3):
        game_sw[1]=int(word)
    else:
        game_sw[1]=int(game_sw[0]/3)
        update.message.reply_text(f'Количество конфет, которое можно брать за один раз будет = {game_sw[1]}')
    logger.info('Количество конфет, которое можно брать за один раз: %s', game_sw[1]) 
    first_move = randint(0,1)
    game_sw[2] = first_move
    print(first_move, game_sw)
    if first_move == 0:
        logger.info("Первый ход человека")
        update.message.reply_text('Первым ходишь ты. Ходи: ') 
    else:
        logger.info("Первый ход бота")
        update.message.reply_text('Первым хожу я: ') 
        if comp_move(update, _) == -1:
            return ConversationHandler.END
    return GAME    

def comp_move(update, _):
        global game_sw
        if game_sw[0] < game_sw[1]:
                game_sw[4] = randint(1,game_sw[0])
        else:
                game_sw[4] = randint(1,game_sw[1])
        update.message.reply_text(f"Мой ход: {game_sw[4]}")
        game_sw[3] = 1
        game_sw[6], game_sw[0] = check(game_sw, game_sw[6], update)
        if game_sw[6] == -1:
            game_sw = [0, 0, 0, 0, 0, 0, 0]
            return -1 
        update.message.reply_text(f'Ваших ходов: {game_sw[5]}, моих ходов: {game_sw[6]}, осталось конфет {game_sw[0]}') 
        update.message.reply_text(f'Ваш ход:')
        return GAME 
       
def chel_move(update, _):
        global game_sw
        word = update.message.text
        if word.isdigit() and int(word) <= game_sw[1]:
                game_sw[4]=int(word)
        else:
                game_sw[4]=game_sw[1]
        logger.info("Количество конфет введенных человеком: %s", game_sw[4])            
        game_sw[3] = 0
        game_sw[5], game_sw[0] = check(game_sw, game_sw[5], update)
        if game_sw[5] == -1:
                game_sw = [0, 0, 0, 0, 0, 0, 0]
                return -1 
        update.message.reply_text(f'Ваших ходов: {game_sw[5]}, моих ходов: {game_sw[6]}, осталось конфет {game_sw[0]}') 
        return GAME 

def game(update, _):
    global game_sw
    game_sw[4]=1
    while game_sw[0] > 0:
            if chel_move(update, _) == -1:
                return ConversationHandler.END
            if comp_move(update, _) == -1:
                return ConversationHandler.END
            return GAME
        
# Обрабатываем команду /cancel если пользователь отменил разговор
def cancel(update, _):
    # определяем пользователя
    user = update.message.from_user
    # Пишем в журнал о том, что пользователь не разговорчивый
    logger.info("Пользователь %s отменил разговор.", user.first_name)
    # Отвечаем на отказ поговорить
    update.message.reply_text(
        'Мое дело предложить - Ваше отказаться'
        ' Будет скучно - пиши.', 
        reply_markup=ReplyKeyboardRemove()
    )
    # Заканчиваем разговор.
    return ConversationHandler.END

if __name__ == '__main__':
    # Создаем Updater и передаем ему токен вашего бота.
    updater = Updater(TOKEN)
    # получаем диспетчера для регистрации обработчиков
    dispatcher = updater.dispatcher
   
    conv_handler = ConversationHandler( # здесь строится логика разговора
        # точка входа в разговор
        
        entry_points=[CommandHandler('start', start)],
        
        # этапы разговора, каждый со своим списком обработчиков сообщений
        states={
            SWEETS: [MessageHandler(Filters.text, sweets_all)],
            SWEET_PER_TIME: [MessageHandler(Filters.text, sweets_per_time)], 
            GAME: [MessageHandler(Filters.text, game)],
        },
        # точка выхода из разговора
        fallbacks=[CommandHandler('cancel', cancel)],
    )

    # Добавляем обработчик разговоров `conv_handler`
    dispatcher.add_handler(conv_handler)

    # Запуск бота
    updater.start_polling()
    updater.idle()