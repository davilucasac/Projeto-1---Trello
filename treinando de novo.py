tarefas = []
# código de criar tarefa
def criar_tarefa():
    tarefa = {'id': int(input('ID: ')),
              'titulo': input('Titulo: '),
              'desc': input('Descricao: '),
              'status': input('Status [A fazer, Fazendo, Concluído] :  ')}
    tarefas.append(tarefa)
def listar_tarefas():
    print('=' * 20)
    print('Minhas Tarefas'.center(20))
    print('=' * 20)
    for tarefa in tarefas:
        print(f"ID: {tarefa['id']}")
        print(f"Título: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['desc']}")
        print(f"Status: {tarefa['status']}")
        print('-' * 20)
def atualizar_tarefas():
    atualizador = int(input('Digite o ID da tarefa que deseja editar: '))
    encontrar = False
    for tarefa in tarefas:
        if tarefa['id'] == atualizador:
            encontrar = True
            opcao = int(input('O que você deseja alterar? (titulo (1), desc (2) ou status (3)? '))
            if opcao == 1:
                tarefa['titulo'] = input('Escolha um novo título: ')
            elif opcao == 2:
                tarefa['desc'] = input('Escolha uma nova descrição: ')
            elif opcao == 3:
                tarefa['status'] = input('Escolha um novo status: ')
            else:
                print('Opção Inválida')
    if encontrar == False:
        print("Tarefa não pode ser atualizada")
def excluir_elemento():
    excluir = int(input('Digite o ID da tarefa que quer excluir: '))
    encontrou = False
    for tarefa in tarefas:
        if excluir == tarefa['id']:
            encontrou = True
            ctz = str(input('Você deseja excluir [S/N]')).upper()
            if ctz == "S":
                tarefas.remove(tarefa)
                print("Tarefa Removida")
    if encontrou == False:
        print('Tarefa não encontrada')
while True:
    print('=-' * 20)
    print("Meu Trelo".center(40))
    print('=-' * 20)
    print('1 - Criar Tarefa')
    print('2 - Listar Tarefa')
    print('3 - Editar Tarefa')
    print('4 - Excluir Tarefa')
    print('0 - Sair')
    escolha = int(input('Escolha uma opção: '))
    # função de criar tarefa
    if escolha == 1:
        criar_tarefa()
    # função de  listar tarefas
    elif escolha == 2:
        listar_tarefas()
    # função de atualizar tarefas
    elif escolha == 3:
        atualizar_tarefas()
    # função de exluir tarefas
    elif escolha == 4:
        excluir_elemento()        
    elif escolha == 0:
        break
