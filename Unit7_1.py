def solve(lst):
    st = []
    z = 0
    for i in lst:
        if i.isdigit():
            st.append(int(i))
            continue
#    print(st)
    for j in lst:
        if not j.isdigit():
            z = j
#    print(z)
    y = st.pop()
    x = st.pop()
    n = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x // y
    }[z](x, y)
    return n


lst = input('Enter expression:').split()
print(solve(lst))