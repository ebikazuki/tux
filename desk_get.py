import json

def desk_result():
    file = open("desk.json", "r")
    json_dict = json.load(file)
    result = json_dict["desk"]
    return result

if __name__ == '__main__':
    desk_result()

