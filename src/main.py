import json
from pathlib import Path
# Define the path to the tasks.json file
DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "tasks.json"

print("LIFE OS")
print("Planner")

def save_tasks():
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

tasks, next_id = load_tasks()

while True:
    print("\nMenu:")
    print("1. Ver tarefas\n2. Adicionar tarefa\n3. Concluir tarefa\n4. remover tarefa\n5. Sair\n")
    
    opcao = input("Escolha uma opção: \n").strip()
    
    if opcao == "1":
        print("=== TAREFAS ===")
        for task in tasks:
            if task['completed'] == False:
                print(f"[ ] {task['id']}. {task['title']} \n")
            else:
                print(f"[✓] {task['id']}. {task['title']} \n")
            
        
    elif opcao == "2":
        title = input("Digite o nome da tarefa: \n")
        task = {
        "id": next_id,
        "title": title,
        "completed": False}
        tasks.append(task)
        next_id += 1
        save_tasks()
        print("Tarefa adicionada! \n")
        
    elif opcao == "3":        
        try:
            # vai verificar se o input eh um numero int
            id_digitado = int(input("Digite o ID da tarefa que deseja concluir: \n"))
            
            for task in tasks:
                if id_digitado == task['id']:
                    task['completed'] = True
                    save_tasks()
                    print("Tarefa concluída!")
                    break
             # ELSE do FOR, caso id digitado nao exista
            else:
                print("Tarefa não encontrada.")
            # mensagem de erro caso input seja invalido
        except ValueError:
                print("ID inválido. Por favor, digite um número inteiro.")
        
    elif opcao == "4":
        try:
            id_digitado = int(input("Digite o ID da tarefa que deseja remover: \n"))
            
            for task in tasks:
                if id_digitado == task['id']:
                    tasks.remove(task)
                    save_tasks()
                    print("Tarefa removida!")
                    break
            else:
                print("Tarefa não encontrada.")
        except ValueError:
                print("ID inválido. Por favor, digite um número inteiro.")
        
    elif opcao == "5":
        print("Saindo...")
        break
    
    else:
        print("Opção inválida..")
    