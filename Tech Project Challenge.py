q = open("test_qs.txt" , "r")
a = open("test_ans.txt", "r")

Ans1 = "b", "B"
Ans2 = "c", "C"
Ans3 = "a", "A"
Ans4 = "d", "D"
Ans5 = "b", "B"

score = 0

Title = "SUPER HARD GENERAL KNOWLEDGE QUIZ!\n(no seriously its so hard that you may have to use GOOGLE)"

good = "Well done, you're really smart. Now onto the next question."
bad = "Well, you're wrong. Hopefully you get something else right"
caps = "Don't use caps pls. That counts as a wrong answer because I cba to add caps to the code"


# AU(number) is the user's answers

print(Title)
print("")
print("You don't have to use capitals while answering, btw.")

print(q.read())

AU1 = str(input(""))

if AU1 == Ans1:
  score += 1
  print(good)
elif AU1 == "B":
  score = score
  print(caps)
else:
  score = score
  print(bad)

AU2 = str(input(""))

if AU2 == Ans2:
  score += 1
  print(good)
elif AU2 == "C":
  score = score
  print(caps)
else:
  score = score
  print(bad)

AU3 = str(input(""))

if AU3 == Ans3:
  score += 1
  print(good)
elif AU3 == "A":
  score = score
  print(caps)
else:
  score = score
  print(bad)

AU4 = str(input(""))

if AU4 == Ans4:
  score += 1
  print(good)
elif AU4 == "D":
  score = score
  print(caps)
else:
  score = score
  print(bad)

AU5 = str(input(""))

if AU5 == Ans5:
  score += 1
  print("Well done")
elif AU5 == "B":
  score = score
  print(caps)
else:
  score = score
  print("That was your last chance.")

print('''
---THE QUIZ IS OVER---''')

print("\nYour score: " + str(score) + "/5")

q.close()
a.close()

quit