print("Conservatory Of Flowers: A super fun true or false quiz! \ncreated by CK'23)

def function(score):
  y= input("true or false? ")
  print (y)
  if y == ("true"):
    print ("yay u got it correct")
    score=score+1

  else:
    print ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx incorecto xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    score=score-1

  return score

def false(score):
  y= input("true or false? ")
  print (y)
  if y == ("false"):
    print ("yay u got it correct")
    score=score+1

  else:
    print ("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx incorecto xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    score=score-1

  return score

score=0

#write this when calling function
#function()

statement= ("Hi there! Do you want to play this game?")
print (statement)

x= input("Yes or No?")
print (x)
if x == ("yes") or x==("Yes"):
  print ("cool let's get started! CoUNtdOwN")

else:
  print ("wrong answer you're going to play anyways!CoUNtdOwN")

for x in range (1,6):
  print (6-x)

print ("\n")

question1= ("PROBLEM 1: Carnivorous plants gets nutrients by trapping and digesting insects and small insects")
print (question1)

score = function(score)
print (score)

print ("\n")

question2= ("PROBLEM 2: A rain forest is a tropical forest near mountains that is usually covered in clouds")
print (question2)

score = false(score)
print (score)

print ("\n")

question3= ("PROBLEM 3: The conditions that surround plants, animals, and people, including weather, soil, and light is called an environment")
print (question3)

score = function(score)
print (score)

print ("\n")

question4= ("PROBLEM 4: A plant that grows on other plants is called an epiphyte")
print (question4)

score = function(score)
print (score)

print ("\n")

question5= ("PROBLEM 5: The amount of water vapor in the air is called condensation")
print (question5)

score = false(score)
print (score)

print ("\n")

middle= ("Congrats you made it halfway!")
print (middle)
count= 0
while count <6:
  print (count)
  count=count+1

else:
  print ("Let's go!")

print ("\n")

question6= ("PROBLEM 6:  A pseudobulb is the part of some orchids that stores water")
print (question6)

score = function(score)
print (score)

print ("\n")

question7= ("PROBLEM 7:  What manufactures food energy through the process of photosynthesis: fertilizer")
print (question7)

score = false(score)
print (score)

print ("\n")

question8= ("PROBLEM 8:  Air is what is usually taken up through the roots and helps the plant move nutrients throughout the plant")
print (question8)

score = function(score)
print (score)

print ("\n")

question9= ("PROBLEM 9: What from the soil and decaying plants and insects are absorbed through the roots and help the plant grow strong: nutrients")
print (question9)

score = function(score)
print (score)

print ("\n")

question10= ("PROBLEM 10: An imaginary line around the center of the earth that divides the Northern and Southern Hemispheres is called the equilateral")
print (question10)

score = false(score)
print (score)

print ("\n")

finish= ("Yay Congrats you finished the quiz!")
print (finish)

print ("total number of points")
print (str(score)+(" out of 10"))
