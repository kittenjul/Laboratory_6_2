 #  12. Подсчитать количество пропусков в данных для каждого столбца
missing = [0]*12

with open("data.csv") as file:
    for line in file:
        data = line.split(',')
        for i in range (0,12):
            if data [i] == '':
                missing[i] += 1
    for i in range (0,12):
        print(i, missing [i])