from datetime import date
from time import ctime


class Greeter:
    name = ""

    def __init__(self, name):
        self.name = name
        pass

    @staticmethod
    def _day():
        """
        현재 요일 반환
        """
        weekdays = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
        today = list(map(int, str(date.today()).split("-")))
        weekday = weekdays[date(today[0], today[1], today[2]).weekday()]
        return weekday

    def _part_of_day(self):
        """
        현재 시각에 해당하는 값을 반환한다.
        """
        time = ctime().split()[3]
        hour = int(time.split(":")[0])
        if hour < 12:
            return "morning"
        elif hour < 5:
            return "afternoon"
        else:
            return "evening"

    def greet(self, store):
        """
        상점 이름이 store에 주어지면
        메서드 _day, _part_of_day 결과와 함께 메세지를 출력한다.
        """

        message = f"""Hi, my name is {self.name}, and welcome to {store}!\
        \nHow's your {self._day()}, {self._part_of_day()} going?\
        \nHere's a coupon for 20% off!"""
        return print(message)


def main():
    greeter = Greeter(input("이름을 입력해주세요: "))
    greeter.greet(input("store 이름을 입력해주세요: "))


if __name__ == "__main__":
    main()
