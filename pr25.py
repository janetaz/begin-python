#!usr/bin/env python3
#
#Binary Search
#
#I'd like to know how this works with odd, even lists
#
#Need: force int, upper, lower bound, ability to go too low, too high alternatingly. 
#int hold?
#https://en.wikipedia.org/wiki/Binary_search_algorithm
#^ talks about upper bound
#1. Set L to 0 and R to n − 1.
#2. If L > R, the search terminates as unsuccessful.
#3. Set m (the position of the middle element) to the floor (the largest previous integer) of (L + R) / 2.
#4. If Am < T, set L to m + 1 and go to step 2.
#5. If Am > T, set R to m − 1 and go to step 2.
#6. Now Am = T, the search is done; return m.
#
#_____________________________

count = 0
rng = [x for x in range(0,101)] #cleaner way?
#midlength = int((len(rng) - 1) / 2)  #largest previous int of (L+R)/2?
L = 0
R = len(rng) - 1
print ("Let's begin!")

while True:
    count += 1
    response = input("Is it " + str(midlength) + "?: ").lower() #place for %s?
    if response == 'yes':
        print ("Whoo! I'm so good! I guessed it in " + str(count) + " tries.")
        break
    elif response == 'too high':
        R = rng[midlength]
        midlength = midlength / 2
    elif response == 'too low':
        
        midlength = midlength + midlength / 2 # i can end w/ elif, ya?
        
        
        
    

