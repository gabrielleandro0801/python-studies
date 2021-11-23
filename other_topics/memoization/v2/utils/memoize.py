class Memoize:

    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        if args not in self.memo:
            print(f'Return from function {self.fn.__name__}() not in cache, executing now with args {list(args)}')
            self.memo[args] = self.fn(*args)
        return self.memo[args]
