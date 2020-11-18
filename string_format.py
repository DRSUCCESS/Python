# # ...STRING FORMAT
# num1 = 3.1425467389
# num2 = 10.2903943

# # PREVIOUS
# print('num1 is:',num1,'and num2 is:',num2)

# # FORMAT METHOD
# print('num1 is {0:.3f} and num2 is {1:.3f}'.format(num1, num2))

# # USING F-STRINGS
# print(f'num1 is {num1:.4f} and num2 is {num2:.4f}')




# # ...IF ELSE STATEMENT
# age =  int(input ('Enter your age:'))

# if age <10:
#     print('You are young, strange one!')
# elif age < 40:
#     print('The fire in you is strong, strang one!')
# else:
#     print('You are wise beyond doubt, strange one!')


# meaty = input ('Do you eat meat? (y/n):')

# if meaty == 'y':
#     print('here is the meaty meany...')
# else:
#     print('here is the veggie menu...')


# # ...FOR LOOP
# ninjas = ['ryu', 'crystal', 'yoshi', 'ken']

# for ninja in ninjas:
#     # print(ninja)
#     if ninja == 'yoshi':
#         print(f'{ninja} - black belt')
#         break #to break out of the loop
#     else:
#         print(ninja)


# # ...WHILE LOOP
# age = 25
# num = 0

# while num < age:
#     if num == 0:
#         num += 1
#         continue
#     if num % 2 == 0:
#         print(num)
#     if num > 10:
#         break
#     num += 1


# # ...RANGE
# for n in range(5):  # range from 0-4
#     print(n)
# for n in range(1, 5):  # range from 1-4
#     print(n)
# for n in range(0, 20, 4):  # range from 0-19, steps of 4
#     print(n)

# burgers = ['beef', 'chicken', 'veg', 'supreme', 'double']
# # for n in range(len(burgers)):
# #     print(n, burgers[n])
# for n in range(len(burgers) -1, -1, -1):
#     print(n, burgers[n])


# # ...FUNCTIONS
# def greet(name='rye', time='noon'):
#     print(f'Good {time} {name}, hope you are well')

# name =  input('enter your name:')
# time = input('enter the time of day:')
# greet(name, time)

# def area(radius):
#     return 3.142 * radius * radius
# def vol(area, length):
#     print(area * length)

# radius = int(input('enter a radius:'))
# length = int(input('enter a length:'))

# vol(area(radius), length)


# # VARIABLE SCOPE
# my_name = 'ryu'

# def print_name():
#     global my_name #override the global var 'ryu'
#     my_name = 'yoshi'
#     print('the name inside the function is', my_name)

# print_name()
# print('outside the function the name is', my_name)


# # ...DICTIONARIES
# # ...SORTING
# def belt_count(dictionary):
#     belts = list(dictionary.values())
#     for belt in set(belts):
#         num = belts.count(belt)
#         print(f'There are {num} {belt} belts')

# # def ninja_intro(dictionary):
# #     for key,val in dictionary.items():
# #         print(f'I am {key} and a {val} belt')

# ninja_belts = {}

# while True:
#     ninja_name = input('enter a ninja name:')
#     ninja_belt = input('enter a belt colour:')
#     ninja_belts[ninja_name] = ninja_belt


#     another = input('add another? (y/n)')
#     if another == 'y':
#         continue #continue to the top of the loop
#     else:
#         break

# # ninja_intro(ninja_belts)
# belt_count(ninja_belts)



# CLASSES
class Planet:

    shape = 'round' # class att

    # instance att
    def __init__(self, name, radius, gravity, system): # create new obj of class
        self.name = name
        self.radius =  radius
        self.gravity = gravity
        self.system = system

    def orbit(self): # instance mtd for individual class
        return f'{self.name} is orbiting in the {self.system}'
    
    @classmethod
    def commons(cls): # mtd for general class
        return f'All planets are {cls.shape} because of gravity'

    @staticmethod # only have access to individual par
    def spin(speed = '2000 miles per hour'):
        return f'The planet spins and spins at {speed}'


naboo = Planet('Naboo', 30000, 8, 'Naboo System')  # create new instance of the same class
# print(f'Name:{naboo.name}')
# print(naboo.orbit())

print(Planet.spin('a very high speed'))