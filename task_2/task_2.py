import datetime
from pyfiglet import Figlet



star_font = Figlet(font="3-d")


def get_input():
    """Запрашивает дату рождения пользователя."""
    day = int(input("Введите день рождения: "))
    month = int(input("Введите месяц рождения: "))
    year = int(input("Введите год рождения: "))
    return day, month, year

def is_weekday(date: datetime.date) -> bool:
    """Проверяет, является ли дата выходным днем (суббота или воскресенье)."""
    weekday = date.weekday()
    return weekday in (5, 6)

def is_leap_year(year: int) -> bool:
    """Проверяет, является ли год високосным."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def calculate_age(born: datetime.date) -> int:
    """Рассчитывает возраст пользователя на текущую дату."""
    today = datetime.date.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    return age

def main():
    day, month, year = get_input()
    birthday = datetime.date(year, month, day)
    weekday = birthday.weekday()
    leap_year = is_leap_year(year)
    age = calculate_age(birthday)
    result_art = star_font.renderText(f"{day}.{month}.{year}")
    
    print(f"\nВаш день рождения приходится на {['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье'][weekday]}")
    print(f"{year} был {'' if leap_year else 'не'} високосным годом.")
    print(f"Вам сейчас {age} лет.")
    print(result_art.replace("/", " "))



    

if __name__ == "__main__":
    main()