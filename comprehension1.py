sarah_fav_stuff = [17, 'Sophia', 46.7, 'piano', 'April 21, 2023']

# collect all the string values in 'stuff'
strs = [strings for strings in sarah_fav_stuff if isinstance(strings, str)]

print(strs)
# collect all the number values in 'sarah_fav_stuff'
# nums = [num for num in sarah_fav_stuff if not isinstance(num, str)]
nums = [n for n in sarah_fav_stuff if isinstance(n, (int, float))]
print(nums)
