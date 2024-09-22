from datetime import date
import pandas as pd

games_date = pd.date_range(start='2024-01-01', end='2024-12-31', freq='W-SUN')

# Впорядкований список гравців
name_of_players = [
    'Загородній Сергій',
    'Сіверський Тімур',
    'Мірошниченко Ігор',
    'Білогуб Олександр',
    'Скобляков Анатолій',
    'Шкуренко Андрій',
    'Тихончук Олександр',
    'Войтович Сергій',
    'Радько Володимир',
    'Кнорозок Юрій',
    'Науменко Андрій',
    'Мутогоров Артем',
    'Мірошниченко Олександр',
    'Войцеховський Іван',
    'Луков Василь',
    'Плаксій Василь',
    'Кірик Віталій',
    'Костюков Дмитро',
    'Битов Ілля',
    'Духаньченко Ігор',
    'Слісаренко Максим',
    'Можарський Олександр',
    'Куценко Олександр',
    'Погорілий Олександр',
    'Шестопал Олексій',
    'Павлюк Сергій',
    'Ставінський Роман',
    'Головко Руслан',
    'Ковтун Сергій',
    'Бекрешов Вадим',
    'Колос Руслан'
]

name_of_players.sort()

# Кольори команд
team_colors = ['Сині', 'Червоні', 'Жовті']

# ----------------------------------------------------------

game_01 = {
    'Червоні': [
        'Науменко Андрій',
        'Битов Ілля',
        'Войцеховський Іван',
        'Мірошниченко Олександр',
        'Мутогоров Артем'
    ],
    'Жовті': [
        'Загородній Сергій',
        'Духаньченко Ігор',
        'Костюков Дмитро',
        'Куценко Олександр',
        'Шестопал Олексій'
    ],
    'Сині': [
        'Погорілий Олександр',
        'Бекрешов Вадим',
        'Мірошниченко Ігор',
        'Радько Володимир',
        'Сіверський Тімур'
    ],
    'Запас': []
}

game_01_points = {
    'Червоні': 13,
    'Сині': 11,
    'Жовті': 30
}

# Список гравців, які брали участь у грі на другій неділі
game_02 = {
    'Червоні': [
        'Науменко Андрій',
        'Духаньченко Ігор',
        'Ковтун Сергій',
        'Луков Василь',
        'Сіверський Тімур'
    ],
    'Жовті': [
        'Погорілий Олександр',
        'Войтович Сергій',
        'Войцеховський Іван',
        'Шестопал Олексій',
        'Шкуренко Андрій'
    ],
    'Сині': [
        'Загородній Сергій',
        'Колос Руслан',
        'Костюков Дмитро',
        'Куценко Олександр',
        'Мірошниченко Олександр'
    ],
    'Запас': []
}

game_02_points = {
    'Червоні': 18,
    'Сині': 16,
    'Жовті': 25
}

# Список гравців, які брали участь у грі на третій неділі

game_03 = {
    'Червоні': [
        'Погорілий Олександр',
        'Білогуб Олександр',
        'Плаксій Василь',
        'Ставінський Роман',
        'Шкуренко Андрій'
    ],
    'Жовті': [
        'Науменко Андрій',
        'Головко Руслан',
        'Духаньченко Ігор',
        'Костюков Дмитро',
        'Мірошниченко Олександр'
    ],
    'Сині': [
        'Загородній Сергій',
        'Ковтун Сергій',
        'Мірошниченко Ігор',
        'Сіверський Тімур',
        'Шестопал Олексій'
    ],
    'Запас': ['Луков Василь']
}

game_03_points = {
    'Червоні': 31,
    'Сині': 17,
    'Жовті': 22,
    'Запас': 10
}

# Список гравців, які брали участь у грі на четвертій неділі

game_04 = {
    'Червоні': [
        'Костюков Дмитро',
        'Мірошниченко Ігор',
        'Мутогоров Артем',
        'Ставінський Роман',
        'Шкуренко Андрій'
    ],
    'Сині': [
        'Духаньченко Ігор',
        'Головко Руслан',
        'Загородній Сергій',
        'Мірошниченко Олександр',
        'Плаксій Василь'
    ],
    'Жовті': [
        'Шестопал Олексій',
        'Білогуб Олександр',
        'Ковтун Сергій',
        'Луков Василь',
        'Погорілий Олександр'
    ],
    'Запас': []
}

game_04_points = {
    'Червоні': 26,
    'Сині': 12,
    'Жовті': 24
}

