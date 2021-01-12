from kitchen.utensils.Utensil import PieDish
from kitchen.ingredients.Ingredient import Cornstarch, Lemon, LemonJuice, LemonZest, Sugar
from kitchen import Rosemary
from kitchen.utensils import Oven, Plate, Bowl, Fridge
from kitchen.ingredients import Butter, Egg, Salt, Milk, Flour, Water, Apple, Lemon, Cornstarch, Cinnamon

#Make cool water
water=Water.take(ml=500)
bowl1=Bowl.use()
bowl1.add(water)
fridge=Fridge.use()
fridge.add(bowl1)
coolwater=fridge.take()
#Preheat oven:
oven= Oven.use()
oven.preheat(degrees=180)

#Take a new bowl and start mixing ingriedients
bowl2= Bowl.use(name='crust dough')
flour=Flour.take(grams=300)
bowl2.add(flour)
bowl2.add(Salt.take(grams=1))
for i in range(25):
    butter= Butter.take(grams=10)
    bowl2.add(butter)
    bowl2.add(coolwater.take('1/25'))
    bowl2.mix

fridge.add(bowl2)
#Start second step
for i in range(6):
    apples=Apple.take()
    apples.peel()
    apples.slice()

lemon=Lemon.take()
lemonzest=lemon.zest()
lemonjuice=lemon.squeeze()

bowl3=Bowl.use()
bowl3.add(apples)
bowl3.add(lemonzest.take('1/2'))
bowl3.add(lemonjuice.take('1/2'))
bowl3.add(Cornstarch.take(grams=10))
bowl3.add(Cinnamon.take(grams=4))
bowl3.add(Salt.take(grams=1))
bowl3.add(Sugar.take(grams=150))

dish=PieDish.use()
fridge.take()
dish.add(bowl2.take('3/4'))
dish.add(bow)

Rosemary.taste(bowl3)





