 #prepare the kitchen
from kitchen import Rosemary
from kitchen.utensils import Oven, Plate, Bowl, BakingTray
from kitchen.ingredients import Butter, Egg, Salt, Flour, ChocolateChips, Sugar, BakingPowder

#start with whisking the butter 
Bowl= Bowl.use (name= 'batter_cookies')
butter = Butter.take(grams=150)
Bowl.add (butter)
Bowl.mix()

#add in the sugar 50 grams at a time
for i in range(4):
    sugar = Sugar.take(grams=50)
    Bowl.add (sugar)
    Bowl.mix()

#add eggs in the bowl
for egg in Egg.take(2):
    egg.crack() 
    Bowl.add(egg)
    Bowl.mix()
Bowl.mix()

#Add a pinch of salt and flour + chocolate chips in the bowl gradually!
Bowl.add(Salt.take('pinch'))
for i in range(5):
    flour = Flour.take(grams=60)
    Bowl.add (flour)
    chocolateChips = ChocolateChips.take (grams = 40 )
    Bowl.add (chocolateChips)
    Bowl.mix()

#final ingredient, put baking powder 
Bowl.add(BakingPowder.take('pinch'))
Bowl.mix()

Rosemary.taste(Bowl)

plate = Plate.use(name='cookies')

#Let's preheat the oven!!
oven= Oven.use()
oven.preheat(degrees=175)

#Put the cookies on tray and cook the cookies
Cookie_tray= BakingTray.use (name= 'cooking_cookie')
for i in range(16):
    Cookie_tray.add(Bowl.take('1/16'))
oven.add(Cookie_tray)
oven.bake(minutes=10)
plate.add(Cookie_tray.take())

Rosemary.serve(plate)
