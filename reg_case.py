import sys
import re

def snake_to_camel(m):
    aux = m.group().split('_')
    result = aux[0] + ''.join([a.title() for a in aux[1:]])
    print(m.group(), '=>', result)
    return result

with open(sys.argv[1], 'r') as f:
    file_open = f.read()

file_out = re.sub(r'"\w+_\w+"', snake_to_camel, file_open)
with open(sys.argv[1], 'w') as f:
    f.write(file_out)
