import unittest
import sys
sys.path.append("../")
from recursion.recursive_floyd import recursive_floyd_warshall, MAX_LENGTH, NO_PATH, MIN_LEVEL
from iterative.iterative_floyd import iterative_floyd

class test_recursive_floyd(unittest.TestCase):
    # This is a function that runs every time a test is executed. Like beforeAll() in jest.
    def setUp(self):
        self.max_length = MAX_LENGTH
        self.min_level = MIN_LEVEL
    
    def test_recursive_floyd_asserts_true_to_expected_value(self):
        # Arrange
        test_graph = [
            [0, 7, NO_PATH, 8],
            [NO_PATH, 0, 5, NO_PATH],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]
        ]
        
        expected_output = [
            [0, 7, 12, 8],
            [NO_PATH, 0, 5, 7],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]
        ]
        
        # Act
        recursive_floyd_warshall(test_graph, self.min_level, self.min_level, self.min_level)
        
        #Assert
        for i in range(self.max_length):
            for j in range(self.max_length):
                self.assertEqual(test_graph[i][j], expected_output[i][j])
    
    def test_recursive_floyd_and_iterative_floyd_returns_same_output(self):
        
        # Arrange
        graph_used_in_iterative_floyd = [
            [0,   7,  NO_PATH, 8],
            [NO_PATH,  0,  5,  NO_PATH],
            [NO_PATH, NO_PATH, 0,   2],
            [NO_PATH, NO_PATH, NO_PATH, 0]]
        
        # Act
        recursive_result = recursive_floyd_warshall(graph_used_in_iterative_floyd, self.min_level, self.min_level, self.min_level)
        iterative_result = iterative_floyd()

        # Assert
        self.assertEqual(recursive_result, iterative_result)
        self.assertIsNotNone(recursive_result)
        self.assertIsNotNone(iterative_result)
        
        
                
if __name__ == '__main__':
    unittest.main()