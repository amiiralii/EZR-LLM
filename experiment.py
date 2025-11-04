from operator import truediv
from ezr import *
from stats import *


filename = "moot/coc1000.csv"
data = Data(csv(filename))
half = len(data.rows)//2

for r in range(10):
    random.seed = r
    the.seed = r
    data.rows = shuffle(data.rows)
    train, holdout = data.rows[:half], data.rows[half:]

    b4   = adds(disty(data,row) for row in data.rows)
    win  = lambda v: int(100*(1 - (v - b4.lo)/(b4.mu - b4.lo)))
    best = lambda rows: win(disty(data, distysort(data,rows)[0]))
    best_row = lambda rows: distysort(data,rows)[0]
    d2hs = [disty(data,row) for row in data.rows]
    stp = 50
    the.Budget = stp
    labels = likely(clone(data, train))
    tree = Tree(clone(data, labels))
    treeShow(data, tree, win)
    holdouts = sorted(holdout, key=lambda row: treeLeaf(tree,row).mu)[:the.Check]
    best_holdout = best(holdouts)
    best_holdout_row = best_row(holdouts)
    print(best_holdout, best_holdout_row)

    print("Random:")
    a = random.choice(holdout)
    print(win(disty(data,a)), a)

    print("Best LLM Answer:")
    a = [689,5,2,3,2,3,2,5,3,5,5,4,4,5,4,3,3,3,2,6,6,4,4,0,3323]
    print(win(disty(data,a)), a)
    
    input("-----")
    sorted_holdout = sorted(holdout, key= lambda x: disty(data,x))
    for sh in sorted_holdout:
        print(f"{disty(data,sh):.2f}, {sh}")
