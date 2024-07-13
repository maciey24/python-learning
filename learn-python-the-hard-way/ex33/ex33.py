i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num

# study drills and experiments:


# 1. Convert this while- loop to a function that you can call, and replace 6 in the test (i < 6)
# with a variable.

def iterate_append(max):
    i = 0
    while i < max:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + 1
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

def iterate_append_with_step(max, step):
    i = 0
    while i < max:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + step
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

def iterate_append_with_step_and_range(max, step):
    for i in range(0, max, step):
        print "At the top i is %d" % i
        numbers.append(i)

        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

# 2. Now use this function to rewrite the script to try different numbers.
numbers = []
iterate_append(8)
numbers = []
iterate_append(10)

numbers = []
iterate_append_with_step(20, 5)

numbers = []
iterate_append_with_step_and_range(20, 5)

