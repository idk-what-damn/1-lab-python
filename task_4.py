def get_length(seq):
    count = 0
    for _ in seq:
        count = count + 1
    return count

def transpose(matrix):
    rows = get_length(matrix)
    cols = get_length(matrix[0])
    transposed = []
    i = 0
    while i < cols:
        new_row = []
        j = 0
        while j < rows:
            new_row = new_row + [matrix[j][i]]
            j = j + 1
        transposed = transposed + [new_row]
        i = i + 1
    return transposed

print("Введите количество строк:")
row_count = int(input())

print("Введите количество столбцов:")
col_count = int(input())

matrix = []
i = 0
while i < row_count:
    print("Введите элементы строки", i + 1, ":")
    row = []
    j = 0
    while j < col_count:
        print(f"  Элемент {j + 1}: ")
        value = int(input())
        row = row + [value]
        j = j + 1
    matrix = matrix + [row]
    i = i + 1

print("\nИсходная матрица:")
i = 0
while i < get_length(matrix):
    print(f"Строка {i + 1}: ", matrix[i])
    i = i + 1

result = transpose(matrix)

print("\nТранспонированная матрица:")
i = 0
while i < get_length(result):
    print(f"Строка {i + 1}: ", result[i])
    i = i + 1
