# whenever you fell that a part of program gives an error
# put the block of code inside try
# except will be the block of lines to output when the error occurs while runtime.
try:
    file = open('name.txt')
except Exception:
    print("file not found!")
