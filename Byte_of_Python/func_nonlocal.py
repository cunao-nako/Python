def func_outer():
    x = 5
    print('x равно', x)

    def func_inner():
        nonlocal x
        x = 10
    func_inner()
    print('Локальное x сменилось на', x)
func_outer()