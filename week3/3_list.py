# a_list = []
# The list has no elements, so we cannot index them.
a_list = [0] * 5

# count = 0
# while count < 5:
# Make it work with lists of any size.
for count in range(len(a_list)):
    a_list[count] = count
    count = count + 1

print(a_list)
