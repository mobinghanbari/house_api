

path = f"api/users/info/usr.txt"

def show_user(message:str):
    with open(path, mode="a") as f:
            f.write(message + "\n")
