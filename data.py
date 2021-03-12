data = \
{
    "language": [
        "ru"
    ],
    "messages": {
        "ru": {
            "help": [
                "/screenshot <count> <sec> - получить <count> снимков экрана с задержкой <sec> между ними. Не желательно <count> ставить более 10.",
                "/photo - сделать снимок с камеры",
                "/writetext <text> - напечатаетсяя текст <text>. \nПяока не работает!",
                "/click <cords> - клткнет по кординатам. кординаты вводить в формате: (x, y) Обязательно в скобках, обязательно через запятую.\nПока не работает!",
                "/comb <key1> <key2> - выполняет сочетание клавиш.\nПока не работает!",
                "/language - Узнать доступные языки.\nПока не работает!",
                "/language <lang> - сменить язык на <lang>. Внимание в <lang> должен быть буквенный код страны.\nПока не работает!",
                "/help <lang>- получить этот список на языке <lang>. Есди <lang> не указан используется код указанный в вашем профиле.",
                "/aboutme - информация о создателе. То есть об о мне. \nПока не работает!"
            ],
            "messages": {
                "errors": {
                    "wrong_message_format": "К сожалению я пка не умею распозновать данный формат сообщений, пожалуйста отправте текстовое сообшщение.",
                    "not_command_transferred": "К сожалению пока я умею работать только с командами"
                },
                "warning": {

                },
                "info":{
                    "doing": "Выполняю, ожидайте."
                },
                "answers": {
                    "/start": " Приветствуем вас в программе удаленного администрирования, чтобы получить список команд напишите /help"
            }
            }
        }
    },
    "metods": {
        "start": {
            "command": "/start",
            "countdata": 0,
            "typedata": [],
            "data": []
        },
        "screenshot": {
            "command": "/screenshot",
            "countdata": 2,
            "typedata": ["int", "float"],
            "data": ["count", "sec"]
        },
        "writetext": {
            "command": "/writetext",
            "countdata": 1,
            "typedata": ["str"],
            "data": ["text"]
        },
        "click": {
            "command": "/click",
            "countdata": 1,
            "typedata": ["tuple"],
            "data": ["coords"]
        },
        "comb": {
            "command": "/comb",
            "countdata": 2,
            "typedata": ["str", "str"],
        "data": ["key1", "key2"]
        },
        "help": {
            "command": "/help",
            "countdata": 1,
            "typedata": ["str"],
            "data": []
        },
        "aboutme": {
            "command": "/aboutme",
            "countdata": 0,
            "typedata": [],
            "data": []
        }
    }
}
