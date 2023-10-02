class State:
    father: any
    def __init__(self, name, chils, f):
        self.name=name
        self.chils=chils
        self.f=f

A = State('A',[],25)
B = State('B',[],25)
C = State('C',[],25)
D = State('D',[],25)
E = State('E',[],25)
F = State('F',[],25)

A.chils=[B,C,D]
B.chils=[A,C,E]
C.chils=[A,B,D,E]
D.chils=[A,C,F]
E.chils=[B,C,F]
F.chils=[D,E]

def BusquedaAvara():
    num=0
    while(num<2):
        print("Estado actual",CurrentS.name)
        print("En Abiertos")
        for i in OpenL:
            print(i.name)
        print("En Cerrados")
        for i in CloseL:
            print(i.name)
        print("Expandiendo Abiertos")
        ExOpen()
        print("En Abiertos tras expandir")
        for i in OpenL:
            print(i.name)

        print("Agregando a Cerrados")
        AddClose()
        num+=1
        print("Fin de ciclo:", num)


def ExOpen():
    
    for i in CurrentS.chils:
        if existIn(i,OpenL):
            print("")
        else:
            OpenL.append(i)
            print("Se agrego:",i.name)
    for i in OpenL:
        i.father=CurrentS.name
        print(i.father, "padre de", i.name)
    
def AddClose():
    print("Existe?")
    print(existIn(CurrentS,CloseL))
    if(existIn(CurrentS,CloseL)):
        CloseL.append(CurrentS)

    for i in CloseL:
        print(i.name)

def existIn(obj,list):
    
    for i in list:
        print(obj.name,"==",i.name)
        if obj.name == i.name:
            print("Existe")
            return False
        else:
            print("No existe")
            return True

ListStates=[A,B,C,D,E,F]
CurrentS = A
OpenL = []
CloseL = [A]

BusquedaAvara()

