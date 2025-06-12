import unittest
from functions.get_files_info import get_files_info

class TestGetFilesInfoManualOutput(unittest.TestCase):
    def test_list_current_directory(self):
        output = get_files_info("calculator", ".")
        print(output)
        self.assertIsInstance(output, str)
        self.assertTrue(len(output) > 0 or output.startswith("Error"))

    def test_list_pkg_directory(self):
        output = get_files_info("calculator", "pkg")
        print(output)
        self.assertIsInstance(output, str)
        self.assertTrue(len(output) > 0 or output.startswith("Error"))

    def test_bin_directory_rejection(self):
        output = get_files_info("calculator", "/bin")
        print(output)
        self.assertIsInstance(output, str)
        self.assertTrue(output.startswith("Error"))

    def test_escape_directory_rejection(self):
        output = get_files_info("calculator", "../")
        print(output)
        self.assertIsInstance(output, str)
        self.assertTrue(output.startswith("Error"))


if __name__ == "__main__":
    unittest.main()
