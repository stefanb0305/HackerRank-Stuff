amount = int(raw_input())
L = []
for _ in range(amount):
    comment = raw_input()
    list=[]
    list = comment.split()
    command = list[0]
    if len(list) == 2:
        e = int(list[1])
    if len(list) == 3:
        i = int(list[1])
        e = int(list[2])
    if command=="insert":
        L.insert(i,e)
    elif command=="remove":
        L.remove(e)
    elif command=="append":
         L.append(e)
    elif command=="sort":
         L.sort()
    elif command=="pop":
         L.pop()
    elif command=="reverse":
         L.reverse()
    elif command=="print":
         print(L)