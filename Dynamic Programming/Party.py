class Emplyee:
    def __init__(self, fun):
        self.emp = []
        self.fun = fun
        self.f = -1
        self.g = -1

def f(v):
    if v.f >= 0:
        return v.f
    x = v.fun
    for u in v.emp:
        x += g(u)
    y = g(v)
    v.f = max(x,y)
    return v.f

def g(v):
    if v.g >=0:
        return v.g
    v.g = 0
    for u in v.emp:
        v.g += f(u)
    return v.g