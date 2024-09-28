import figures
def logic(inp_name,x1,x2,y1,y2):
    if inp_name == "король":
        return figures.king(x1,x2,y1,y2)
    elif inp_name=="пешка":
        return figures.pawn(x1,x2,y1,y2)
    elif inp_name=="ладья":
        return figures.rook(x1,x2,y1,y2)
    elif inp_name=="слон":
        return figures.elephant(x1,x2,y1,y2)
    elif inp_name=="королева":
        if figures.elephant(x1,x2,y1,y2)==1:
            return 1
        else:
            return figures.rook(x1,x2,y1,y2)
    else:
        return figures.horse(x1,x2,y1,y2)