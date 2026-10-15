import json
from pathlib import Path
# Define the path to the tasks.json file
DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "tasks.json"

def save_tasks(tasks, next_id):
    data = {
        "next_id": next_id,
        "tasks": tasks
    }
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

def load_tasks():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
        return data["tasks"], data["next_id"]
    except FileNotFoundError:
        # se o arquivo nao for encontrado, comeca o programa com uma lista vazia com ID 1
        return [], 1
    except json.JSONDecodeError:
        print("Erro: o arquivo de tarefas contem JSON invalido.")
        raise