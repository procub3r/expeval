# These are the only operators supported right now.
# They are ordered as per their precedence, and
# operators of equal precedence are in a nested list.
operators = [['**'], ['*', '/', '%'], ['+', '-']]

# Operation functions.
# ops is a tuple ((x1, y1), (x2, y2)) where:
#   x is the index in expr where the operand starts
#   and y is the index in expr where the operand ends.
#   x1, y1 correspond to the first operand whereas
#   x2, y2 corresond to the second operand.
def exp_func(expr, ops):
    return str(float(expr[ops[0][0]:ops[0][1]]) ** float(expr[ops[1][0]:ops[1][1]]))

def mult_func(expr, ops):
    return str(float(expr[ops[0][0]:ops[0][1]]) * float(expr[ops[1][0]:ops[1][1]]))

def div_func(expr, ops):
    return str(float(expr[ops[0][0]:ops[0][1]]) / float(expr[ops[1][0]:ops[1][1]]))

def mod_func(expr, ops):
    return str(float(expr[ops[0][0]:ops[0][1]]) % float(expr[ops[1][0]:ops[1][1]]))

def add_func(expr, ops):
    return str(float(expr[ops[0][0]:ops[0][1]]) + float(expr[ops[1][0]:ops[1][1]]))

def sub_func(expr, ops):
    return str(float(expr[ops[0][0]:ops[0][1]]) - float(expr[ops[1][0]:ops[1][1]]))

# A dictionary containing all supported
# operands and their respective functions.
op_func = {
    '**': exp_func,

    '*': mult_func,
    '/': div_func,
    '%': mod_func,

    '+': add_func,
    '-': sub_func,
}

# Given index of a '(', returns
# index of matching ')'.
def find_matching_paren(expr, s):
    spc = 0
    epc = 0
    for i in range(s + 1, len(expr)):
        if expr[i] == '(':
            spc += 1
        elif expr[i] == ')':
            epc += 1
            if epc == spc + 1:
                return i
    print('[error]: mismatching parens.')

# Given the index of an operator, returns
# the index ranges of it's operands.
def get_ops(expr, op_indx, op_len):
    lops = 0  # Left OPerand Start (really gotta work on my naming skills XD)
    for i in range(op_indx - 1, -1, -1):
        if not (expr[i].isdigit() or (expr[i] == '.')):
            lops = i + 1
            break
    lope = op_indx  # Left OPerand End
    rops = op_indx + op_len  # Right OPerand Start
    rope = len(expr)  # Right OPerand End
    for i in range(rops, len(expr)):
        if not (expr[i].isdigit() or (expr[i] == '.')):
            rope = i
            break
    return ((lops, lope), (rops, rope))

# Evaluates all operations.
# Follows operator precedence as a result
# of operators being ordered in the list.
def resolve_op(expr):
    for op_list in operators:
        for op in op_list:
            # Evaluate all instances of op. Hence the while loop.
            while (op_indx := expr.find(op)) != -1:
                # ops = operands on either side of the operator.
                ops = get_ops(expr, op_indx, len(op))
                result = op_func[op](expr, ops)
                expr = expr[:ops[0][0]] + result + expr[ops[1][1]:]
    return expr

# Recursively resolve all parens.
# Makes necessary calls to resolve_op()
# to resolve everything within parens as well.
def resolve_parens(expr):
    print('[expr]:', expr)
    s = 0
    # If there are still brackets left in expr,
    # resolve them with a recursive call.
    while (sp := expr.find('(', s)) != -1:
        s = find_matching_paren(expr, sp)
        result = resolve_parens(expr[sp+1:s])
        # Replace sub-expression with computed result.
        expr = expr[:sp] + result + expr[s+1:]
        s = 0
        print('[expr]:', expr)
    # The deepest recursive call won't contain any '()',
    # and will skip the while loop. Then it will execute
    # resolve_op() to resolve pure operators without parens.
    return resolve_op(expr)

# Main function. Called by the user with expr as
# an argument. TODO: Come up with a better name?
def eval_expr(expr):
    expr = ''.join(expr.split())
    print('[final result]:', resolve_parens(expr))

# Call eval_expr() with an expression to test this!
