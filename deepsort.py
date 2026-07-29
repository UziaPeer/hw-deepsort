def deep_sorted(x:any)->str:
   def key(v):
        if isinstance(v, dict):
            return (3, [(key(k), key(v[k])) for k in sorted(v, key=key)])
        if isinstance(v, (list, tuple)):
            return (2, [key(i) for i in v])
        if isinstance(v, set):
            return (1, sorted(key(i) for i in v))
        return (0, v)


    if isinstance(x, dict):
        return "{" + ", ".join(f"{deep_sorted(k)}: {deep_sorted(x[k])}" for k in sorted(x, key=key)) + "}"
    if isinstance(x, list):
        return "[" + ", ".join(deep_sorted(i) for i in sorted(x, key=key)) + "]"
    if isinstance(x, tuple):
        items = [deep_sorted(i) for i in sorted(x, key=key)]
        return "(" + ", ".join(items) + ("," if len(items) == 1 else "") + ")"
    if isinstance(x, set):
        if not x:
            return "set()"
        return "{" + ", ".join(deep_sorted(i) for i in sorted(x, key=key)) + "}"
    return repr(x)


if __name__ == '__main__':
    # x=eval(input())
    # print(deep_sorted(x))
    import doctest
    print (doctest.testmod())
