# Handling error is exception handling

try:
    print(5/0)
except Exception as e:
    print("Error")
    print(e)

"""
try:
       # Some Code.... 
except:
       # optional block
       # Handling of exception (if required)
else:
       # execute if no exception
finally:
      # Some code .....(always executed)
"""