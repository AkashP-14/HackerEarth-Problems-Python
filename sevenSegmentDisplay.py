# Remember input number could be anything and not just from 0-9! 
# This means: if Alice gets number: 3, she will have 5 matches. But, if she gets a number say: 10, she will have a total of 8 matches.


segment = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]                     # Initial Segment Values.

for i in range(int(input())):                                # No. of test_cases

   no_matches = sum((segment[int(i)] for i in input()))      # Calculating total number of matches available.

   if(no_matches % 2 == 0):
       print('1' * (no_matches//2))

   else:  
       print('7', end='')                                    # '7' is largest number, with smallest matches requirement.
       print('1' * (no_matches//2 - 1))