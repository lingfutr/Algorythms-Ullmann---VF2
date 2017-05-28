import unittest
import VF2
import networkx as nx

class TestUM(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_read(self):
        G1=nx.Graph()
        for i in range(4):
            G1.add_node(i)
        G1.add_edge(0,1)
        G1.add_edge(0,2)
        G1.add_edge(2,3)
        G2=VF2.read('C:\\Users\\Di\\PycharmProjects\\algorythms-Ullmann-VF2\\graphs\\graph1')
        self.assertEqual(G1.edges(),G2.edges())
        self.assertEqual(G1.order(), G2.order())




    def test_exist(self):
        set2=set([i*2 for i in range(6)])
        set1=set([i for i in range(8)])
        self.assertEqual(VF2.exist(set1,set2),[0,2,4,6])




    if __name__ == '__main__':
        unittest.main()