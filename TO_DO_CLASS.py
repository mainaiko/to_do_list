class To_Do_List():
    def __init__(self, teste):
        self.teste = teste

    def add_task(self):
        variavel_name = input("escolha o nome da task")
        self.teste.append({"task": variavel_name, "done": False})
    
    def list_task(self):
        return print (self.teste)
    
    def mark_task_done(self, index):
        if 0<= index < len(self.teste):
            self.teste[index]["done"] = True
    
    def delete_task(self):
        if len(self.teste) > 0:
            self.teste.pop()
