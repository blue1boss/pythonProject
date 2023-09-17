class Car:
    max_oil = 50 #최대 주유량을 나타내고 있음

    def __init__(self,oil):
        self.oil = oil

    def add_oil(self,oil):
        if oil <= 0: # 0 이하이면 주유는 진행하지 않음
            return
        self.oil+= oil
        if self.oil > Car.max_oil : #최대의 주유량을 넘지 않게 하는 코드
            self.oil = Car.max_oil #넘어버리면 50으로 덮어쓰기가 되는 것으로 진행 100을 넣으면 50만 남게 된다.


    def car_info(self):
        print(f'현재 주유상태: {self.oil}')


class Hybrid(Car):
    max_battery = 30

    def __init__(self, oil, battery):
        super().__init__(oil)
        self.battery = battery

    def charge(self,battery):
        if battery <= 0:
            return
        self.battery += battery
        if self.battery > Hybrid.max_battery:
            self.battery = Hybrid.max_battery

    def hybrid_info(self):
        super(). car_info()
        print(f'현재 충전상태: {self.battery}')


#실행코드
car = Hybrid(0,0)
car.add_oil(100)
car.charge(50)
car.hybrid_info()

#자식에서 부모의 코드를 사용한다는 확장 개념으로 이해할 수 있음.