# Список гравців, які брали участь у грі на п'ятій неділі

game_05 = {
    'Червоні': [
        'Костюков Дмитро',
        'Білогуб Олександр',
        'Сіверський Тімур',
        'Скобляков Анатолій',
        'Слісаренко Максим'
    ],
    'Сині': [
        'Духаньченко Ігор',
        'Головко Руслан',
        'Загородній Сергій',
        'Мірошниченко Ігор',
        'Ставінський Роман'
    ],
    'Жовті': [
        'Шкуренко Андрій',
        'Бекрешов Вадим',
        'Куценко Олександр',
        'Науменко Андрій',
        'Мірошниченко Олександр'
    ],
    'Запас': ['Луков Василь']
}

game_05_points = {
    'Червоні': 24,
    'Сині': 41,
    'Жовті': 6,
    'Запас': 24
}

# Список гравців, які брали участь у грі на шостій неділі

game_06 = {
    'Червоні': [
        'Загородній Сергій',
        'Білогуб Олександр',
        'Головко Руслан',
        'Плаксій Василь',
        'Погорілий Олександр'
    ],
    'Сині': [
        'Костюков Дмитро',
        'Ковтун Сергій',
        'Куценко Олександр',
        'Мірошниченко Ігор',
        'Павлюк Сергій'
    ],
    'Жовті': [
        'Духаньченко Ігор',
        'Мірошниченко Олександр',
        'Науменко Андрій',
        'Сіверський Тімур',
        'Шкуренко Андрій'
    ],
    'Запас': []
}

game_06_points = {
    'Червоні': 32,
    'Сині': 32,
    'Жовті': 5,
    'Запас': 0
}

# Список гравців, які брали участь у грі на сьомій неділі

game_07 = {
    'Червоні': [
        'Загородній Сергій',
        'Білогуб Олександр',
        'Войцеховський Іван',
        'Головко Руслан',
        'Сіверський Тімур'
    ],
    'Сині': [
        'Костюков Дмитро',
        'Мірошниченко Ігор',
        'Мірошниченко Олександр',
        'Науменко Андрій',
        'Скобляков Анатолій'
    ],
    'Жовті': [
        'Духаньченко Ігор',
        'Луков Василь',
        'Погорілий Олександр',
        'Ставінський Роман',
        'Шестопал Олексій'
    ],
    'Запас': []
}

game_07_points = {
    'Червоні': 12,
    'Сині': 18,
    'Жовті': 32,
    'Запас': 0
}

# Список гравців, які брали участь у грі на восьмій неділі

game_08 = {
    'Червоні': [
        'Духаньченко Ігор',
        'Битов Ілля',
        'Білогуб Олександр',
        'Войцеховський Іван',
        'Павлюк Сергій'
    ],
    'Сині': [
        'Загородній Сергій',
        'Мірошниченко Олександр',
        'Науменко Андрій',
        'Скобляков Анатолій',
        'Тихончук Олександр'
    ],
    'Жовті': [
        'Погорілий Олександр',
        'Луков Василь',
        'Плаксій Василь',
        'Сіверський Тімур',
        'Шкуренко Андрій'
    ],
    'Запас': ['Головко Руслан']
}

game_08_points = {
    'Червоні': 39,
    'Сині': 4,
    'Жовті': 28,
    'Запас': 24
}


# Список гравців, які брали участь у грі на дев'ятій неділі

game_09 = {
    'Червоні': [
        'Загородній Сергій',
        'Луков Василь',
        'Плаксій Василь',
        'Сіверський Тімур',
        'Слісаренко Максим'
    ],
    'Сині': [
        'Духаньченко Ігор',
        'Мірошниченко Олександр',
        'Павлюк Сергій',
        'Скобляков Анатолій',
        'Ставінський Роман'
    ],
    'Жовті': [
        'Мірошниченко Ігор',
        'Битов Ілля',
        'Войцеховський Іван',
        'Головко Руслан',
        'Шкуренко Андрій'
    ],
    'Запас': ['Науменко Андрій']
}

game_09_points = {
    'Червоні': 21,
    'Сині': 17,
    'Жовті': 23,
    'Запас': 20
}


# Список гравців, які брали участь у грі на десятій неділі

