import csv
import re

# Defina o caminho para o arquivo error.log
arquivo_log = "C:\\Local\\do arquivo\\error.log"

# Defina o caminho para o arquivo CSV de saída
arquivo_csv = "C:\\Local\\do arquivo\\final_error.csv"

# Poderá alterar o parâmetro de expressões regulares - já está para o error.log
padrao_log = r'\[(.*?)\] \[(.*?)\] \[(.*?)\] (.*)'

with open(arquivo_log, 'r') as log_file:
    with open(arquivo_csv, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(['Data/Hora', 'Nível', 'Módulo', 'Mensagem'])

        for linha in log_file:
            match = re.match(padrao_log, linha)
            if match:

                data_hora = match.group(1)
                nivel = match.group(2)
                modulo = match.group(3)
                mensagem = match.group(4)

                writer.writerow([data_hora, nivel, modulo, mensagem])

print('Conversão concluída. Arquivo CSV gerado:', arquivo_csv)
