from kitchen import Rosemary
from kitchen.utensils import Pan, Plate, Bowl
from kitchen.ingredients import Butter, Egg, Salt
import random

bowl = Bowl.use(name='eggs')
for i in range(2):

    egg= Egg.take()
    egg.crack()
    bowl.add(egg)
bowl.mix()


pan = Pan.use(name='omelettes')
for i in range(2):
    pan.add(Butter.take('slice'))
    pan.add(egg)
    pan.add(Salt.take('dash'))
    pan.cook(minutes=2)

    plate = Plate.use()
    plate.use()
    omelettes = pan.take()
    plate.add(omelettes)
#This generates the output.
Rosemary.serve(plate)