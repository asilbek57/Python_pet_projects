

## Questions:
# 
# 1. <a href="https://pynative.com/python-if-else-and-for-loop-quiz/">Loops quiz</a>
# 2.  What is the difference between the continue and break statements in Python?
# 3. Can you explain the difference between for loop and while loop?
# 4. How would you implement a nested for loop system? Provide an example.

# 2) continue is used in order to skip a specific element from a container and moves on to the next one, without stopping the process of a loop
# break, on the other hand, is used to stop the entire loop 
# 3) for loop enables to take every element from a list, dictionary or set and repeat it certain amount of times, so that it would be easy to take actions over elements faster and easier. while loop enables to repeat an element as long as the condition given by us stays True and breaks when the condition becomes False.
# 4) I can implement it and create a table of multiplication from math:
#     for i in range(1,11):
#         for n in range(1,11):
#             print(i*n, end = ", ")
#     print()
# 
# here I have two main bodies : first is outer loop and the second is the inner(nested) loop
# 

# ## Homeworks:
# 
# **1.** Return uncommon elements of lists. Order of elements does not matter.
# 
# input:
#     list1 = [1, 1, 2]
#     list2 = [2, 3, 4]
# output: [1, 1, 3, 4]
# 
# 
# 
# input:
#     list1 = [1, 2, 3]
#     list2 = [4, 5, 6]
# output: [1, 2, 3, 4, 5, 6]
# 
# 
# 
# input:
#     list1 = [1, 1, 2, 3, 4, 2]
#     list2 = [1, 3, 4, 5]
# output: [2, 2, 5]
# 
# 
# **2.** Print the square of each number which is less than `n` on a separate line.
# 
# input: n = 5
# output:
#     1
#     4
#     9
#     16
# 
# 
# 
# **3.** `txt` nomli string saqlovchi o'zgaruvchi berilgan. `txt`dagi har uchinchi belgidan keyin pastgi chiziqcha (underscore) qo'yilsin. Agar belgi unli harf yoki orqasidan ostki chiziqcha qo'yilgan harf bo'lsa, ostki chiziqcha keyingi harfdan keyin qo'yilsin. Agar belgi satrdagi oxirgi belgi bo'lsa chiziqcha qo'yilmasin.
# 
# input: hello
# output: hel_lo
# 
# input: assalom
# output: ass_alom
# 
# input: abcabcdabcdeabcdefabcdefg
# output: abc_abcd_abcdeab_cdef_abcdefg
# 

# In[ ]:


#Q1
from collections import Counter
list1 = [1,1,2]
list2 = [2,3,4]
c1 = Counter(list1)
c2 = Counter(list2)
uncommon = list((c1 - c2).elements()) + list((c2-c1).elements())
print(uncommon)


list1 = [1,2,3]
list2 = [4,5,6]
united = set(list1) | set(list2)
print(united)




from collections import Counter
list1 = [1,1,2,3,4,2]
list2 = [1,3,4,5]
set1 = set(list1)
set2 = set(list2)
part1 = []
for x in list1:
    if x not in set2:
        part1.append(x)
part2 = []
for x in list2:
    if x not in set1:
        part2.append(x)

print(part1 + part2)



n = 5
for i in range(n):
    print(i**2)







# **4. Number Guessing Game**
# Create a simple number guessing game.
# - The computer randomly selects a number between 1 and 100. 
# - If the guess is high, print "Too high!". 
# - If the guess is low, print "Too low!". 
# - If they guess correctly, print "You guessed it right!" and exit the loop.
# - The player has 10 attempts to guess it. If the player can not find the correct number in 10 attempts, print "You lost. Want to play again? ".
# - If the player types one of 'Y', 'YES', 'y', 'yes', 'ok' then start the game from the beginning.
# 
# 
# > Hint: Use Python’s `random.randint()` to generate the number.
# 
# **5. Password Checker**
# Task: Create a simple password checker.
# - Ask the user to enter a password. 
# - If the password is shorter than 8 characters, print "Password is too short." 
# - If the password doesn’t contain at least one uppercase letter, print "Password must contain an uppercase letter.". 
# - If the password meets both criteria, print "Password is strong."
# 
# **6. Prime Numbers**
# Task: Write a Python program that prints all prime numbers between 1 and 100.
# 
# > A prime number is a number greater than 1 that is not divisible by any number other than 1 and itself. Use nested loops to check divisibility.
# 
# ---
# 
# ### Bonus Challenge
# Task: Create a simple text-based Rock, Paper, Scissors game where the player plays against the computer.
# - The computer randomly chooses `rock`, `paper`, or `scissors` using `random.choice()`.
# - The player enters their choice.
# - Display the winner and keep track of scores for the player and the computer.
# - First to 5 points wins the match.

# In[ ]:


#Q4
import random


play_again = True
while play_again:
    number = random.randint(1,100)
    n = 0
    while n <= 10:
        i = int(input("Enter a number between 1 and a 100: "))
        print(i)
        if i > number:
            print("Too high!")
        elif i < number:
            print("Too Low!")
        elif i == number:
            print("You guessed correctly!")
            play_again = False
            break
        n += 1 
        
    else:
        losing = input("You lost, wanna play again? ")
        print(losing)
        if losing == 'Yes':
            play_again = True
        else:
            play_again = False
    








#Q5
p = input("Enter a password: ")

if not any(char.isupper() for char in p):
    print("Password must contain an uppercase letter.")
elif len(p) < 8:
    print("Password is too short")
else:
    print("Password is strong")



#Q6
for n in range(2,100):
    prime = True
    for i in range(2, n):
        if n%i == 0 :
            prime = False
            break
    if prime:
        print(n)
            
        





