N1, N2, N3, N4 = map(float, input().split())
Mean = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 10
print('Media: %.1f'%Mean)
if Mean >= 7.0:
    print('Aluno aprovado.')
elif Mean < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    ExamScore = float(input())
    print('Nota do exame: %.1f'%ExamScore)
    FinalMean = (ExamScore + Mean) / 2
    if FinalMean >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado')
    print('Media final: %.1f'%FinalMean)