game_10 = {
    'Червоні': [
        'Загородній Сергій',
        'Головко Руслан',
        'Куценко Олександр',
        'Мірошниченко Олександр',
        'Науменко Андрій'
    ],
    'Сині': [
        'Духаньченко Ігор',
        'Білогуб Олександр',
        'Слісаренко Максим',
        'Ставінський Роман',
        'Шкуренко Андрій'
    ],
    'Жовті': [
        'Мірошниченко Ігор',
        'Битов Ілля',
        'Луков Василь',
        'Плаксій Василь',
        'Скобляков Анатолій'
    ],
    'Запас': []
}

game_10_points = {
    'Червоні': 14,
    'Сині': 24,
    'Жовті': 34,
    'Запас': 0
}

# Список гравців, які брали участь у грі на одинадцятій неділі

game_11 = {
    'Червоні': [
        'Загородній Сергій',
        'Погорілий Олександр',
        'Сіверський Тімур',
        'Ставінський Роман',
        'Шкуренко Андрій'
    ],
    'Сині': [
        'Духаньченко Ігор',
        'Войтович Сергій',
        'Головко Руслан',
        'Мірошниченко Олександр',
        'Шестопал Олексій'
    ],
    'Жовті': [
        'Мірошниченко Ігор',
        'Битов Ілля',
        'Войцеховський Іван',
        'Мутогоров Артем',
        'Скобляков Анатолій'
    ],
    'Запас': ['Луков Василь']
}

game_11_points = {
    'Червоні': 33,
    'Сині': 13,
    'Жовті': 21,
    'Запас': 22
}

# Список гравців, які брали участь у грі на дванадцятій неділі

game_12 = {
    'Червоні': [
        'Ставінський Роман',
        'Войцеховський Іван',
        'Кірик Віталій',
        'Войтович Сергій',
        'Шестопал Олексій'
    ],
    'Сині': [
        'Загородній Сергій',
        'Ковтун Сергій',
        'Сіверський Тімур',
        'Слісаренко Максим',
        'Білогуб Олександр'
    ],
    'Жовті': [
        'Мірошниченко Ігор',
        'Костюков Дмитро',
        'Мутогоров Артем',
        'Шкуренко Андрій',
        'Мірошниченко Олександр'
    ],
    'Запас': ['Погорілий Олександр']
}

game_12_points = {
    'Червоні': 21,
    'Сині': 10,
    'Жовті': 33,
    'Запас': 10
}

# Список гравців, які брали участь у грі на тринадцятій неділі

game_13 = {
    'Червоні': [
        'Загородній Сергій',
        'Погорілий Олександр',
        'Сіверський Тімур',
        'Кірик Віталій',
        'Скобляков Анатолій'
    ],
    'Сині': [
        'Духаньченко Ігор',
        'Мутогоров Артем',
        'Науменко Андрій',
        'Луков Василь',
        'Білогуб Олександр'
    ],
    'Жовті': [
        'Мірошниченко Ігор',
        'Ковтун Сергій',
        'Плаксій Василь',
        'Шкуренко Андрій',
        'Мірошниченко Олександр'
    ],
    'Запас': ['Костюков Дмитро']
}

game_13_points = {
    'Червоні': 33,
    'Сині': 17,
    'Жовті': 13,
    'Запас': 21
}

# Список гравців, які брали участь у грі на чотирнадцятій неділі

game_14 = {
    'Червоні': [
        'Духаньченко Ігор',
        'Костюков Дмитро',
        'Шкуренко Андрій',
        'Шестопал Олексій',
        'Білогуб Олександр'
    ],
    'Сині': [
        'Загородній Сергій',
        'Битов Ілля',
        'Кнорозок Юрій',
        'Войтович Сергій',
        'Слісаренко Максим'
    ],
    'Жовті': [
        'Мірошниченко Ігор',
        'Войцеховський Іван',
        'Науменко Андрій',
        'Скобляков Анатолій',
        'Мірошниченко Олександр'
    ],
    'Запас': ['Погорілий Олександр']
}

game_14_points = {
    'Червоні': 5,
    'Сині': 26,
    'Жовті': 25,
    'Запас': 19
}

# Список гравців, які брали участь у грі на п'ятнадцятій неділі

game_15 = {
    'Червоні': [
        'Погорілий Олександр',
        'Ковтун Сергій',
        'Луков Василь',
        'Мірошниченко Олександр',
        'Шкуренко Андрій'
    ],
    'Сині': [
        'Загородній Сергій',
        'Білогуб Олександр',
        'Костюков Дмитро',
        'Ставінський Роман',
        'Скобляков Анатолій'
    ],
    'Жовті': [
        'Мірошниченко Ігор',
        'Куценко Олександр',
        'Плаксій Василь',
        'Сіверський Тімур',
        'Шестопал Олексій'
    ],
    'Запас': []
}

