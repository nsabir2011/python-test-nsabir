import sys, io
sys.path.append('..')
import unittest
from unittest.mock import patch
from answers.q3 import Node, recursive, another_recursive, non_recursive, lca

class TestQ3(unittest.TestCase):

    @patch('sys.stderr', new_callable=io.StringIO)
    @patch('sys.stdout', new_callable=io.StringIO)
    def assert_print(self, function, arguments, expected_output, expected_err, mock_stdout, mock_stderr):
        function(*arguments)
        self.assertEqual(mock_stderr.getvalue(), expected_err)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stderr', new_callable=io.StringIO)
    def assert_error(self, function, arguments, expected_err, mock_stderr):
        function(*arguments)
        self.assertEqual(mock_stderr.getvalue(), expected_err)

    @classmethod
    def setUpClass(self):
        self.node_1 = Node(1, None)
        self.node_2 = Node(2, self.node_1)
        self.node_3 = Node(3, self.node_1)
        self.node_4 = Node(4, self.node_2)
        self.node_5 = Node(5, self.node_2)
        self.node_6 = Node(6, self.node_3)
        self.node_7 = Node(7, self.node_3)
        self.node_8 = Node(8, self.node_4)
        self.node_9 = Node(9, self.node_4)
        self.incorrect_type = [1, 2]
    
    def test_smaple_input_all(self):
        self.assertEqual(recursive(self.node_6, self.node_7, [], []).value, 3)
        self.assertEqual(recursive(self.node_3, self.node_7, [], []).value, 3)
        self.assertEqual(another_recursive(self.node_6, self.node_7, [], []).value, 3)
        self.assertEqual(another_recursive(self.node_3, self.node_7, [], []).value, 3)
        self.assertEqual(non_recursive(self.node_6, self.node_7).value, 3)
        self.assertEqual(non_recursive(self.node_3, self.node_7).value, 3)

    def test_same_node(self):
        error = ''
        self.assert_print(lca, (self.node_1, self.node_1), '1\n', error)
        self.assert_print(lca, (self.node_3, self.node_3), '3\n', error)
        self.assert_print(lca, (self.node_8, self.node_8), '8\n', error)
        self.assert_print(lca, (self.node_4, self.node_4), '4\n', error)
        self.assert_print(lca, (self.node_6, self.node_6), '6\n', error)

    def test_opposite_leaf(self):
        error = ''
        self.assert_print(lca, (self.node_8, self.node_7), '1\n', error)
        self.assert_print(lca, (self.node_9, self.node_6), '1\n', error)
        self.assert_print(lca, (self.node_5, self.node_6), '1\n', error)

    def test_same_parent(self):
        error = ''
        self.assert_print(lca, (self.node_8, self.node_9), '4\n', error)
        self.assert_print(lca, (self.node_2, self.node_3), '1\n', error)
        self.assert_print(lca, (self.node_7, self.node_6), '3\n', error)
        self.assert_print(lca, (self.node_4, self.node_5), '2\n', error)

    def test_father(self):
        error = ''
        self.assert_print(lca, (self.node_8, self.node_4), '4\n', error)
        self.assert_print(lca, (self.node_2, self.node_5), '2\n', error)
        self.assert_print(lca, (self.node_3, self.node_6), '3\n', error)
        self.assert_print(lca, (self.node_4, self.node_2), '2\n', error)

    def test_grandfather(self):
        error = ''
        self.assert_print(lca, (self.node_8, self.node_2), '2\n', error)
        self.assert_print(lca, (self.node_2, self.node_9), '2\n', error)
        self.assert_print(lca, (self.node_7, self.node_1), '1\n', error)

    def test_cousins(self):
        error = ''
        self.assert_print(lca, (self.node_4, self.node_6), '1\n', error)
        self.assert_print(lca, (self.node_7, self.node_5), '1\n', error)

    def test_uncle(self):
        error = ''
        self.assert_print(lca, (self.node_9, self.node_5), '2\n', error)
        self.assert_print(lca, (self.node_2, self.node_6), '1\n', error)
        self.assert_print(lca, (self.node_8, self.node_5), '2\n', error)

    def test_no_error(self):
        error = ''
        self.assert_error(lca, (self.node_1, self.node_1), error)

    def test_error(self):
        self.assertRaises(TypeError, lca, *self.incorrect_type)
        self.assertRaises(TypeError, lca, {'a'}, self.node_1)

if __name__ == '__main__':
    unittest.main()