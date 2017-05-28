import unittest
import Ullmann
import networkx as nx

class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_read(self):
        matrix=[]
        matrix.append([0,1,1,0])
        matrix.append([1,0,0,0])
        matrix.append([1,0,0,1])
        matrix.append([0,0,1,0])
        self.assertEqual(Ullmann.read_matrix_from_file("C:\\Users\\Di\\PycharmProjects\\algorythms-Ullmann-VF2\\graphs\\graph1"),matrix)




    def test_condition1(self):
        matrix1=Ullmann.read_matrix_from_file("C:\\Users\\Di\\PycharmProjects\\algorythms-Ullmann-VF2\\graphs\\graph1")
        matrix2 = []
        matrix2.append([0, 1, 1, 0])
        matrix2.append([1, 0, 0, 0])
        matrix2.append([1, 0, 0, 1])
        matrix2.append([0, 0, 1, 0])
        self.assertEqual(Ullmann.condition1(matrix1,matrix2),True)
        matrix2[0][0]=1
        self.assertEqual(Ullmann.condition1(matrix1, matrix2), True)
        matrix2[0][1]=0
        self.assertEqual(Ullmann.condition1(matrix1, matrix2), False)

    def test_deg(self):
        matrix=Ullmann.read_matrix_from_file("C:\\Users\\Di\\PycharmProjects\\algorythms-Ullmann-VF2\\graphs\\graph1")
        self.assertEqual(Ullmann.deg(matrix,0),2)
        self.assertEqual(Ullmann.deg(matrix,1),1)
        self.assertEqual(Ullmann.deg(matrix,2),2)
        self.assertEqual(Ullmann.deg(matrix,3),1)


    def test_m0_init(self):
        matrix1=Ullmann.read_matrix_from_file("C:\\Users\\Di\\PycharmProjects\\algorythms-Ullmann-VF2\\graphs\\graph1")
        matrix2=Ullmann.read_matrix_from_file("C:\\Users\\Di\\PycharmProjects\\algorythms-Ullmann-VF2\\graphs\\graph2")
        matrix3=[]
        matrix3.append([0,1,0,1])
        matrix3.append([0,1,0,1])
        matrix3.append([1,1,1,1])
        matrix3.append([1,1,1,1])
        self.assertEqual(Ullmann.m0_init(matrix1,matrix2),matrix3)


    def test_vect_mul(self):
        pass

    def test_row(self):
        pass

    def test_column(self):
        pass

    def test_mul_matrix(self):
        matrix=[]
        matrix.append([1,0,0,2])
        matrix.append([0,0,1,0])
        matrix.append([0,1,2,0])
        matrix.append([1,0,0,1])
        matrix1=Ullmann.read_matrix_from_file("C:\\Users\\Di\\PycharmProjects\\algorythms-Ullmann-VF2\\graphs\\graph1")
        matrix2=Ullmann.read_matrix_from_file("C:\\Users\\Di\\PycharmProjects\\algorythms-Ullmann-VF2\\graphs\\graph2")
        self.assertEqual(Ullmann.mul_matrix(matrix1,matrix2),matrix)


    def test_transpose_matrix(self):
        pass



    def test_my_condition(self):
        matrix1 = []
        matrix1.append([1, 0, 0, 0])
        matrix1.append([0, 0, 1, 0])
        matrix1.append([0, 1, 0, 0])
        matrix1.append([0, 0, 0, 1])
        matrix2 = []
        matrix2.append([1, 0, 0, 0])
        matrix2.append([0, 0, 1, 0])
        matrix2.append([0, 1, 0, 0])
        matrix2.append([1, 0, 0, 1])

        self.assertEqual(Ullmann.my_condition(matrix1),True)
        self.assertEqual(Ullmann.my_condition(matrix2),False)


    if __name__ == '__main__':
        unittest.main()