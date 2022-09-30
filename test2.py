"""
2. Задан массив из чисел a1... aN, требуется найти границы его строго монотонного подотрезка максимальной длины. Если их несколько, вывести границы любого.
Примеры: 
1) ввод: -3, 2, 3, 4, 5, 6, 7, 7, 8
вывод: 0, 6
2) ввод: -1, -1, -1, -1, -1, -1, -1, -1, -1
вывод: 0, 0 (или другой индекс: i, i)
"""

print ("2. Задан массив из чисел a1... aN, требуется найти границы его строго монотонного подотрезка максимальной длины. Если их несколько, вывести границы любого. \n Примеры: \n ввод 1: -3, 2, 3, 4, 5, 6, 7, 7, 8 \n вывод: 0, 6 \n ввод 2 : -1, -1, -1, -1, -1, -1, -1, -1, -1 \n вывод: 0, 0 (или другой индекс: i, i)")
print ('Вы можете воспользоваться нашими примерами для тестирования программы:')

d = [[-3, 2, 3, 4, 5, 6, 7, 7, 8], [-1, -1, -1, -1, -1, -1, -1, -1, -1], [0, 8, 9, 10, 11, 12, 163, 18, 19, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 100]]

for i in range(len(d)):
	print (d[i])

l_index = int(input ('Выберите пример, указав цифру: '))

l = d[l_index -1]



def check_list (input_list):
	
	input_list.append(input_list[-1])
	
	input_list.append(input_list[-1])

	matrix = []
	
	index = 0

	while index < len(input_list) - 2:

		delta1 = input_list[index+1] - input_list[index]
		delta2 = input_list[index+2] - input_list[index+1]

		sequence = set()

		if delta1 == delta2:	
			
			new_list = input_list[index:]

			for i in range(len(new_list)-2):

				if new_list[i+1] - new_list[i] == new_list[i+2] - new_list[i+1] and delta1 !=0 :

					sequence.add(i+index)
					sequence.add(i+1+index)
					sequence.add(i+2+index)
					i = i+1

				else:
					break

		if len(sequence) > 2 :
			matrix.append(sequence)
			index = index + len(sequence) -1 
		else: 
			index = index + 1

	return(matrix)

fin_matrix = check_list(l)

if len(fin_matrix) == 0:
	print ('Вывод: 0,0')
	exit()


max_list=0
index = 0

for i in range(len(fin_matrix)):
	if len(fin_matrix[i]) > max_list:
		max_list = len(fin_matrix[i])
		index = i

print ('Вывод: ', min(fin_matrix[index]), ",", max(fin_matrix[index]))












