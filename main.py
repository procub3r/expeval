# These are the only operators supported atm.
operators = [['**'], ['*', '/', '%'], ['+', '-']]

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

op_func = {
    '**': exp_func,

    '*': mult_func,
    '/': div_func,
    '%': mod_func,

    '+': add_func,
    '-': sub_func,
}

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

def get_ops(expr, op_indx, op_len):
    lops = 0
    for i in range(op_indx - 1, -1, -1):
        if not (expr[i].isdigit() or (expr[i] == '.')):
            lops = i + 1
            break
    lope = op_indx
    rops = op_indx + op_len
    rope = len(expr)
    for i in range(rops, len(expr)):
        if not (expr[i].isdigit() or (expr[i] == '.')):
            rope = i
            break
    return ((lops, lope), (rops, rope))

def resolve_op(expr):
    for op_list in operators:
        for op in op_list:
            while (op_indx := expr.find(op)) != -1:
                # ops = operands on either side of the operator.
                ops = get_ops(expr, op_indx, len(op))
                result = op_func[op](expr, ops)
                expr = expr[:ops[0][0]] + result + expr[ops[1][1]:]
    return expr

def resolve_parens(expr):
    print('[expr]:', expr)
    s = 0
    while (sp := expr.find('(', s)) != -1:
        s = find_matching_paren(expr, sp)
        result = resolve_parens(expr[sp+1:s])
        expr = expr[:sp] + result + expr[s+1:]
        s = 0
        print('[expr]:', expr)
    return resolve_op(expr)

def eval_expr(expr):
    expr = ''.join(expr.split())
    print('[final result]:', resolve_parens(expr))

# Call eval_expr() with an expression to test this!
