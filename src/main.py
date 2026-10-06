
print("LIFE OS")
print("Planner")
tasks = []


while True:
    print("\nMenu:")
    print("1. Ver tarefas\n2. Adicionar tarefa\n3. Concluir tarefa\n4. remover tarefa\n5. Sair")
    
    opcao = input("Escolha uma opção: ").strip()
    print("Você escolheu a opção:", opcao)
    
    if opcao == "1":
        print("Ver tarefas")
        continue
    elif opcao == "2":
        print("Adicionar tarefa")
        continue
    elif opcao == "3":
        print("Concluir tarefa")
        continue
    elif opcao == "4":
        print("Remover tarefa")
        continue
    elif opcao == "5":
        print("Saindo...")
        break
    else:
        print("Opção inválida.")
        break
    