from operator import truediv
from ezr import *
from stats import *


filename = "moot/coc1000.csv"
data = Data(csv(filename))
# half = len(da
half = 200
# data.rows = shuffle(data.rows)
train, holdout = data.rows[:half], data.rows[half:half+50]

b4   = adds(disty(data,row) for row in data.rows)
win  = lambda v: int(100*(1 - (v - b4.lo)/(b4.mu - b4.lo)))
best = lambda rows: win(disty(data, distysort(data,rows)[0]))
best_row = lambda rows: distysort(data,rows)[0]
d2hs = [disty(data,row) for row in data.rows]
stp = 50
the.Budget = stp
labels = likely(clone(data, train))
# labels = train
tree = Tree(clone(data, labels))
treeShow(data, tree, win)
holdouts = sorted(holdout, key=lambda row: treeLeaf(tree,row).mu)[:the.Check]
best_holdout = best(holdouts)
best_holdout_row = best_row(holdouts)
print(best_holdout, best_holdout_row)
print("Best LLM Answer:")
a = holdout[47]
print(win(disty(data,a)), a)
print("-----")
sorted_holdout = sorted(holdout, key= lambda x: disty(data,x))
for sh in sorted_holdout:
    print(f"{disty(data,sh):.2f}, {sh}")
