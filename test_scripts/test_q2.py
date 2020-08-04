import sys, io
sys.path.append('..')
import unittest
from unittest.mock import patch
from answers.q2 import print_depth, a, b, emp_2

class TestQ2(unittest.TestCase):
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
        self.class_instance = emp_2
        self.diffrent_class_instance = b
        self.incorrect_type = [1, 2, 3]

    def test_simple(self):
        output = 'a 1\n'
        error = ''
        self.assert_print(print_depth, self.simple, output, error)

    def test_sample_input(self):
        output = ('key1 1\n'
                  'key2 1\n'
                  'key3 2\n'
                  'key4 2\n'
                  'key5 3\n'
                  'user: 3\n'
                  'first_name: 4\n'
                  'last_name: 4\n'
                  'father: 4\n'
                  'first_name: 5\n'
                  'last_name: 5\n'
                  'father: 5\n')
        error = ''
        self.assert_print(print_depth, self.sample_input_from_question, output, error)

    def test_instance_input(self):
        output = ('first_name: 1\n'
                  'last_name: 1\n'
                  'designation: 1\n'
                  'key1 2\n'
                  'key2 2\n'
                  'key3 3\n'
                  'key4 3\n'
                  'key5 4\n'
                  'user: 4\n'
                  'first_name: 5\n'
                  'last_name: 5\n'
                  'father: 5\n'
                  'first_name: 6\n'
                  'last_name: 6\n'
                  'father: 6\n')
        error = ''
        self.assert_print(print_depth, self.class_instance, output, error)

    def test_complex_input(self):
        output = ('key1 1\n'
                  'key2 1\n'
                  'key3 2\n'
                  'key4 2\n'
                  'key5 3\n'
                  'key6 3\n'
                  'key1 4\n'
                  'key2 4\n'
                  'key3 5\n'
                  'key4 5\n'
                  'key5 6\n'
                  'user: 6\n'
                  'first_name: 7\n'
                  'last_name: 7\n'
                  'father: 7\n'
                  'first_name: 8\n'
                  'last_name: 8\n'
                  'father: 8\n'
                  'cls: 1\n'
                  'first_name: 2\n'
                  'last_name: 2\n'
                  'designation: 2\n'
                  'key7 1\n'
                  'user: 2\n'
                  'first_name: 3\n'
                  'last_name: 3\n'
                  'father: 3\n'
                  'first_name: 4\n'
                  'last_name: 4\n'
                  'father: 4\n')
        error = ''
        self.assert_print(print_depth, self.diffrent_class_instance, output, error)

    def test_no_error(self):
        error = ''
        self.assert_error(print_depth, self.simple, error)

    def test_error(self):
        self.assertRaises(TypeError, print_depth, self.incorrect_type)

if __name__ == '__main__':
    unittest.main()
