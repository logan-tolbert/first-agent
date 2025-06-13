import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


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

class TestGetFileContent(unittest.TestCase):
    def test_main_file(self):
        result = get_file_content("calculator", "main.py")
        print(result)
        self.assertIsInstance(result, str)

    def test_pkg_calculator_file(self):
        result = get_file_content("calculator", "pkg/calculator.py")
        print(result)
        self.assertIsInstance(result, str)

    def test_bin_cat_file(self):
        result = get_file_content("calculator", "/bin/cat")
        print(result)
        self.assertIsInstance(result, str)

class TestWriteFile(unittest.TestCase):
    def test_write_existing_file(self):
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(result)
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("Successfully") or result.startswith("Error:"))

    def test_write_nested_file(self):
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(result)
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("Successfully") or result.startswith("Error:"))

    def test_write_outside_directory(self):
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(result)
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("Error:"))

if __name__ == "__main__":
    unittest.main()