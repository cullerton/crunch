import unittest
from prog_test.code import iter_commands
from types import GeneratorType

script = """# Get all users
SELECT * FROM users;

# Get all users with similar interests
SELECT * FROM
    users
WHERE interest IN ("robotics", "jui jitsu", "music");"""


class Test_iter_commands(unittest.TestCase):

    def test_generator_result(self):
        """test that result is a generator"""
        self.assertIsInstance(iter_commands(script), GeneratorType)

    def test_result_item_is_tuple(self):
        """Test that we get tuples in results"""
        result = iter_commands(script)
        for item in result:
            self.assertIsInstance(item, tuple)

    def test_values_in_result_item(self):
        """Test the we have valid items in result tuple"""
        result = iter_commands(script)
        for item in result:
            self.assertIsInstance(item[0], int)
            self.assertIsInstance(item[1], int)
            self.assertIsInstance(item[2], int)
            self.assertIsInstance(item[3], str)


if __name__ == '__main__':
    unittest.main()
