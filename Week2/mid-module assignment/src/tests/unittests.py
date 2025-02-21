import unittest
import sys
sys.path.append("../")
from recursion.recursive_floyd import recursive_floyd_warshall, MAX_LENGTH, NO_PATH, MIN_LEVEL

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
        
                
if __name__ == '__main__':
    unittest.main()