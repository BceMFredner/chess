import chess
let_list="ABCDEFGH"
inp_cord = input()
inp_name = input()
inp_num_1,inp_num_2=(inp_cord.split("-"))
cord=[int(inp_num_1[1]),int(inp_num_2[1]),int(let_list.find(str(inp_num_1[0]))),int(let_list.find(str(inp_num_2[0])))]
x1,x2,y1,y2=cord[0],cord[1],cord[2],cord[3]
if chess.logic(inp_name,x1,x2,y1,y2)==1:
    print("Да, может")
else:
    print("Нет, не может")