game_15_points = {
    'Червоні': 17,
    'Сині': 11,
    'Жовті': 23,
    'Запас': 0
}

# Список гравців, які брали участь у грі на шістнадцятій неділі

game_16 = {
    'Червоні': [
        'Духаньченко Ігор',
        'Слісаренко Максим',
        'Ковтун Сергій',
        'Шкуренко Андрій',
        'Шестопал Олексій'
    ],
    'Сині': [
        'Загородній Сергій',
        'Войцеховський Іван',
        'Сіверський Тімур',
        'Науменко Андрій',
        'Скобляков Анатолій'
    ],
    'Жовті': [
        'Мірошниченко Ігор',
        'Битов Ілля',
        'Луков Василь',
        'Мірошниченко Олександр',
        'Білогуб Олександр'
    ],
    'Запас': []
}

game_16_points = {
    'Червоні': 25,
    'Сині': 36,
    'Жовті': 12,
    'Запас': 0
}

# Список гравців, які брали участь у грі на сімнадцятій неділі

game_17 = {
    'Червоні': [
        'Духаньченко Ігор',
        'Погорілий Олександр',
        'Науменко Андрій',
        'Шестопал Олексій',
        'Білогуб Олександр'
    ],
    'Сині': [
        'Загородній Сергій',
        'Сіверський Тімур',
        'Мутогоров Артем',
        'Луков Василь',
        'Мірошниченко Олександр'
    ],
    'Жовті': [
        'Мірошниченко Ігор',
        'Войцеховський Іван',
        'Битов Ілля',
        'Шкуренко Андрій',
        'Куценко Олександр'
    ],
    'Запас': []
}

game_17_points = {
    'Червоні': 17,
    'Сині': 16,
    'Жовті': 27,
    'Запас': 0
}

# Список гравців, які брали участь у грі на вісімнадцятій неділі

game_18 = {
    'Червоні': [
        'Мірошниченко Ігор',
        'Погорілий Олександр',
        'Науменко Андрій',
        'Скобляков Анатолій',
        'Мірошниченко Олександр'
    ],
    'Сині': [
        'Духаньченко Ігор',
        'Костюков Дмитро',
        'Битов Ілля',
        'Луков Василь',
        'Шестопал Олексій'
    ],
    'Жовті': [
        'Загородній Сергій',
        'Войцеховський Іван',
        'Сіверський Тімур',
        'Куценко Олександр',
        'Білогуб Олександр'
    ],
    'Запас': ['Шкуренко Андрій']
}

game_18_points = {
    'Червоні': 18,
    'Сині': 28,
    'Жовті': 18,
    'Запас': 10
}

# Список гравців, які брали участь у грі на дев'ятнадцятій неділі

game_19 = {
    'Червоні': [
        'Мірошниченко Ігор',
        'Погорілий Олександр',
        'Сіверський Тімур',
        'Шкуренко Андрій',
        'Мірошниченко Олександр'
    ],
    'Сині': [
        'Духаньченко Ігор',
        'Костюков Дмитро',
        'Битов Ілля',
        'Слісаренко Максим',
        'Шестопал Олексій'
    ],
    'Жовті': [
        'Загородній Сергій',
        'Войцеховський Іван',
        'Мутогоров Артем',
        'Куценко Олександр',
        'Білогуб Олександр'
    ],
    'Запас': ['Науменко Андрій']
}

game_19_points = {
    'Червоні': 26,
    'Сині': 22,
    'Жовті': 20,
    'Запас': 10
}

# Список гравців, які брали участь у грі на двадцятій неділі

game_20 = {
    'Червоні': [
        'Шкуренко Андрій',
        'Куценко Олександр',
        'Науменко Андрій',
        'Погорілий Олександр'
    ],
    'Сині': [
        'Духаньченко Ігор',
        'Битов Ілля',
        'Білогуб Олександр',
        'Костюков Дмитро',
        'Мутогоров Артем'
    ],
    'Жовті': [
        'Загородній Сергій',
        'Головко Руслан',
        'Мірошниченко Олександр',
        'Сіверський Тімур',
        'Слісаренко Максим'
    ],
    'Запас': ['Мірошниченко Ігор']
}

game_20_points = {
    'Червоні': 28,
    'Сині': 26,
    'Жовті': 6,
    'Запас': 28
}

