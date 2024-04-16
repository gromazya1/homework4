immutable_var = 1, "one", 1.1, True
print(immutable_var)
#immutable_var[2] = False выдает ошибкку, т.к. кортеж не поддерживает обращение по элементам
#однако, если внутри кортежа сделать список, то элементы в списке можно изменять
immutable_var = 1, "one", [1.1, True]
immutable_var[2][0] = False
print(immutable_var)
mutable_list = ["zero", "one", "two", "three"]
print(mutable_list)
mutable_list[0] = "changed"
mutable_list.extend(["changed" , 4])
mutable_list.remove("changed")
print(mutable_list)
print("changed" in mutable_list)

