from TO_DO_CLASS import To_Do_List

def menu():
    print ("(1) adicionar task",
    "(2) listar tasks",
    "(3) marcar feito",
    "(4) deletar ultima task"
    )


def main():
    todo_list = To_Do_List([])

    while True:
        menu()
        resposta = int(input("Escolha uma opçao: "))

        if resposta == 1:
            todo_list.add_task()

        elif resposta == 2:
            todo_list.list_task()

        elif resposta == 3:
            task = int(input("qual deseja marcar feito?"))
            todo_list.mark_task_done(task)

        elif resposta == 4:
            todo_list.delete_task()
        
        else:
            print ("resposta incorreta")
            main()

main()

    