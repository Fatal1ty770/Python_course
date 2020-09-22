class Matrix:
    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matric = [[0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]

        for i in range(len(self.list_1)):

            for j in range(len(self.list_2[i])):
                matric[i][j] = self.list_1[i][j] + self.list_2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matric]))


    def __str__(self):
        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matric]))



my_matrix = Matrix([[2, 14, 1],
                    [16, 7, 86],
                    [95, 36, 89]],
                   [[26, 68, 87],
                    [16, 81, 5],
                    [84, 13, 26]])


print(my_matrix.__add__())
