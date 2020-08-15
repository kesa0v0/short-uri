from simplifier import base62
from database import DB

if __name__ == "__main__":
    db = DB()

    uri = "https://somekindofsomething.lol"
    shorturi = base62()

    print(shorturi)
