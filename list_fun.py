# For all the numbers between 1 and 100(including 100), # create a variable called answer, 
#which contains a list with all # the numbers that are divisible by 12.  (12, 24, etc)
# USE A LIST COMPREHENSION.

#create variable that contains a list from 1-100
my_nums = list(range(1,101))
#create variable that holds the answer of the numbers that are divisible by 12
answer = [num for num in my_nums if num % 12 == 0]
#print results
print(answer)