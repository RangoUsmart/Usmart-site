from decimal import Decimal
from django.conf import settings
from .models import MainUserExp, MainUserInfo, MainUserSkill


class Rezume(object):

    def active(self):
        mass=[]
        for i in range(3):
                mass.append(self(i))
        #     # цикл закончился, поскольку закончился блок с отступом
            # print(self[i])
        print(type(self))
        print(type(mass))

        return self
        
    