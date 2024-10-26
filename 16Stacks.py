def create_stack():
    stack = []
    return stack

def is_empty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)

def pop(stack):
    if is_empty(stack):
        return None
    return stack.pop()

def peek(stack):
    if is_empty(stack):
        return None
    return stack[-1]

def size(stack):
    return len(stack)
