from sys import argv

script, first, second, third = argv
# script, first  = argv
# script, first, second, third, fourth = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

fourth = raw_input("type in some more\n")
print "Your fourth variable is:", fourth
