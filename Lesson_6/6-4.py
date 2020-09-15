class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} started'

    def stop(self):
        return f'{self.name}  stopped'

    def turn_right(self):
        return f'{self.name} turned right'

    def turn_left(self):
        return f'{self.name} turned left'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Speed of {self.name} is normal for town car'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'


bugatti = SportCar(180, 'Grey', 'Bugatti', False)
kia = TownCar(40, 'White', 'Kia', False)
man = WorkCar(75, 'Rose', 'Man', True)
ford = PoliceCar(130, 'Blue',  'Ford', True)
print(man.turn_left())
print(f'When {kia.turn_right()}, then {bugatti.stop()}')
print(f'{man.go()} with speed exactly {man.show_speed()}')
print(f'{man.name} is {man.color}')
print(f'Is {bugatti.name} a police car? {bugatti.is_police}')
print(f'Is {man.name}  a police car? {man.is_police}')
print(bugatti.show_speed())
print(kia.show_speed())
print(ford.police())
print(ford.show_speed())