# Список гравців, які брали участь у грі на двадцять першій неділі

game_21 = {
    'Червоні': [
        'Загородній Сергій',
        'Погорілий Олександр',
        'Плаксій Василь',
        'Головко Руслан',
        'Мірошниченко Олександр'
    ],
    'Сині': [
        'Духаньченко Ігор',
        'Костюков Дмитро',
        'Науменко Андрій',
        'Луков Василь',
        'Скобляков Анатолій'
    ],
    'Жовті': [
        'Мірошниченко Ігор',
        'Битов Ілля',
        'Сіверський Тімур',
        'Кірик Віталій',
        'Білогуб Олександр'
    ],
    'Запас': []
}

game_21_points = {
    'Червоні': 37,
    'Сині': 27,
    'Жовті': 8,
    'Запас': 0
}

# Список гравців, які брали участь у грі на двадцять другій неділі

game_22 = {
    'Червоні': [
        'Мірошниченко Ігор',
        'Духаньченко Ігор',
        'Битов Ілля',
        'Шкуренко Андрій',
        'Мірошниченко Олександр'
    ],
    'Сині': [
        'Погорілий Олександр',
        'Войцеховський Іван',
        'Головко Руслан',
        'Науменко Андрій',
        'Куценко Олександр'
    ],
    'Жовті': [
        'Загородній Сергій',
        'Плаксій Василь',
        'Костюков Дмитро',
        'Кірик Віталій',
        'Білогуб Олександр'
    ],
    'Запас': ['Луков Василь']
}

game_22_points = {
    'Червоні': 22,
    'Сині': 41,
    'Жовті': 8,
    'Запас': 24
}

# Список гравців, які брали участь у грі на двадцять третій неділі

game_23 = {
    'Червоні': [
        'Погорілий Олександр',
        'Плаксій Василь',
        'Войтович Сергій',
        'Слісаренко Максим',
        'Білогуб Олександр'
    ],
    'Сині': [
        'Загородній Сергій',
        'Духаньченко Ігор',
        'Сіверський Тімур',
        'Луков Василь',
        'Мірошниченко Олександр'
    ],
    'Жовті': [
        'Мірошниченко Ігор',
        'Костюков Дмитро',
        'Науменко Андрій',
        'Шкуренко Андрій',
        'Шестопал Олексій'
    ],
    'Запас': ['Головко Руслан']
}

game_23_points = {
    'Червоні': 22,
    'Сині': 16,
    'Жовті': 24,
    'Запас': 10
}

# Список гравців, які брали участь у грі на двадцять четвертій неділі

game_24 = {
    'Червоні': [
        'Загородній Сергій',
        'Головко Руслан',
        'Мутогоров Артем',
        'Куценко Олександр',
        'Слісаренко Максим'
    ],
    'Сині': [
        'Духаньченко Ігор',
        'Костюков Дмитро',
        'Кнорозок Юрій',
        'Скобляков Анатолій',
        'Шестопал Олексій'
    ],
    'Жовті': [
        'Мірошниченко Ігор',
        'Науменко Андрій',
        'Войтович Сергій',
        'Шкуренко Андрій',
        'Білогуб Олександр'
    ],
    'Запас': ['Мірошниченко Олександр']
}

game_24_points = {
    'Червоні': 21,
    'Сині': 28,
    'Жовті': 13,
    'Запас': 21
}

# Список гравців, які брали участь у грі на двадцять п'ятій неділі

game_25 = {
    'Червоні': [
        'Загородній Сергій',
        'Головко Руслан',
        'Науменко Андрій',
        "Шкуренко Андрій",
        "Білогуб Олександр"
    ],
    'Сині': [
        'Духаньченко Ігор',
        'Костюков Дмитро',
        'Мутогоров Артем',
        "Войтович Сергій",
        "Шестопал Олексій"
    ],
    'Жовті': [
        'Мірошниченко Ігор',
        'Сіверський Тімур',
        "Куценко Олександр",
        "Слісаренко Максим",
        "Мірошниченко Олександр"
    ],
    'Запас': []
}

game_25_points = {
    'Червоні': 12,
    'Сині': 39,
    'Жовті': 23,
    'Запас': 0
}

# Список гравців, які брали участь у грі на двадцять шостій неділі

