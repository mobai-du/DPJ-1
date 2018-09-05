def range2(n):

    count = 0
    while count < n :
        print(count)
        count += 1
        yield  count #return

print(range2(10))
f = range2(10)
next(f)
f.__next__()