from enum import Enum

TRIGGER_WORDS = [
    'хлебушек',
    'хлеб',
]
WELCOME_LIST = [
    'здарова заебал',
    'салам',
    'саламалейкум',
    'ку',
    'привет',
    'хуя ты вежливый'
]
KAZAKH_LIST = [
    'фу, козах',
    'щщс',
    'щещен сыгин',
    'э котакбастар',
    'жумайсынба',
    'борат в чате detected',
    '🇰🇿',
]
FREE_WORDS = {
    'f': ['F', 'помянем'],
    'помянем': ['F', 'помянем'],
    'да': 'Пизда',
    'нет': 'Пидора ответ',
    'я': 'головка от хуя',
    'щщс': KAZAKH_LIST,
    'щещен сыгин': KAZAKH_LIST,
}

FAGGOT_EDITOR_MESSAGES = [
    'Редачер пидор!',
    'Редачер - нехороший человек',
    'редачер эт самое',
    'ха, поiмав редачера',
    'Пусть все видят, как ты редактируешь сообщения',
]

OTHER_DIALOGS = {
    'drop': [
        'aнус себе дропни',
        'кулхацкер в чяте',
        'БД у тебя за щекой оставил, проверяй',
    ],
    'ты': [
        'нет ты',
        'сам такой',
        'а ты еблан рукожопый',
        'нет',
        'не смущай бота',
        '...',
        'да'
    ],
    'пидор': ['спасибо за комплимент', 'ди нахуй'],
    'тупой': ['ебать, тут все интеллектуалы?'],
    'салам': WELCOME_LIST,
    'привет': WELCOME_LIST,
    'ку': WELCOME_LIST,
    'щщс': KAZAKH_LIST,
    'щещен сыгин': KAZAKH_LIST,
}
DEFAULT_PREFIX = [
    '',
    'тупа',
    'скорее всего',
    'вероятно',
    'ля,',
    'ха-ха,',
    'ха,',
]
DEFAULT_CHANCE = [
    'крайне-мала',
    'стопроц',
]
ERROR_CHAT_MESSAGES = [
    'Что-то сломалось, позовите @Lev_key',
    'Ты точно правильно команду ввёл?',
    'Криворукий мудак. Ты сломал бота.',
]
DEFAULT_UNKNOWN_MESSAGE = [
    'Не знаю, что ответить',
    'Мне ЛевК запретил на такое отвечать',
    'Какой ты оригинальный, диву даюсь.'
]

COMMANDS_MAPPER = {
    'кто': 'who_is',
    'у кого': 'who_have_is',
    'топ': 'top',
    'среда': 'wednesday',
    'четверг': 'thursday',
    'вторник': 'tuesday',
    'баян': 'tuesday',
    'f': 'f_func',
    'цифри': 'get_num',
    'цифры': 'get_num',
    'рандом': 'get_num',
    'шанс': 'get_chance',
    'вероятность': 'get_chance',
    'геи': 'gey_double',
    'гей-парочка': 'gey_double',
    'гей-пара': 'gey_double',
    'help': 'help',
    'hlep': 'help',
    'хелп': 'help',
    'выбери': 'choose_variant',
    'стата': 'show_stats',
    'добавь привязку': 'add_local_meme_name',
    'удали привязку': 'delete_local_meme_name',
    'покажи привязки': 'show_local_meme_names',
    'добавь подстроку': 'add_local_substring',
    'удали подстроку': 'delete_local_substring',
    'покажи подстроки': 'show_local_substrings',
    'добавь ответ': 'add_unknown_answer',
    'добавь триггер': 'add_local_free_word',
    'удали триггер': 'delete_local_free_word',
    'покажи триггеры': 'show_local_free_words',
    'цитата': 'get_quote',
    'цит': 'get_quote',
    'понедельник': 'get_quote',
    'обнуляй': 'get_quote',
}

COMMANDS_COLLECTION = list(OTHER_DIALOGS.keys()) + \
                      list(COMMANDS_MAPPER.keys())


class StatsEnum(Enum):
    TOTAL_CALL_SLUG = 'Сколько раз вызвал бота'
    FAGGOTER = 'Сколько раз стал пидором'
    EDITOR = 'Сколько раз редактировал сообщения'
    FLUDER = 'Сколько раз написал сообщение'
    QUOTER = 'Сколько раз просил цитату'


class LocalMemeTypesEnum(Enum):
    MEME_NAMES = 'Локальные команды'
    UNKNOWN_MESSAGE = 'Фразы на отсутствующие команды'
    FREE_WORDS = 'Триггеры'
    SUBSTRING_WORDS = 'Входящие значения'
