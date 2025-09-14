from operator import add, sub, mul, truediv


def basic_op(operator, value1, value2):
    ops = {"+": add, "-": sub, "*": mul, "/": truediv}
    try:
        return ops[operator](value1, value2)
    except:
        raise ValueError(f"Unknown operator: {operator}")
