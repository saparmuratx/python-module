def parse_arguments(args):

    res = dict()

    command = args.pop(0)

    for argument in args:
        arg_pair = argument.split('=')
        if len(arg_pair) == 2:
            res[arg_pair[0]] = arg_pair[1]
    
    return command, res

def format_expenses_list(expenses):
    res = list()
    for row in expenses:
        res.append(f"# {row[0]}   {row[1]} {row[2]}    {row[3]}")

    return res
