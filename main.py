operators = '*+'

def add_func(a, b):
    return str(int(a) + int(b))

op_func = {
    '+': add_func
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

def resolve_op(expr):
    for i in range(0, len(expr)):
        if expr[i] in operators:
            result = op_func[expr[i]](expr[i-1], expr[i+1])
            return result

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
    print(resolve_parens(expr))

eval_expr('(1 + (2 + 3)) + (4 + (5 + 6)) + 7')