game_26 = {
    'Червоні': [
        'Погорілий Олександр',
        "Ковтун Сергій",
        "Войтович Сергій",
        "Мутогоров Артем",
        "Мірошниченко Олександр"
    ],
    'Сині': [
        'Духаньченко Ігор',
        'Головко Руслан',
        "Луков Василь",
        "Слісаренко Максим",
        "Білогуб Олександр"
    ],
    'Жовті': [
        'Загородній Сергій',
        "Сіверський Тімур",
        "Битов Ілля",
        "Скобляков Анатолій",
        "Шестопал Олексій"
    ],
    'Запас': ['Кнорозок Юрій']
}

game_26_points = {
    'Червоні': 33,
    'Сині': 14,
    'Жовті': 18,
    'Запас': 10
}

# Список гравців, які брали участь у грі на двадцять сьомій неділі

game_27 = {
    'Червоні': [
        'Мірошниченко Ігор',
        "Головко Руслан",
        "Науменко Андрій",
        "Слісаренко Максим",
    ],
    'Сині': [
        'Духаньченко Ігор',
        'Костюков Дмитро',
        "Битов Ілля",
        "Радько Володимир",
        "Білогуб Олександр"
    ],
    'Жовті': [
        'Загородній Сергій',
        "Сіверський Тімур",
        "Погорілий Олександр",
        "Войтович Сергій",
        "Шестопал Олексій"
    ],
    'Запас': []
}

game_27_points = {
    'Червоні': 24,
    'Сині': 11,
    'Жовті': 18,
    'Запас': 0
}

# Список гравців, які брали участь у грі на двадцять восьмій неділі

game_28 = {
    'Червоні': [
        'Загородній Сергій',
        "Погорілий Олександр",
        "Ковтун Сергій",
        "Сіверський Тімур",
        "Кнорозок Юрій"
    ],
    'Сині': [
        'Духаньченко Ігор',
        'Костюков Дмитро',
        "Плаксій Василь",
        "Скобляков Анатолій",
        "Білогуб Олександр"
    ],
    'Жовті': [
        'Мірошниченко Ігор',
        "Войцеховський Іван",
        "Битов Ілля",
        "Науменко Андрій",
        "Слісаренко Максим"
    ],
    'Запас': ["Мутогоров Артем"]
}

game_28_points = {
    'Червоні': 26,
    'Сині': 16,
    'Жовті': 32,
    'Запас': 10
}

# Список гравців, які брали участь у грі на двадцять дев'ятій неділі

game_29 = {
    'Червоні': [
        'Загородній Сергій',
        "Погорілий Олександр",
        "Плаксій Василь",
        "Радько Володимир",
    ],
    'Сині': [
        'Духаньченко Ігор',
        'Костюков Дмитро',
        "Битов Ілля",
        "Скобляков Анатолій",
        "Слісаренко Максим"
    ],
    'Жовті': [
        'Мірошниченко Ігор',
        "Войцеховський Іван",
        "Сіверський Тімур",
        "Куценко Олександр",
        "Білогуб Олександр"
    ],
    'Запас': []
}

game_29_points = {
    'Червоні': 24,
    'Сині': 36,
    'Жовті': 11,
    'Запас': 0
}

# Список гравців, які брали участь у грі на тридцятій неділі

game_30 = {
    'Червоні': [
        'Погорілий Олександр',
        "Ковтун Сергій",
        "Плаксій Василь",
        "Кнорозок Юрій",
        "Мірошниченко Олександр"
    ],
    'Сині': [
        'Духаньченко Ігор',
        'Костюков Дмитро',
        "Мутогоров Артем",
        "Слісаренко Максим",
        "Радько Володимир"
    ],
    'Жовті': [
        'Мірошниченко Ігор',
        "Загородній Сергій",
        "Битов Ілля",
        "Скобляков Анатолій",
        "Білогуб Олександр"
    ],
    'Запас': []
}

game_30_points = {
    'Червоні': 36,
    'Сині': 25,
    'Жовті': 19,
    'Запас': 0
}

# Список гравців, які брали участь у грі на тридцять першій неділі

game_31 = {
    'Червоні': [
        'Загородній Сергій',
        "Мірошниченко Ігор",
        "Плаксій Василь",
        "Сіверський Тімур",
        "Сизий Роман"
    ],
    'Сині': [
        'Духаньченко Ігор',
        'Костюков Дмитро',
        "Скобляков Анатолій",
        "Слісаренко Максим",
        "Білогуб Олександр"
    ],
    'Жовті': [
        'Погорілий Олександр',
        "Битов Ілля",
        "Мутогоров Артем",
        "Кнорозок Юрій",
        "Мірошниченко Олександр"
    ],
    'Запас': []
}

