# whenever you fell that a part of program gives an error
# put the block of code inside try
# except will be the block of lines to output when the error occurs while runtime.
# try block is executed line by line! only after first line satisfies flow goes to next line


# order of precedence of except matters
try:
    file = open('trial.txt')
    a = num
except FileNotFoundError:  # exception can be in many form.
    print("file not found!")  # we get custom error instead of long lines!

except Exception:
    print("wrong variable declaration")
