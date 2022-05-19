def pipe(*args):
    if(len(args) > 1):
        *head, tail = args
        return tail(pipe(*head))

    return args[0] 

def sum_1(a, b):
    return a + b

def mult_2(a):
    return a * 2

ans = pipe([3, sum_1, mult_2])
print(ans)