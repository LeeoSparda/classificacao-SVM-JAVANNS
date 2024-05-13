def update_class_label(class_label):
    if class_label == 'A':
        return '1'
    elif class_label == 'B':
        return '2'
    elif class_label == 'C':
        return '3'
    elif class_label == 'D':
        return '4'
    elif class_label == 'E':
        return '5'
    elif class_label == 'F':
        return '6'
    elif class_label == 'G':
        return '7'
    elif class_label == 'H':
        return '8'
    elif class_label == 'I':
        return '9'
    elif class_label == 'J':
        return '10'
    elif class_label == 'K':
        return '11'
    elif class_label == 'L':
        return '12'
    elif class_label == 'M':
        return '13'
    elif class_label == 'N':
        return '14'
    elif class_label == 'P':
        return '15'
    elif class_label == 'Q':
        return '16'
    elif class_label == 'R':
        return '17'
    elif class_label == 'T':
        return '18'
    elif class_label == 'V':
        return '19'
    elif class_label == 'W':
        return '20'
    elif class_label == 'X':
        return '21'
    elif class_label == 'Y':
        return '22'
    elif class_label == 'Z':
        return '23'
    # Adicione mais condições conforme necessário para outras classes
    else:
        return class_label

def update_javanns_file(input_file, output_file):
    with open(input_file, 'r') as input_file, open(output_file, 'w') as output_file:
        for line in input_file:
            data = line.strip().split(',')
            class_label = data[-1]
            updated_class_label = update_class_label(class_label)
            updated_line = ','.join(data[:-1]) + f',{updated_class_label}\n'
            output_file.write(updated_line)

input_file_javanns = "C:/Users/Leonardo Borges/Desktop/CG/Atividade7/atividade/javanns_resultados.txt"
output_file_javanns_updated = "C:/Users/Leonardo Borges/Desktop/CG/Atividade7/atividade/javanns_resultados1.txt"

update_javanns_file(input_file_javanns, output_file_javanns_updated)
print(f"O arquivo atualizado foi salvo em '{output_file_javanns_updated}'.")
