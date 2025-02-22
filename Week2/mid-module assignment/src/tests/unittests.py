import unittest
import sys
from sys import maxsize
sys.path.append("../")
from recursion.recursive_floyd import recursive_floyd_warshall
from iterative.iterative_floyd import iterative_floyd


class test_recursive_floyd(unittest.TestCase):
    # This is a function that runs every time a test is executed. Like beforeAll() in jest.
    def setUp(self):
        self.no_path = maxsize
        
    
    def test_recursive_floyd_asserts_true_to_expected_value(self):
        # Arrange
        min_level = 0
        test_graph = [
            [0, 7, self.no_path, 8],
            [self.no_path, 0, 5, self.no_path],
            [self.no_path, self.no_path, 0, 2],
            [self.no_path, self.no_path, self.no_path, 0]
        ]
        expected_output = [
            [0, 7, 12, 8],
            [self.no_path, 0, 5, 7],
            [self.no_path, self.no_path, 0, 2],
            [self.no_path, self.no_path, self.no_path, 0]
        ]
        max_length = len(test_graph[0])
        
        # Act
        recursive_floyd_warshall(test_graph, min_level, min_level, min_level)
        
        #Assert
        for i in range(max_length):
            for j in range(max_length):
                self.assertEqual(test_graph[i][j], expected_output[i][j])
    
    def test_recursive_floyd_and_iterative_floyd_returns_same_output(self):
        # Arrange
        min_level = 0
        test_graph = [
            [0, 7, self.no_path, 8],
            [self.no_path, 0, 5, self.no_path],
            [self.no_path, self.no_path, 0, 2],
            [self.no_path, self.no_path, self.no_path, 0]
        ]
        
        # Act
        recursive_result = recursive_floyd_warshall(test_graph, min_level, min_level, min_level)
        iterative_result = iterative_floyd()

        # Assert
        self.assertEqual(recursive_result, iterative_result)
        self.assertIsNotNone(recursive_result)
        self.assertIsNotNone(iterative_result)
        
        
                
if __name__ == '__main__':
    unittest.main()