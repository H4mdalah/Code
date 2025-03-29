# Write code below 💖

gryffindor  = 0
ravenclaw   = 0
hufflepuff  = 0
slytherin   = 0 

question_1 = int(input("Do you like Dawn or Dusk? \n 1) Dawn \n 2) Dusk \n"))

if question_1 == 1:
  gryffindor = gryffindor + 1
  ravenclaw  = ravenclaw + 1
else:
  hufflepuff = hufflepuff + 1
  slytherin = slytherin + 1

print("The Score Now is : \n gyffindor  = ", gryffindor, "\n ravenclaw  = ", ravenclaw, "\n hufflepuff = ", hufflepuff, "\n slytherin  = ", slytherin )

question_2 = int(input("When I am dead, I want people to remember me as : \n 1) The Good \n 2) The Great \n 3) The Wise \n 4) The Bold \n"))

if question_2 == 1:
  hufflepuff = hufflepuff + 2
elif question_2 == 2:
  slytherin = slytherin + 2
elif question_2 == 3:
  ravenclaw = ravenclaw + 2
elif question_2 == 4:
  gryffindor = gryffindor + 2
else:
  print("Wrong Input")

print("The Score Now is : \n gyffindor  = ", gryffindor, "\n ravenclaw  = ", ravenclaw, "\n hufflepuff = ", hufflepuff, "\n slytherin  = ", slytherin )

question_3 = int(input("Which kind of instrument most pleases your ear : \n 1) The Violin \n 2) The trumpet \n 3) The Piano \n 4) The drum \n"))

if question_3 == 1:
  slytherin = slytherin + 4
elif question_3 == 2:
  hufflepuff = hufflepuff + 4
elif question_3 == 3:
  ravenclaw = ravenclaw + 4
elif question_3 == 4:
  gryffindor = gryffindor + 4
else:
  print("Wrong Input")

print("The Score Now is : \n gyffindor  = ", gryffindor, "\n ravenclaw  = ", ravenclaw, "\n hufflepuff = ", hufflepuff, "\n slytherin  = ", slytherin )

if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
  print("House With the most point is gryffindor with", gryffindor , "points")
elif ravenclaw >= gryffindor and ravenclaw >= hufflepuff and ravenclaw >= slytherin:
  print("House with the most point is ravenclaw with", ravenclaw , "points")
elif hufflepuff >= gryffindor and hufflepuff >= ravenclaw and hufflepuff >= slytherin:
  print("House with the most point is hufflepuff with", hufflepuff , "points")
elif slytherin >= gryffindor and slytherin >= ravenclaw and slytherin >= hufflepuff:
  print("House with the most point is slytherin with", slytherin , "points")
else:
  print("All Winners")


# To Do Make The ranking from number 1 to number 4