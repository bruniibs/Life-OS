from storage import save_tasks, load_tasks
from planner import add_task, complete_task, remove_task, list_tasks

tasks, next_id = load_tasks()

print("LIFE OS")
print("Planner")


while True:
    print("\nMenu:")
    print("1. Ver tarefas\n2. Adicionar tarefa\n3. Concluir tarefa\n4. remover tarefa\n5. Sair\n")
    
    opcao = input("Escolha uma opção: \n").strip()
    
    if opcao == "1":
        print("=== TAREFAS ===")
        for task in list_tasks(tasks):
            if task["completed"]:
                print(f"[✓] {task['id']}. {task['title']}")
            else:
                print(f"[ ] {task['id']}. {task['title']}")
        
    elif opcao == "2":
        # recebe o titulo da tarefa
        title = input("Digite o nome da tarefa: \n")
        
        # recebe a prioridade da tarefa
        priority = input(
            "Prioridade (low, medium, high): \n"
        ).strip().lower()
        
        while priority not in ("low", "medium", "high"):
            print("Prioridade inválida. Por favor, escolha entre low, medium ou high.")
            priority = input(
                "Prioridade (low, medium, high): \n"
            ).strip().lower()
        
        # cria e salva a tarefa        
        next_id = add_task(tasks, next_id, title, priority)
        save_tasks(tasks, next_id)
        
        print("Tarefa adicionada! \n")
        
    elif opcao == "3":        
        try:
            # vai verificar se o input eh um numero int
            id_digitado = int(input("Digite o ID da tarefa que deseja concluir: \n"))
            
            if complete_task(tasks, id_digitado):
                save_tasks(tasks, next_id)
                print("Tarefa concluída!")
            else:
                print("Tarefa não encontrada.")
            # mensagem de erro caso input seja invalido
        except ValueError:
                print("ID inválido. Por favor, digite um número inteiro.")
        
    elif opcao == "4":
        try:
            id_digitado = int(input("Digite o ID da tarefa que deseja remover: \n"))
            
            if remove_task(tasks, id_digitado):
                save_tasks(tasks, next_id)
                print("Tarefa removida!")
            else:
                print("Tarefa não encontrada.")

        except ValueError:
                print("ID inválido. Por favor, digite um número inteiro.")
        
    elif opcao == "5":
        print("Saindo...")
        break
    
    else:
        print("Opção inválida..")
    