
class Car:
    def Go():
        print('Car Go')

    def Stop(self):
        print('Car Stop')

c = Car()

# 메소드 호출
Car.Go()
#c.Go()      # Go(c)

c.Stop()    # Stop(c)
Car.Stop(c) # 이렇게도 호출가능