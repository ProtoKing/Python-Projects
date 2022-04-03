
def add(*args):
    sum = 0
    for n in args:
        sum += n
    return print(sum)

def calculate(n, **kwargs):
    # for key, value in kwargs.items():
    #   print(key)
    #   print(value)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

add(3, 4, 5)

class Car:
    def __init__(self, **kw):
        self.make = kw['make']
        self.model = kw['model']

my_car = Car(make='Nissan')
print(my_car.make)

