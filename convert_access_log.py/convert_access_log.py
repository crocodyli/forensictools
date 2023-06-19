import csv
import re

# Defina o caminho para o arquivo access.log
arquivo_log = "C:\\Local\\do arquivo\\access.log"

# Defina o caminho para o arquivo CSV de saída
arquivo_csv = "C:\\Local\\do arquivo\\final_access.csv"

# Poderá alterar o parâmetro de expressões regulares - já está para o access.log
padrao_log = r'^(\S+) \S+ \S+ \[([^\]]+)\] "(\S+) ([^\s]+) \S+" (\d+) (\d+|-)'

with open(arquivo_log, 'r') as log_file:
    with open(arquivo_csv, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        writer.writerow(['IP', 'Data', 'Hora', 'Método', 'URL', 'Código', 'Bytes'])

        for linha in log_file:
            match = re.match(padrao_log, linha)
            if match:
                ip = match.group(1)
                data_hora = match.group(2)
                metodo = match.group(3)
                url = match.group(4)
                codigo = match.group(5)
                bytes = match.group(6)

                writer.writerow([ip, data_hora.split()[0], data_hora.split()[1], metodo, url, codigo, bytes])

print('Conversão concluída. Arquivo CSV gerado:', arquivo_csv)


