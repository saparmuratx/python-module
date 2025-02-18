
var = 11


def test():
    global var
    var = 0

    return var


print(test())
print(var)