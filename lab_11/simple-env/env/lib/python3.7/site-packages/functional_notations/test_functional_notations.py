from .functional_notations import _F, F

def test__F():
    A = _F(lambda x: x)
    try:
        print(1 @ A)
    except NotImplementedError:
        print('left @ is not implemented by design')
    A @= 1
    print("A = ", A)


    # Examples
    @_F
    def mul(x):
        return x * 2


    def some_fn(a, b):
        a + b


    A = F(lambda x: x)
    A @= 1
    print("A = ", A)

    print(F)
    print(F @ some_fn)
    print(F @ 1)

    mul @ [1]
    mul @ 5

    import numpy as np

    # Applying a function to an array
    _F(lambda x: 2 + x) @ np.array([0, 3, 2, 1])
    # Alternatively
    F @ (lambda x: [2 * _ for _ in x]) @ [3, 1, 2, 4]
    # Or Alternatively
    F(lambda *x: 2 * x) @ [3, 1, 2, 4]

    add = lambda x: x + 1
    pow = lambda x: x ** 3

    print(F)
    # function composition:
    print(F @ add)
    print(F @ mul)
    print(F @ add @ 10)
    # from the left to the right
    print(F @ add @ mul @ 10)
    # print((F @ add @ mul @ 10) + 1)

    print(_F(add) @ 1)
    F @ list @ (lambda x: [_ * 2 for _ in x]) @ [1, 2, 3, 4]
    # Out[15]: [2, 4, 6, 8]

    # This is currently not working
    F @ list @ (lambda fn: map(fn, [1, 2, 3, 4])) @ (lambda x: x + 1)

    # This works
    print(F @ list @ (lambda xs: [x + 1 for x in xs]) @ [1, 2, 3, 4])
