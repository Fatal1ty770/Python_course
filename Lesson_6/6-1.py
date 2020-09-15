from time import sleep


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        i = 0
        while True:
            print(f'Светофор переключается \n '
                  f'{TrafficLight.__color[i]}')
            if i == 0:
                sleep(3)
            elif i == 1:
                sleep(2)
            elif i == 2:
                sleep(4)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()