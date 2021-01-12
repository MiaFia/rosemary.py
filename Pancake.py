from kitchen import Rosemary
from kitchen.utensils import Pan, Plate, Bowl
from kitchen.ingredients import Butter, Egg, Salt, Milk, Flour

bowl= Bowl.use(name='batter')
#To take two eggs and add them to the bowl:
for i in range(2):
    eggs= Egg.take()
    eggs.crack()
    bowl.add(eggs)
    bowl.mix()
salt= Salt.take('dash')
bowl.add(salt)
#Add flour and mix it in
for i in range(5):
    flour= Flour.take(grams= 50)
    bowl.add(flour)
    bowl.mix

#Add milk and mix it in
for i in range(2):
    milk= Milk.take(ml=250)
    bowl.add(milk)
    bowl.mix()
Rosemary.taste(bowl) #Because I want Rosemary to be able to enjoy the dough.

#Take pan and bake the pancakes
pan= Pan.use(name='pancakes')
pan.add(Butter.take('slice'))
for i in range(8): #Since I want 8 pancakes
    pan.add(bowl.take('1/8'))
    for i in range(4): #To bake them from both sides
        pan.cook(minutes=0.5)
        pan.flip()
    plate = Plate.use()
    plate.use()
    pancakes = pan.take()
    plate.add(pancakes)
Rosemary.serve(plate)
#Rosemary serves each pancake on it's own plate.
#If I wanted it all on one plate I would take out the plate of the pipe.






