
"""Implement tree abstraction and tree processing"""

"""Tree abstraction"""

def tree(label, branches = []):
    """Defines a tree"""
    
    for branch in branches:
        assert is_tree(branch)
    
    return [label] + list(branches)


def label(tree):
    """Returns the label of the tree"""
    
    return tree[0]


def branches(tree):
    """Returns the branches of the tree"""

    return tree[1:]

def is_tree(tree):
    """Checks if the argument qualifies to be a tree"""

    if type(tree) != list or len(tree) < 1:
        return False

    for branch in branches(tree):
        if not is_tree(branch):
            return False

    return True

def is_leaf(tree):
    """Checks if the tree passed is a leaf"""

    return not branches(tree)

"""Tree Processing"""

def fib_tree(n):
    """Create a fibbonaci tree"""

    if n<=1:
        return tree(n)

    else:
        left, right = fib_tree(n-2), fib_tree(n-1)
        return tree(label(left)+label(right), [left, right])


def leaf_count(t):
    """Counts the number of leaves in a tree"""

    if is_leaf(t):
        return 1
    else:
        branch_count = [leaf_count(b) for b in branches(t)]
        return sum(branch_count)

def leaves(t):
    """Returns a list containing the leaf labels of a tree"""

    if is_leaf(t):
        return [label(t)]
    else:
        return sum([leaves(b) for b in branches(t)],[])


def increment_leaves(t):
    """Increment all the leaves by 1 and return tree"""

    if is_leaf(t):
        return tree(label(t)+1)
    
    else:
        bs = [increment_leaves(b) for b in branches]
        return tree(label(t), bs] 

def increment(t):
    """Increment all the labels by 1"""
     
    return tree(label(t)+1, [increment(b) for b in branches(t)])

def print_tree(t, indent = 0):
    """Print a tree"""
    
    print(' ' * indent + str(label(t)) ) 
    for b in branches:
        print_tree(b, indent+1)
