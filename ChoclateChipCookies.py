from kitchen.ingredients.Ingredient import Sugar
from kitchen import Rosemary
from kitchen.utensils import Plate, Bowl, Oven, BakingTray
from kitchen.ingredients import Butter, Salt, Egg, Milk, Flour, ChocolateChips, BakingPowder
#Preheating the oven
oven= Oven.use()
oven.preheat(degrees=175)
#Adding ingriedients
bowl=Bowl.use(name= 'cookiebatter')
butter=Butter.take(grams=300)
bowl.add(butter)
#To add sugar in bits:
for i in range(4):
    sugar=Sugar.take(grams=50)
    bowl.add(sugar)
    bowl.mix()
#Add the eggs:
for i in range(2):
    eggs= Egg.take()
    eggs.crack()
    bowl.add(eggs)
bowl.mix()
#For flavour add some salt:
bowl.add(Salt.take('pinch'))
#Add flour, chocolate chips and baking powder.
for i in range(4):
    flour= Flour.take(grams=75)
    bowl.add(flour)
    chocchips= ChocolateChips.take(grams=50)
    bowl.add(chocchips)
    bowl.mix()
bowl.add(BakingPowder.take(grams=4))
Rosemary.taste(bowl) #The cook should also get to taste the batter in the making.

#Put batter on tray:
tray=BakingTray.use(name='cookies')
for i in range(16):
    tray.add(bowl.take('1/16'))

#Bake the dough:
oven.add(tray)
oven.bake(minutes= 10)
#Take out of the oven and serve:
cookies=tray.take()
plate = Plate.use()
plate.add(cookies)
Rosemary.serve(cookies)






