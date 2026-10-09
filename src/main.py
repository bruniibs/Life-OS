
print("LIFE OS")
print("Planner")

tasks = []

while True:
    print("\nMenu:")
    print("1. Ver tarefas\n2. Adicionar tarefa\n3. Concluir tarefa\n4. remover tarefa\n5. Sair\n")
    
    opcao = input("Escolha uma opção: \n").strip()
    print("Você escolheu a opção: \n", opcao)
    
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
        "id": len(tasks) + 1,
        "title": title,
        "completed": False}
        tasks.append(task)
        print("Tarefa adicionada! \n")
        
    elif opcao == "3":        
        try:
            # vai verificar se o input eh um numero int
            id_digitado = int(input("Digite o ID da tarefa que deseja concluir: \n"))
            
            for task in tasks:
                if id_digitado == task['id']:
                    task['completed'] = True
                    print("Tarefa concluída!")
                    break
             # ELSE do FOR, caso id digitado nao exista
            else:
                print("Tarefa não encontrada.")
            # mensagem de erro caso input seja invalido
        except ValueError:
                print("ID inválido. Por favor, digite um número inteiro.")
        
    elif opcao == "4":
        print("Remover tarefa")
        
    elif opcao == "5":
        print("Saindo...")
        break
    
    else:
        print("Opção inválida.")
    