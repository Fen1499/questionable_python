import sys
import glob

def snake_to_camel(st):
    camel = st[0].upper() + st[1:]
    return "".join(camel)

def case(path):
    with open(path, "r") as f:
        file_in = f.read()
    pieces = file_in.split("_")
    if len(pieces) > 1:
        file_out = pieces[0] + "".join([snake_to_camel(p) for p in pieces[1:]])
        with open(path, "w") as f:
            f.write(file_out)
        return path.split('/')[-1]
    else:
        return None


for f in glob.glob(f"{sys.argv[1]}"):
    print(case(f))



