# For all the numbers between 1 and 100(including 100), # create a variable called answer, 
#which contains a list with all # the numbers that are divisible by 12.  (12, 24, etc)
# USE A LIST COMPREHENSION.

#create variable that contains a list from 1-100
my_nums = list(range(1,101))
#create variable that holds the answer of the numbers that are divisible by 12
answer = [num for num in my_nums if num % 12 == 0]
#print results
#print(answer)

#Sum the list but ignore the duplicates
#Please write a function that sums a list, but ignores any duplicate items in the list.
#For instance, for the list [3, 4, 3, 6] , the function should return 10.
def sum_no_duplicates(first_list):
    #create empty list to store none duplicates
    new_list = []
    #create variable to hold sum of none duplicate numbers
    sum = 0

    for num in first_list:
        #use count to count the number of times the value appears in the first_list
        if first_list.count(num) < 2:
            #if num has less than 2 occurrences, add to new list
            new_list.append(num)

    #go through each item in list and add them together in the sum variable
    for num in new_list:
        sum += num

    return sum

print(sum_no_duplicates([3, 4, 3, 6])) #10
print(sum_no_duplicates([1, 1, 2, 3])) #5
print(sum_no_duplicates([1, 1, 2, 3,1])) #5
print(sum_no_duplicates([1, 1, 2, 3, 1, 2])) #3