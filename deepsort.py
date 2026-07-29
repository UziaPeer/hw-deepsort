def deep_sorted(x:any)->str:
    if isinstance(x, dict):
        return "{" + ", ".join(repr(k) + ": " + deep_sorted(x[k]) for k in sorted(x)) + "}"
    if isinstance(x, list):
        return "[" + ", ".join(sorted(deep_sorted(i) for i in x)) + "]"
    if isinstance(x, tuple):
        return "(" + ", ".join(sorted(deep_sorted(i) for i in x)) + ")"
    if isinstance(x, set):
        return "{" + ", ".join(sorted(deep_sorted(i) for i in x)) + "}"
    return str(x)


if __name__ == '__main__':
    # x=eval(input())
    # print(deep_sorted(x))
    import doctest
    print(doctest.testmod())
