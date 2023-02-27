table_options = [(i, 2*(i-1)+j) for i in range(1, 51) for j in range(1, 3)]
final_options = [(table_options[i], table_options[j]) for i in range(len(table_options)) for j in range(i+1, len(table_options))]

for value in final_options:
    print(value)