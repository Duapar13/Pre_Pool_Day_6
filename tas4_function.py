# Add a new parameter to your previous function.
# It should provide the possibility to make a vegetarian sandwich (double vegetables and no ham).
# If this option is not specified, by default, the sandwich must be a lettuce-tomato-double ham
# one.

burger = input("Qu'elle burger : (viande) ou (végétarien)")

def bread () :
    print (" wwwwwwwwwwwwww ")
def lettuce () :
    print (" ~~~~~~~~~~~~ ")
def cheese () :
    print ('**************')
def tomato () :
    print ("O O O O O O")
def ham () :
    print (" ============ ")
def ham_vegetable () :
    print (" *_*_*_*_*_*_* ")



if burger == "viande":
    bread()
    lettuce()
    tomato()
    cheese()
    ham()
    bread()
elif burger == "végétarien":
# else:
    bread()
    lettuce()
    tomato()
    cheese()
    ham_vegetable()
    bread()