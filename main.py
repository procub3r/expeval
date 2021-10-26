operators = ['**', ['*', '/', '//', '%'], ['+', '-']]

def eval(expr):
    print('[expr]:', expr)
    sp = expr.find('(')
    ep = -1
    if sp != -1:
        tmp_sp_count = 0
        tmp_ep_count = 0
        for i in range(sp + 1, len(expr)):
            if expr[i] == '(':
                tmp_sp_count += 1
            elif expr[i] == ')':
                tmp_ep_count += 1
                if tmp_ep_count == tmp_sp_count + 1:
                    ep = i
                    break
        eval(expr[sp+1:ep])
    else:
        print(f'\t{eval(expr)}')
