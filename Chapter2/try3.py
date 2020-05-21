errno = 50159747054
name = 'Bob'

print('Hey %(name)s, there is a 0x%(errno)x error!' % {
    "name": name,
    "errno": errno
})

print('Hey {name}, there is a 0x{errno:x} error!'.format(
    name=name,
    errno=errno)
)

print(f'Hello, {name}!')

print(f"Hey {name}, there's a {errno:#x} error!")

from string import Template
templ_string = 'Hey $name, there\'s a $error error!'
print(Template(templ_string).substitute(name=name, error=hex(errno)))