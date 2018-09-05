def fib(max):
    n, a, b = 0, 0, 1
    while n< max:
        print("before yield")
        yield b #把函数的执行过程冻结在这一步，并且把b的值，返回给外面
        # print(b)
        a, b = b, a+b
        n = n + 1

    return 'done'

print(fib(10))
f = fib(10)
# f = fib(10)
#
# for i in f:
#     print(i)

print(next(f))
# print(next(f))
# print(next(f))
# print(next(f))