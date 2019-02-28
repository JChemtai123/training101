# from Classesrev import Card
#
# card1 = Card(4500)
#
# print(card1.balance)
# print(card1.withdraw(3000))
#
# print(card1.balance)

from class_lib import Library

techcamplib = Library(bks=50, gen= ['comedy','drama','Fiction'], mems= ['Actely', 'Kiki','wells','Chemutai'])

print(techcamplib.books)
print(techcamplib.genre)
print(techcamplib.members)

techcamplib.lend()
print(techcamplib.books)