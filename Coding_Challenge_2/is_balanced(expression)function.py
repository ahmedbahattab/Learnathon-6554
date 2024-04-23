def is_balanced(expression):
    stack = []
    opening_brackets = {'(', '[', '{'}
    closing_brackets = {')', ']', '}'}
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}

    for char in expression:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            top = stack.pop()
            if bracket_pairs[top] != char:
                return False

    return len(stack) == 0

# Example usage:
print(is_balanced("{[()]}"))  # True
print(is_balanced("{[}]"))    # False
