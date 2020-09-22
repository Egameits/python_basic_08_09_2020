# result = []

# for itm in range(10):
   # if itm & 1:
      # result.append(itm)

# print(result)


# result2 = [(itm, n, m) for itm in range(10) for itm in range(10) for n in range(10, 20) for m in range(50, 100)]
# print(result2)


# t_tup = tuple((itm, n, m) for itm in range(10) for itm in range(10) for n in range(10, 20) for m in range(50, 100))
# print(t_tup)


# def my_map(func, iter_object):
    # for itm in iter_object:
        # yield func(itm)


# def some(x):
    # yield x - 2
    # yield x - 3
   # yield x - 4


# tmp = my_map(lambda x: x**2, range(10))

# for itm in tmp:
    # print(itm)

# while True:
    # try:
        # itm = next(tmp)
        # print(itm)
    # except StopIteration:
        # break



import statistics as stat
a = [itm for itm in range(2, 500) if itm & 1]

def statistics():
    return 0

print(stat.mean(a))
