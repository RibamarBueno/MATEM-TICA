notas = []

n_alunos  = int(input("Digite o número de alunos: \n"))
n_disciplinas = int(input("Digite o número de disciplinas: \n"))

for i in range(n_alunos):
    notas_aluno = []
    for j in range(n_disciplinas):
        nota = int(input(f"Digite a nota do aluno {i + 1} na disciplina {j + 1}:\n"))
        notas_aluno.append(nota)
    notas.append(notas_aluno)

print("Matriz de Notas:")
for i in range(n_alunos):
    print(notas[i])