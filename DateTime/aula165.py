from datetime import datetime

from dateutil.relativedelta import relativedelta  # type:ignore

valor_total = 1_000_000
data_inicio_emprestimo = datetime.strptime('2020/12/20', '%Y/%m/%d')
data_final_emprestimo = (data_inicio_emprestimo + relativedelta(years=5))
data_parcela = data_inicio_emprestimo
data_lista = []
parcelas_pagas = i = 0

while data_parcela < data_final_emprestimo:
    parcelas_pagas += 1
    data_parcela = data_inicio_emprestimo + relativedelta(months=parcelas_pagas)
    data_lista.append(data_parcela.strftime("%d/%m/%Y"))

for data in data_lista:
    print(
        f'Parcela {i} | Vence em {data} | Valor {valor_total/len(data_lista):,.2f} R$')
    i += 1
