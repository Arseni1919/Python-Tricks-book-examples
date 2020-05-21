import datetime
print(dir(datetime))
print([_ for _ in dir(datetime) if 'date' in _.lower()])
print(help(datetime))