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
# we can use else content in try, but inorder to be specific about the error we dont

# finally
# it runs even if there is an exception

# raise is usedd to manually create an exception
from os import error


try:
    file = open('trial.txt')
    #a = num
    if file.name == "trial.txt":
        raise Exception

except FileNotFoundError as e:  # exception can be in many form.
    print(e)  # we get custom error instead of long lines!

except Exception:
    print("error")

except Exception as e:
    print(e)

else:
    print(file.read())
    file.close()

finally:
    print("------Done---------")
