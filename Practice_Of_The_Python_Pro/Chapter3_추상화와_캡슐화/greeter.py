from datetime import date
from time import ctime
from datetime import datetime


def day():
    """
    현재 요일 반환
    """
    return datetime.now().strftime("%A")


def part_of_day():
    """
    현재 시각에 해당하는 값을 반환한다.
    """

    current_hour = datetime.now().hour

    if current_hour < 12:
        part_of_day = "morning"
    elif current_hour < 17:
        part_of_day = "afternoon"
    else:
        part_of_day = "evening"

    return part_of_day


class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self, store):
        """
        상점 이름이 store에 주어지면
        메서드 _day, _part_of_day 결과와 함께 메세지를 출력한다.
        """

        message = f"""Hi, my name is {self.name}, and welcome to {store}!\
        \nHow's your {day()}, {part_of_day()} going?\
        \nHere's a coupon for 20% off!"""
        return print(message)


def main():
    greeter = Greeter(input("이름을 입력해주세요: "))
    greeter.greet(input("store 이름을 입력해주세요: "))


if __name__ == "__main__":
    main()
