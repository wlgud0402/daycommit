class Car():
  def __init__(self, speed):
    self.speed = speed
  
  def run(self):
    print(str(1 * self.speed)+"의 속도로 달립니다.")

class Supercar(Car):
  def __init__(self, speed):
    super().__init__(speed)
  
  def turboRun(self):
    print("터보카의 터보기능 " + str(3 * self.speed)+"의 속도로 달립니다.")

myCar = Car(10)
print(myCar.speed)
myCar.run()

mySuperCar = Supercar(30)
mySuperCar.turboRun()
mySuperCar.run()