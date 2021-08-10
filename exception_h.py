# try
# whenever you fell that a part of program gives an error
# put the block of code inside try
# except will be the block of lines to output when the error occurs while runtime.
# try block is executed line by line! only after first line satisfies flow goes to next line

# except
# order of precedence of except matters
# when you dont want custion msg use: except Exception as e

# else
# if try does not raise an exception control flow goes to else
try:
    file = open('trial.txt')
    a = num
except FileNotFoundError as e:  # exception can be in many form.
    print(e)  # we get custom error instead of long lines!

except Exception as e:
    print(e)
