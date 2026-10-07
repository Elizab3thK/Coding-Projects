import random
PASSWORD = "sraet"
WORD_LETTER_LIST = ["s", "r", "a", "e", "t"]
COUNTER = 0
def add(x,y):
   return x + y
def sub(x,y):
   return x - y
def multiply(x,y):
   return x * y
def divide(x,y):
   return x / y

def reveal(count):
   if (count == 1):
      return WORD_LETTER_LIST[0]
   elif(count == 2):
      return WORD_LETTER_LIST[1]
   elif (count == 3):
      return WORD_LETTER_LIST[2]
   elif (count == 4):
      return WORD_LETTER_LIST[3]
   elif (count == 5):
      return WORD_LETTER_LIST[4]

def Reveal_A_Letter():
   counter = 1
   while (counter < 6):
      num = int(input("Pick a number 1 to 12: "))
      x = random.randint(1, 50)
      y = random.randint(1, 10)
      if (num <= 3):
         addition = add(x,y)
         print(x, "+", y)
         answer = int(input("Enter your answer: "))
         if (answer == addition):
            print("Correct")
            print("The letter is...", reveal(counter))
            counter += 1
         else:
            print("try again")
      elif (num <= 6):
         print(x, "/", y)
         div = "{:.2f}".format(divide(x, y))
         division = div
         answer = input("Enter your answer(please put two decimals between the number): ")
         if (answer == division):
            print("Correct")
            print("The letter is...", reveal(counter))
            counter += 1
         else:
            print("try again")
      elif (num <= 9):
         multiplication = multiply(x,y)
         print(x, "*", y)
         answer = int(input("Enter your answer: "))
         if (answer == multiplication):
            print("Correct")
            print("The letter is...", reveal(counter))
            counter += 1
         else:
            print("try again")
      elif (num <= 12):
         subtraction = sub(x,y)
         print(x, "-", y)
         answer = int(input("Enter your answer:"))
         if (answer == subtraction):
            print("Correct")
            print("The letter is..." , reveal(counter))
            counter += 1
         else:
            print("try again")
      else:
         print("Sorry try again!")


if __name__ == '__main__':
   print("Welcome to Reveal A Letter")
   print("How to play: answer math problems correctly in order to reveal letters for the hidden code")
   print("You will have three chances to guess the correct order of the letters and win the game")
   print("Are you ready to play?")
   print("")
   Reveal_A_Letter()
   print("")
   print("Now that you have the letters")
   print("Time for you to guess the password")
   count = 3
   while(True):
      print("You have only ", count, "guesses")
      guess = input("Please enter the password: ")
      if (guess == PASSWORD):
         print("YEAHHHHH you won the game!!!!")
         break
      else:
         ("Try AGAIN!!!!!")
         count -= 1
      if (count == 0):
         print("Sorry you loss :(")
         print("The password was", PASSWORD)
         print("Better luck next time")
         break



