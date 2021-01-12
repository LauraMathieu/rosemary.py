#preparing the kitchen
from kitchen import Rosemary
from kitchen.utensils import Pan, Plate, Bowl 
from kitchen.ingredients import Butter, Egg, Salt, Flour, Milk

#start with whisking the two eggs in a bowl
Bowl= Bowl.use (name= 'batter')
for egg in Egg.take(2):
    egg.crack() 
    Bowl.add(egg)
    Bowl.mix()
Bowl.mix()

#Add a dash of salt and flour in the bowl
Bowl.add(Salt.take('dash'))
for i in range(5):
    flour = Flour.take(grams=50)
    Bowl.add (flour)
    Bowl.mix()

#add the milk 
for i in range(2):
    milk = Milk.take(ml=250)
    Bowl.add (milk)
    Bowl.mix()
Bowl.mix()

Rosemary.taste(Bowl)

plate = Plate.use(name='pancakes')

#Cook the Pancakes!!!
pancakes_pan = Pan.use (name= 'pancakes')
for i in range(8):
    pancakes_pan.add(Butter.take('slice'))
    pancakes_pan.add(Bowl.take('1/8'))
    pancakes_pan.cook(minutes=1)
    pancakes_pan.flip
    pancakes_pan.cook(minutes=1)
    plate.add(pancakes_pan.take())

Rosemary.serve(plate)