game_31_points = {
    'Червоні': 31,
    'Сині': 16,
    'Жовті': 19,
    'Запас': 0
}

# Список гравців, які брали участь у грі на тридцять другій неділі

game_32 = {
    'Червоні': [
        'Загородній Сергій',
        "Мірошниченко Ігор",
        "Плаксій Василь",
        "Кнорозок Юрій",
        "Шестопал Олексій"
    ],
    'Сині': [
        'Духаньченко Ігор',
        'Костюков Дмитро',
        "Битов Ілля",
        "Скобляков Анатолій",
        "Білогуб Олександр"
    ],
    'Жовті': [
        'Погорілий Олександр',
        "Ковтун Сергій",
        "Головко Руслан",
        "Куценко Олександр",
        "Слісаренко Максим"
    ],
    'Запас': []
}

game_32_points = {
    'Червоні': 21,
    'Сині': 17,
    'Жовті': 34,
    'Запас': 0
}

# Список гравців, які брали участь у грі на тридцять третій неділі

game_33 = {
    'Червоні': [
        'Загородній Сергій',
        "Ковтун Сергій",
        "Сіверський Тімур",
        "Науменко Андрій",
        "Шкуренко Андрій"
    ],
    'Сині': [
        'Духаньченко Ігор',
        'Костюков Дмитро',
        "Битов Ілля",
        "Скобляков Анатолій",
        "Мірошниченко Олександр"
    ],
    'Жовті': [
        'Погорілий Олександр',
        "Головко Руслан",
        "Кнорозок Юрій",
        "Куценко Олександр",
        "Білогуб Олександр"
    ],
    'Запас': ["Луков Василь"]
}

game_33_points = {
    'Червоні': 29,
    'Сині': 13,
    'Жовті': 32,
    'Запас': 10
}

# Список гравців, які брали участь у грі на тридцять четвертій неділі

game_34 = {
    'Червоні': [
        'Загородній Сергій',
        "Ковтун Сергій",
        "Плаксій Василь",
        "Сіверський Тімур",
        "Слісаренко Максим"
    ],
    'Сині': [
        'Духаньченко Ігор',
        'Костюков Дмитро',
        "Мутогоров Артем",
        "Науменко Андрій",
        "Шестопал Олексій"
    ],
    'Жовті': [
        'Погорілий Олександр',
        "Головко Руслан",
        "Битов Ілля",
        "Шкуренко Андрій",
        "Білогуб Олександр"
    ],
    'Запас': []
}

game_34_points = {
    'Червоні': 14,
    'Сині': 29,
    'Жовті': 22,
    'Запас': 0
}

# Список гравців, які брали участь у грі на тридцять п'ятій неділі

game_35 = {
    'Червоні': [
        'Загородній Сергій',
        "Мірошниченко Ігор",
        "Плаксій Василь",
        "Сіверський Тімур",
        "Шестопал Олексій"
    ],
    'Сині': [
        'Духаньченко Ігор',
        'Костюков Дмитро',
        "Мутогоров Артем",
        "Науменко Андрій",
        "Шкуренко Андрій"
    ],
    'Жовті': [
        'Погорілий Олександр',
        "Головко Руслан",
        "Войтович Сергій",
        "Луков Василь",
        "Білогуб Олександр"
    ],
    'Запас': []
}

game_35_points = {
    'Червоні': 25,
    'Сині': 20,
    'Жовті': 29,
    'Запас': 0
}

# Список гравців, які брали участь у грі на тридцять шостій неділі

game_36 = {
    'Червоні': [
        'Мірошниченко Ігор',
        "Плаксій Василь",
        "Мутогоров Артем",
        "Шкуренко Андрій",
        "Мірошниченко Олександр"
    ],
    'Сині': [
        'Духаньченко Ігор',
        'Головко Руслан',
        "Войтович Сергій",
        "Шестопал Олексій",
        "Слісаренко Максим"
    ],
    'Жовті': [
        'Загородній Сергій',
        "Сіверський Тімур",
        "Сизий Роман",
        "Скобляков Анатолій",
        "Білогуб Олександр"
    ],
    'Запас': []
}

game_36_points = {
    'Червоні': 22,
    'Сині': 25,
    'Жовті': 17,
    'Запас': 0
}

# Список гравців, які брали участь у грі на тридцять сьомій неділі

