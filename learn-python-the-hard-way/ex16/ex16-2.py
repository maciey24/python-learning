from sys import argv

script, filename = argv

testFile = open(filename)
testFileContent = testFile.read()

print testFile
testFile.close()
print testFile

print testFileContent

