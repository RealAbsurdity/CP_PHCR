# make a list of values
values = [1, 2, 3, 4]

# square each number in values and return the sum of the squared values:
value = 0
for number in values:
    value += number * number

print(value)


# this is the same when using the ** exponent operator:
value2 = 0
for number in values:
    value2 += number**2

print(value2)


# we can also use list comprehension to create a list of squared values:
sqValues = [number**2 for number in values]
# number squared from each number in the values list will be placed in a new list
print(sqValues)

# sum() can then add all of the sqValues[] list like this:
value3 = sum(sqValues)
print(value3)


# or we can use list comprehension inside sum() like this:
value4 = sum(sample**2 for sample in values)
print(value4)