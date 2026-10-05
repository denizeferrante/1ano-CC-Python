from aluno import Aluno
from disciplina import Disciplina

# criar / instanciar 1 aluno
aluno1 = Aluno("João", "123456", "Ciência da Computação")

# criar / instanciar 2 disciplinas
sers = Disciplina("Soluções Renováveis", "Tritiack")
prompt_ia = Disciplina("Prompt & IA", "José Maia")

# matricular o aluno nas disciplinas
aluno1.matricular(sers)
aluno1.matricular(prompt_ia)

# adicionar notas das disciplinas do aluno
aluno1.adicionar_nota(sers, 10)
aluno1.adicionar_nota(sers, 8)
aluno1.adicionar_nota(prompt_ia, 5)
aluno1.adicionar_nota(prompt_ia, 3)

# print(aluno1.calcular_media_d(prompt_ia))
print(aluno1.calcular_media_geral())




