# A 2 x 3 matrix of integers.
matrix = [[30, -49, 26], [16, 9, -89]]
# Print the first element.
print(matrix[0][0]) # 30
# Print the last element.
print(matrix[1][2]) # -89
# Print the last element again using the indices in an easier manner.
print(matrix[-1][-1]) # -89

"""Tulostetaan matriisi riveittäin tutumpaan kaksiulotteiseen muotoon kahdella 
eri tavalla:"""

# Print the matrix row by row using the row index. The len function
# counts the number of rows.
for row_ind in range(0, len(matrix)):     # [30, -49, 26]
    print(matrix[row_ind])                # [16, 9, -89]

# Print the matrix row by row using the row as a counter.
for row in matrix:                        # [30, -49, 26]
    print(row)                            # [16, 9, -89]

"""Koodista havaitaan, että tässä esimerkissä kannattaa laskea ilman indeksejä, 
koska matriisia silmukoitaessa for liittää row-viitteen automaattisesti kuhunkin
matriisin alilistoista."""
