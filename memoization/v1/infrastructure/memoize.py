def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            print(f'Return from function {f.__name__}() not in cache, executing now with args [{x}]')
            memo[x] = f(x)
        return memo[x]

    return helper
