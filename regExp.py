import re

regExp = '[0-9a-zA-z][_0-9a-zA-Z-]*@[0-9a-zA-Z-]+(\.[_0-9a-zA-Z-]+){1,2}$'

email = 'abc@abc.com'
email2 = 'abc@abc.c'

print(bool(re.search(regExp,email)))
print(bool(re.search(regExp,email2)))