# module2.py

def add_str(*args, **kwargs):
    kwargs_list = ['%s=%s' % (k, kwargs[k]) for k in kwargs]
    print(''.join(args), ','.join(kwargs_list))

def add_num(*args, **kwargs):
    t = globals()['__builtins__'][kwargs['type']]
    print(sum(map(t, args)))
