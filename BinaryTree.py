
# node OP (T) (T) donde T puede ser lo mismo que escribi primero o "Leaf D" siendo D un numero
# OP = sum | res | div | mul
#
# Ejemplo:
#       Node MUL (node sum (Leaf 49) (Leaf 104)) (Leaf 38)
#

from JLolibrary import Node

simbols = {
    'SUM': '+',
    'RES': '-',
    'MUL': 'x',
    'DIV': '÷'
}

def createNode(line):
    parent = Node(simbols[line[5:8].upper()])
    left_start = line.index('(')
    left_end = left_start
    left_stack = []
    for c in line[left_start: ]:
        if c == '(':
            left_stack.append(1)
        elif c == ')':
            left_stack.pop()
        if len(left_stack) == 0:
            break
        left_end += 1
    if(line[left_start + 1 : left_start + 5] == 'Leaf'):
        parent.left = Node(int(line[left_start + 6 : left_end]))

    else:
        parent.left = createNode(line[left_start + 1 : left_end])


    right_start = line.index('(', left_end)
    right_end = right_start

    right_stack = []
    for c in line[right_start: ]:

        if c == '(':
            right_stack.append(1)
        elif c == ')':
            right_stack.pop()


        if len(right_stack) == 0:
            break
        right_end += 1
    
    if(line[right_start + 1 : right_start + 5] == 'Leaf'):
        parent.right = Node(line[right_start + 6 : right_end])

    else:
        parent.right = createNode(line[right_start + 1 : right_end])
    # print("(%s, %s)" % (left_start, left_end), '(%s, %s)' % (right_start, right_end))
    # print(root, '|', line[left_start + 1 : left_end], '|', line[right_start + 1 : right_end])
    return parent



if __name__ == '__main__':
    
    
    #line = "Node MUL (node SUM (Leaf 49) (Leaf 104)) (Leaf 38)"
    line = "Node MUL (Node SUM (Node DIV (Leaf 16) (Leaf 4)) (Leaf 5)) (Node RES (Leaf 3) (Leaf 5))"

    print(line)

    tree = createNode(line)
    print(tree)





