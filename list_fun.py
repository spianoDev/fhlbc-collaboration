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
def sum_no_duplicates(l):
    new_list = []
    sum = 0
    if len(l) == 0:
        return sum
    elif l[0] == l[1]:
        l = list(filter((l[0]).__ne__, l))

    for num in l:
        print('first list', l)
        print('new list',new_list)
        if num not in new_list:
            new_list.append(num)
        else:
            new_list = list(filter((num).__ne__, new_list))
            l = list(filter((num).__ne__, l))
        
    
    for num in new_list:
        sum += num

    return sum

# print(sum_no_duplicates([3, 4, 3, 6])) #10
# print(sum_no_duplicates([1, 1, 2, 3])) #5
print(sum_no_duplicates([1, 1, 2, 3,1])) #5
# print(sum_no_duplicates([1, 1, 2, 3, 1, 1])) #5