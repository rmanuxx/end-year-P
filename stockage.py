import json 

STOCKAGE="database.json"

def save_coffre(coffre):
    with open(STOCKAGE,"w",encoding="utf-8") as file :
        json.dump(coffre,file,indent=4,ensure_ascii=False)

def load_coffre():
    try:
        with open(STOCKAGE,"r",encoding="utf-8") as file :
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []
      