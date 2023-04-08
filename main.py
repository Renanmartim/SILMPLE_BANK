class banco:
    
    saldo = 0
        

    def __init__(self, nome, id):
        self.id = id
        self.nome = nome
        print("----------------------------------------------")
        print("BANCO CLASSIC")
        print("----------------------------------------------")
        print(f"BEM-VINDO {self.nome} SUA CONTA É: {self.id}")
        print("----------------------------------------------")
        
    def sacar(self, valor):
        if valor > self.saldo:
            print("----------------------------------------------")
            print("VOCE NÃO TEM ESTE VALOR EM CONTA")
            print("----------------------------------------------")
        elif valor > 500:
            print("----------------------------------------------")
            print("VOCE SÓ PODE SACAR VALORES A BAIXO DE R$ 500")
            print("----------------------------------------------")
        else:
            self.saldo = self.saldo - valor 
            
    def depositar(self, deposito):
        self.saldo = self.saldo + deposito
    
    def extrato(self):
        print("----------------------------------------------")
        print(f"SALDO EM CONTA: {self.saldo}")
        print("----------------------------------------------")
        
print("BANCO CLASSIC")
print("Digite seu nome: ")   
nome = input()        
print("Digite sua conta: ")     
conta = input()

total = 0
limit = 0

bc = banco(nome , conta)


print("-----------OPERAÇÕES POSSÍVEIS-----------")
print("[0] - DEPOSITAR")
print("[1] - SACAR")
print("[2] - EXTRATO")
print("[3] - SAIR")

op = int(input())

while op != 3:
    
    if op == 0:
        print("DIGITE A QUANTIA QUE GOSTARIA DE DEPOSITAR: ")
        depositar = int(input())
        bc.depositar(depositar)
        print("-----------OPERAÇÕES POSSÍVEIS-----------")
        print("[0] - DEPOSITAR")
        print("[1] - SACAR")
        print("[2] - EXTRATO")
        print("[3] - SAIR")

        op = int(input())
            
    elif op == 1:
        print("DIGITE A QUANTIA QUE GOSTARIA DE SACAR: ")
        saque = int(input())
        total = total + saque
        if total <= 1500 or limit <= 3:
            bc.sacar(saque)
            limit = limit + 1
        
        else:
            print("LIMITE DIÁRIO ATINGIDO")
        print("-----------OPERAÇÕES POSSÍVEIS-----------")
        print("[0] - DEPOSITAR")
        print("[1] - SACAR")
        print("[2] - EXTRATO")
        print("[3] - SAIR")

        op = int(input())
        
                
    elif op == 2:
        bc.extrato()
        print("-----------OPERAÇÕES POSSÍVEIS-----------")
        print("[0] - DEPOSITAR")
        print("[1] - SACAR")
        print("[2] - EXTRATO")
        print("[3] - SAIR")

        op = int(input())
        
    elif op == 3:
        break
        
        

            
        
        
    
