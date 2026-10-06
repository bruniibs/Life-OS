
print("LIFE OS")
print("Planner")
tasks = []

task = {
    "id": 1,
    "title": "Estudar Python",
    "completed": False
}


while True:
    print("\nMenu:")
    print("1. Ver tarefas\n2. Adicionar tarefa\n3. Concluir tarefa\n4. remover tarefa\n5. Sair")
    
    opcao = input("Escolha uma opção: ").strip()
    print("Você escolheu a opção:", opcao)
    
    if opcao == "1":
        print("Ver tarefas")
    elif opcao == "2":
        print("Digite o nome da tarefa:")
        title = input("")
        print("Tarefa adicionada!")
        tasks.append(task)
    elif opcao == "3":
        print("Concluir tarefa")
    elif opcao == "4":
        print("Remover tarefa")
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
    