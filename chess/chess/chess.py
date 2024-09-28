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

def in_out(inp_cord,inp_name):
    letter_list = "ABCDEFGH"
    inp_num_1, inp_num_2 = (inp_cord.split("-"))
    cord = [int(inp_num_1[1]), int(inp_num_2[1]), int(letter_list.find(str(inp_num_1[0]))),
    int(letter_list.find(str(inp_num_2[0])))]
    x1, x2, y1, y2 = cord[0], cord[1], cord[2], cord[3]
    if logic(inp_name, x1, x2, y1, y2) == 1:
        return 1
    else:
        return 0