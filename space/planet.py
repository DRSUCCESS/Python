# CLASSES
class Planet:

    shape = 'round'  # class att

    # instance att
    def __init__(self, name, radius, gravity, system):  # create new obj of class
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):  # instance mtd for individual class
        return f'{self.name} is orbiting in the {self.system}'

    @classmethod
    def commons(cls):  # mtd for general class
        return f'All planets are {cls.shape} because of gravity'

    @staticmethod  # only have access to individual par
    def spin(speed='2000 miles per hour'):
        return f'The planet spins and spins at {speed}'
