class Person:
    def __init__(self, name1, name2):
        self.ivan = name1
        self.tejo = name2
    def person1_type(self):
        ivan_typing = input(f'{self.ivan}: ')
        return ("Ivan :" + '"' + ivan_typing + '"')
    def person2_type(self):
        tejo_typing = input(f'{self.tejo}: ')
        return ("Tejo :" + '"' + tejo_typing + '"')


real_massage = Person('Ivan', 'Tejo')
while True:
    print(real_massage.person1_type())
    print(real_massage.person2_type())
