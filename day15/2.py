D, M = open('in.txt').read().split('\n\n')

def move(p, d):
    p += d
    if all([
        G[p] != '[' or move(p+1, d) and move(p, d),
        G[p] != ']' or move(p-1, d) and move(p, d),
        G[p] != 'O' or move(p, d), G[p] != '#']):
            G[p], G[p-d] = G[p-d], G[p]
            return True


for D in D, D.translate(str.maketrans(
        {'#':'##', '.':'..', 'O':'[]', '@':'@.'})):

    G = {i+j*1j: c for j, r in enumerate(D.split())
                   for i, c in enumerate(r)}
    pos, = [p for p in G if G[p] == '@']

    for m in M.replace('\n', ''):
        C = G.copy()
        dir = {'<':-1, '>':+1, '^':-1j, 'v':+1j}[m]

        if move(pos, dir): pos += dir
        else: G = C

    ans = sum(pos for pos in G if G[pos] in 'O[')
    print(int(ans.real + ans.imag*100))
