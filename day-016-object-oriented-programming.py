"""
At some point in the project, you will may have coded a ton of lines and tons of functions, each of them related to one another.
Bascially your code tries to do a lot of things, and manage a whole bunch of relationships. And because of that, at some point your code become very spaghetti-looking-like.
Annd at this point it's very hard to keep track and remember whatever is going on inside your code.
This style of programming called Procedural Programming. Where we set up procedures or functions that do particular things. And one procedure leads to another, all in all from top to bottom.
Procedual Programming is the most easiest paradigms of Programming. But it's lack the ability to be comprehensive for the big picture, the complexity, and as our programs grow, it will get very confusing.
To write and grow more and more complex projects we need to use the OOP or Object Oriented Programming.
"""

from turtle import Turtle, Screen
from prettytable import PrettyTable

tommy = Turtle()
tommy.shape('turtle')
tommy.color('red')
# print(tommy.forward(100))

my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

pokemons = PrettyTable()
pokemons.add_column("Pokemon Name", ["Pikachu", "Raychu", "Charmander"])
pokemons.add_column("Type", ["Elec", "Elec", "Fire"])
print(pokemons)
