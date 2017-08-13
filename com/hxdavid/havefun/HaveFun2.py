from mpmath import mp


def my_annotation(f):
    def wrapper():
        print("Wrap start")
        f()
        print("Wrap end")

    return wrapper


def my_annotation2(f):
    def wrapper():
        print("Wrap start 2")
        f()
        print("Wrap end 2")

    return wrapper


@my_annotation
@my_annotation2
def run():
    mp.dps = 2000
    ds = str(mp.pi)
    ds = ds[0] + ds[2:]
    ans = [0 for i in range(10)]
    for s in ds:
        ans[int(s)] += 1  # It is much faster, don't use lambda expression to reduce algorithm complexity.
    print(ans)


def avg(l):
    return sum(l) / float(len(l))


run()
# if __name__ == '__main__':
#     print(avg(Timer("run()", "from functools import reduce\n"
#                              "from timeit import timeit\n"
#                              "from mpmath import mp\n"
#                              "from __main__ import run").repeat(5, 20)))