game_37 = {
    'Червоні': [
        'Загородній Сергій',
        "Мірошниченко Ігор",
        "Ковтун Сергій",
        "Сіверський Тімур",
        "Скобляков Анатолій"
    ],
    'Сині': [
        'Погорілий Олександр',
        "Головко Руслан",
        "Войтович Сергій",
        "Слісаренко Максим",
        "Білогуб Олександр"
    ],
    'Жовті': [
        'Духаньченко Ігор',
        "Костюков Дмитро",
        "Плаксій Василь",
        "Мутогоров Артем",
        "Мірошниченко Олександр"
    ],
    'Запас': []
}

game_37_points = {
    'Червоні': 14,
    'Сині': 16,
    'Жовті': 42,
    'Запас': 0
}

# Список гравців, які брали участь у грі на тридцять восьмій неділі

game_38 = {
    'Червоні': [
        'Загородній Сергій',
        "Мірошниченко Ігор",
        "Головко Руслан",
        "Сіверський Тімур",
        "Слісаренко Максим"
    ],
    'Сині': [
        'Погорілий Олександр',
        "Плаксій Василь",
        "Ковтун Сергій",
        "Войтович Сергій",
        "Мірошниченко Олександр"
    ],
    'Жовті': [
        'Духаньченко Ігор',
        "Костюков Дмитро",
        "Луков Василь",
        "Шестопал Олексій",
        "Білогуб Олександр"
    ],
    'Запас': []
}

game_38_points = {
    'Червоні': 20,
    'Сині': 25,
    'Жовті': 29,
    'Запас': 0
}

# --------------------------------------------------------------------------------------------

# Формуємо таблицю з результатами ігор
games_df = pd.DataFrame(
    columns=['Дата', 'Гравець', 'Команда', 'Номер гри', 'Очки']
)


def add_game_to_df(game, game_points, game_number):
    for team, players in game.items():
        for player in players:
            games_df.loc[len(games_df)] = [
                games_date[game_number],
                player,
                team,
                game_number + 1,
                game_points[team]
            ]


add_game_to_df(game_01, game_01_points, 0)
add_game_to_df(game_02, game_02_points, 1)
add_game_to_df(game_03, game_03_points, 2)
add_game_to_df(game_04, game_04_points, 3)
add_game_to_df(game_05, game_05_points, 4)
add_game_to_df(game_06, game_06_points, 5)
add_game_to_df(game_07, game_07_points, 6)
add_game_to_df(game_08, game_08_points, 7)
add_game_to_df(game_09, game_09_points, 8)
add_game_to_df(game_10, game_10_points, 9)
add_game_to_df(game_11, game_11_points, 10)
add_game_to_df(game_12, game_12_points, 11)
add_game_to_df(game_13, game_13_points, 12)
add_game_to_df(game_14, game_14_points, 13)
add_game_to_df(game_15, game_15_points, 14)
add_game_to_df(game_16, game_16_points, 15)
add_game_to_df(game_17, game_17_points, 16)
add_game_to_df(game_18, game_18_points, 17)
add_game_to_df(game_19, game_19_points, 18)
add_game_to_df(game_20, game_20_points, 19)
add_game_to_df(game_21, game_21_points, 20)
add_game_to_df(game_22, game_22_points, 21)
add_game_to_df(game_23, game_23_points, 22)
add_game_to_df(game_24, game_24_points, 23)
add_game_to_df(game_25, game_25_points, 24)
add_game_to_df(game_26, game_26_points, 25)
add_game_to_df(game_27, game_27_points, 26)
add_game_to_df(game_28, game_28_points, 27)
add_game_to_df(game_29, game_29_points, 28)
add_game_to_df(game_30, game_30_points, 29)
add_game_to_df(game_31, game_31_points, 30)
add_game_to_df(game_32, game_32_points, 31)
add_game_to_df(game_33, game_33_points, 32)
add_game_to_df(game_34, game_34_points, 33)
add_game_to_df(game_35, game_35_points, 34)
add_game_to_df(game_36, game_36_points, 35)
add_game_to_df(game_37, game_37_points, 36)
add_game_to_df(game_38, game_38_points, 37)

games = [game_01, game_02, game_03, game_04, game_05, game_06, game_07, game_08, game_09, game_10,
            game_11, game_12, game_13, game_14, game_15, game_16, game_17, game_18, game_19, game_20,
            game_21, game_22, game_23, game_24, game_25, game_26, game_27, game_28, game_29, game_30,
            game_31, game_32, game_33, game_34, game_35, game_36, game_37, game_38]