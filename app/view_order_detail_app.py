import unittest, sys
sys.path.append('../testcase')
sys.path.append('../tools')
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from commonClass import *
import view_order_detail

class PythonOrgSearch(unittest.TestCase):

	def setUp(self):
		service = Service("C:\Program Files (x86)\chromedriver.exe")
		# webdriver.Chrome(service=service) | webdriver.Edge(service=service) | webdriver.Firefox(service=service) | webdriver.Safari(service=service)
		self.driver = webdriver.Chrome(service=service)
		self.driver.maximize_window()

	# testcase
	def test_application(self):
		testScenario = view_order_detail.TestCaseProcess(self.driver)
		testScenario.run()

	def tearDown(self):
		ErrorHandler.assert_element()
		self.driver.close()

if __name__ == "__main__":
    unittest.main()