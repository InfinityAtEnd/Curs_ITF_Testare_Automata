from C_09_TEMA import Login
import unittest
import HtmlTestRunner

class Tema10Suite(unittest.TestCase):
	def test_suite(self):
		for_testing = unittest.TestSuite()
		for_testing.addTest(unittest.defaultTestLoader.loadTestsFromTestCase(Login))
		runner = HtmlTestRunner.HTMLTestRunner(combine_reports=True)
		runner.run(for_testing)