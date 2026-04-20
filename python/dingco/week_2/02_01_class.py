class Person:
    def __init__(self):
        print("hihihi", self)


person_1 = Person()  # hihihi <__main__.Person object at 0x1067e6d60> 이 출력됩니다!

person_2 = Person()  # hihihi <__main__.Person object at 0x106851550> 이 출력됩니다!
