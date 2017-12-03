import random
from uuid import uuid4
from collections import defaultdict
SEMENTE=42 #Gera uma pseudo-aleatoriadade reproduzivel
ESPECIES=["monitoria","extensão","pesquisa"]
MATERIAS=["Algoritmos","Lógica Matemática","Introdução à Ciência da Computação","Cálculo  Diferencial e Integral 1","Geometria Analítica e Álgebra Linear","Comunicação Linguística","Ética Profissional e Cidadania","Algoritmos e Estruturas de Dados","Elementos de Lógica Digital","Física 3","Probabilidade e Estatística","Fundamentos de Administração","Algoritmos e Estruturas de Dados","Arquitetura e Organização de Computadores","Interação Homem-Computador","Cálculo Numérico","Análise e Projeto Orientado a Objetos","Banco de Dados 1","Teoria dos Grafos","Linguagens Formais", "Autômatos e Computabilidade","Sistemas Microcontrolados","Redes de Computadores","Programação de Aplicativos","Banco de Dados 2","Sistemas Operacionais","Linguagens de Programação","Análise de Algoritmos","Projeto Integrador","Engenharia de Software 1","Redes de Computadores","Computação Gráfica","Inteligência ArtificiaL"]
random.seed(SEMENTE)
#x=0 -> Não tem projeto, nem dependencias. x=1 Tem projetos. x=2 Tem dp's
def geradorAluno():
	x=random.randint(0,2)
	aux=random.randint(1,10)#Definirá o semestre do Aluno
	if(aux==1):#Caso for do primeiro Semestre
		aluno={
                        "_id":uuid4().hex,
                        "RA":''.join(random.sample("0123456789",7)),
                        "nome":''.join(random.sample("abcdefghijklmnopqrstuvwxyz",random.randint(3,20))),
                        "semestre":aux,
                        #"CR":round(random.random(),3) Aluno no primeiro semestre n tem CR
		}
	else:
		aluno={
                        "_id":uuid4().hex,
			"RA":''.join(random.sample("0123456789",7)),
			"nome":''.join(random.sample("abcdefghijklmnopqrstuvwxyz",random.randint(3,20))),
			"semestre":aux,
			"CR":round(random.random(),3)
			}
	if(x==0):
		return aluno
	if(x==1):
		aluno['projeto'] = projetoAluno()
		return aluno
	aluno['dependencias']= dependeciasAluno()
	return aluno
	
def projetoAluno():
	projeto = {
		"especie":ESPECIES[random.randint(0,2)],
		"salario":random.randint(300,1200)
		}
	return projeto
def dependeciasAluno():
	dps=[]
	x=random.randint(1,33) # define o número de matérias
	for i in range(1,x+1):
		dps.append(MATERIAS[random.randint(0,32)])
	return dps
