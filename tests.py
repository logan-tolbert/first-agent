import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file 
from functions.run_python import run_python_file

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

class TestRunPythonFile(unittest.TestCase):
    def test_run_main(self):
        result = run_python_file("calculator", "main.py")
        print(result)
        self.assertIsInstance(result, str)
        self.assertFalse(result.startswith("Error:"))

    def test_run_tests_file(self):
        result = run_python_file("calculator", "tests.py")
        print(result)
        self.assertIsInstance(result, str)
        self.assertTrue("STDOUT:" in result or "STDERR:" in result or result.startswith("Error:"))

    def test_escape_directory_rejection(self):
        result = run_python_file("calculator", "../main.py")
        print(result)
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("Error:"))

    def test_nonexistent_file(self):
        result = run_python_file("calculator", "nonexistent.py")
        print(result)
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("Error:"))

if __name__ == "__main__":
    unittest.main()