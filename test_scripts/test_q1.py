import sys, io
sys.path.append('..')
import unittest
from unittest.mock import patch
from answers.q1 import (recursive, recursive_with_map, non_recursive,
                        another_non_recursive, print_depth, a, b)

class TestQ1(unittest.TestCase):
    @patch('sys.stderr', new_callable=io.StringIO)
    @patch('sys.stdout', new_callable=io.StringIO)
    def assert_print(self, function, argument, expected_output, expected_err, mock_stdout, mock_stderr):
        function(argument)
        self.assertEqual(mock_stderr.getvalue(), expected_err)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stderr', new_callable=io.StringIO)
    def assert_error(self, function, argument, expected_err, mock_stderr):
        function(argument)
        self.assertEqual(mock_stderr.getvalue(), expected_err)

    @classmethod
    def setUpClass(self):
        self.simple = {'a': 1}
        self.sample_input_from_question = a
        self.bigger_nested_dict = b
        self.incorrect_type = [1, 2, 3]

    def test_simple(self):
        output = 'a 1\n'
        error = ''
        self.assert_print(recursive, self.simple, output, error)
        self.assert_print(recursive_with_map, self.simple, output, error)
        self.assert_print(non_recursive, self.simple, output, error)
        self.assert_print(another_non_recursive, self.simple, output, error)

    def test_sample_input(self):
        output = ('key1 1\n'
                  'key2 1\n'
                  'key3 2\n'
                  'key4 2\n'
                  'key5 3\n')
        error = ''
        self.assert_print(recursive, self.sample_input_from_question, output, error)
        self.assert_print(recursive_with_map, self.sample_input_from_question, output, error)
        self.assert_print(non_recursive, self.sample_input_from_question, output, error)
        self.assert_print(another_non_recursive, self.sample_input_from_question, output, error)


    def test_bigger_nested_dict(self):
        output = ('key0 1\n'
                  'key1 2\n'
                  'key2 2\n'
                  'key3 3\n'
                  'key4 3\n'
                  'key5 4\n'
                  'key6 1\n'
                  'key7 2\n'
                  'key8 2\n'
                  'key9 3\n'
                  'key10 3\n'
                  'key11 1\n'
                  'key12 1\n'
                  'key13 2\n')
        error = ''
        self.assert_print(recursive, self.bigger_nested_dict, output, error)
        self.assert_print(recursive_with_map, self.bigger_nested_dict, output, error)
        self.assert_print(another_non_recursive, self.bigger_nested_dict, output, error)

    def test_no_error(self):
        error = ''
        self.assert_error(recursive, self.simple, error)
        self.assert_error(recursive_with_map, self.simple, error)
        self.assert_error(non_recursive, self.simple, error)
        self.assert_error(another_non_recursive, self.simple, error)

    def test_error(self):
        self.assertRaises(TypeError, print_depth, self.incorrect_type)

if __name__ == '__main__':
    unittest.main()
