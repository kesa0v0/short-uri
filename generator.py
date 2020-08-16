from database import DB

words = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
         'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
         'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
db = DB()


def simplifier(num):
    result = ""

    while num % 62 > 0 or result == "":
        result += words[num % 62]
        num = int(num / 62)

    return result


def generate(uri):
    num = db.insert()
    shorturi = simplifier(num)
    db.update(num, uri, shorturi)
