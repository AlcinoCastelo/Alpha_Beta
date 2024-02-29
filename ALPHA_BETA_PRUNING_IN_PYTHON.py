tree = [[[1,2], [6,7]], [[1, 0], [11,5]]]
pruned = 0
def children(node, depth, alpha, beta):
    global pruned
    global tree
    for child in node:
        if isinstance(child, list):
            nalpha, nbeta = children(child, depth+1, alpha, beta)
            if depth %2 ==0:
                
                alpha = nbeta if nbeta > alpha else alpha
            if depth %2 ==1:
                #beta = nalpha is nalpha < beta else beta
                beta = nalpha if nalpha < beta else beta
        else:
            if depth %2 == 0 and child > alpha:
                alpha = child
            if depth %2 == 1 and child < beta:
                beta = child
            if alpha >= beta:
                pruned +=1
                break
    return alpha, beta
alpha, beta = children(tree, 0, -15, 15)
print("alpha:", alpha)
print("beta:", beta)
print("pruning:", pruned)
