from kitchen import Rosemary
from kitchen.utensils import Pan, Plate, Bowl
from kitchen.ingredients import Butter, Egg, Salt, Milk, Flour
#Code stays the same from previous excercise except for marked occasions. For better overview are the other comments taken out.
#Here one can add in the amount of batches one wants to make
amount_in_multiples_of_8= 4 #Amount of batches
bowl= Bowl.use(name='batter')
for i in range(amount_in_multiples_of_8):
    for i in range(2):
        eggs= Egg.take()
        eggs.crack()
        bowl.add(eggs)
        bowl.mix()
    salt= Salt.take('dash')
    bowl.add(salt)
    for i in range(5):
        flour= Flour.take(grams= 50)
        bowl.add(flour)
        bowl.mix
    for i in range(2):
        milk= Milk.take(ml=250)
        bowl.add(milk)
        bowl.mix()

#To determine the right size of batter that is needed to put into the pan.
portionsize=(1/8)/amount_in_multiples_of_8
pan= Pan.use(name='pancakes')
pan.add(Butter.take('slice'))
for i in range(8*amount_in_multiples_of_8): #To determine how many pancakes we are cooking.
    pan.add(bowl.take(portionsize))
    for i in range(4):
        pan.cook(minutes=0.5)
        pan.flip()
    plate = Plate.use()
    plate.use()
    pancakes = pan.take()
    plate.add(pancakes)
Rosemary.serve(plate)






