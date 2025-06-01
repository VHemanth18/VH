import json

BASE_DIR = "D:/GEN AI/VH/"
def read_user():
    with open(f"{BASE_DIR}data/users.json") as stream:
        users = json.load(stream)
        return users


def read_alternatives(question_id: int):
    with open(f"{BASE_DIR}data/alternatives.json") as stream:
        alternatives = json.load(stream)

    for alternative in alternatives:
        if alternative['question_id'] == question_id:
            res = alternative.get('alternative')
            print(res)
            return res






if __name__ == "__main__":
    print(read_user())
    read_alternatives(1)