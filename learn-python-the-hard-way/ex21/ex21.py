def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b


def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b


def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b


def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b


def formula(age, height, weight, iq):
    return age + height - iq / 2 * weight


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
what_calculated_with_formula = formula(age, height, weight, iq)

print "That becomes: ", what, "Can you do it by hand?"
print "What calculated with formula:", what_calculated_with_formula

a = 2
b = 3
c = 4
simple_formula_result = b ** 2 - 4 * a * c
print "delta =", simple_formula_result
delta = subtract(multiply(b, b), multiply(multiply(4, a), c))
print "delta =", delta
