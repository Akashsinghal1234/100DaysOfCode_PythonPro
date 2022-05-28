row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
position_list = list(position)
position_list[0] = int(position_list[0]) - 1
position_list[1] = int(position_list[1]) - 1
map[position_list[1]][position_list[0]] = "x"
print(f"{row1}\n{row2}\n{row3}")