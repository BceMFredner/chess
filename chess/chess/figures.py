def delta(num1,num2):
    return abs(num1-num2)
def elephant(num_1,num_2,let_1,let_2):
    if delta(let_1,let_2) == delta(num_1,num_2):
        return 1
    else:
        return 0
def rook(num_1,num_2,let_1,let_2):
    if let_1 == let_2 and num_1 != num_2:
        return 1
    elif num_1 == num_2 and let_1 != let_2:
        return 1
    else:
        return 0
def pawn(num_1,num_2,let_1,let_2):
    if let_1 == let_2:
        if num_2 - num_1 == 1:
            return 1
        else:
            return 0
    else:
        return 0
def king(num_1,num_2,let_1,let_2):
    if delta(let_1,let_2) <= 1:
        if delta(num_1,num_2) <= 1:
            return 1
        else:
            return 0
    else:
        return 0
def horse(num_1,num_2,let_1,let_2):
    if delta(let_1,let_2) == 2 and delta(num_1,num_2) == 1:
        return 1
    elif delta(num_1,num_2) == 2 and delta(let_1,let_2) == 1:
        return 1
    else:
        return 0