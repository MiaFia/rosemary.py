from kitchen.ingredients.Ingredient import Sugar
from kitchen import Rosemary
from kitchen.utensils import Plate, Bowl, Oven, BakingTray
from kitchen.ingredients import Butter, Salt, Egg, Milk, Flour, ChocolateChips, BakingPowder
#This recipe is the same as the original one. The only difference here is that one can vary the amount of batches one wants to make
#There are 16 cookies per batch. All changed elements are commented. For better overview are the other comments taken out.
#Amount of batches
batches= 4

oven= Oven.use()
oven.preheat(degrees=175)
bowl=Bowl.use(name= 'cookiebatter')
for i in range(batches):
    butter=Butter.take(grams=300)
    bowl.add(butter)
    for i in range(4):
        sugar=Sugar.take(grams=50)
        bowl.add(sugar)
        bowl.mix()
    for i in range(2):
        eggs= Egg.take()
        eggs.crack()
        bowl.add(eggs)
    bowl.mix()
    bowl.add(Salt.take('pinch'))
    for i in range(4):
        flour= Flour.take(grams=75)
        bowl.add(flour)
        chocchips= ChocolateChips.take(grams=50)
        bowl.add(chocchips)
        bowl.mix()
    bowl.add(BakingPowder.take(grams=4))

#Since the amount of dough needs to be the same per cookie.
doughamount=((1/16)/batches)
tray=BakingTray.use(name='cookies')
for i in range(16*batches): #Since the dough needs to be added a certain amount of times.
    tray.add(bowl.take(doughamount))

oven.add(tray)
oven.bake(minutes= 10)
cookies=tray.take()
plate = Plate.use()
plate.add(cookies)
Rosemary.serve(cookies)






