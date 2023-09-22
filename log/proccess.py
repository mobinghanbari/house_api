path = f"log/count.txt"

def insert():
    m = open(path, "r")
    data = int(m.read())
    if data == 0:
        count = "0"
        m = int(count)+1
        count = str(m)
        with open(path, mode="w") as f:
                f.write(count)
    if data > 0:
        with open(path, mode="w") as fn:
            data = data+1
            count = str(data)
            fn.write(count)


path2 = f"log/detail.txt"

def create_log(message:str):
    with open(path2, mode="a") as f2:
            f2.write(message + "\n")