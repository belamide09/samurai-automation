import time
from element import *
from commonClass import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
        self.baseEvent = BasicEvent(self.driver)
        self.assertEvent = AssertEvent(self.driver)

class TestCaseProcess(BasePage):

	def run(self):
		# target page
		self.driver.get("https://v2on55itlab.web-store.jp/admin")		
		# element checking time
		CommonExec.element_wait_time = 5

		self.baseEvent.set_text_value({
			"selector":"name",
			"locator":"admin_id",
			"value":"test",
			"log_status": True
		})

		self.baseEvent.set_text_value({
			"selector":"name",
			"locator":"admin_pass",
			"value":"test",
			"log_status": True
		})

		self.baseEvent.click_element({
			"selector":"class_name",
			"locator":"btn_login",
			"log_status": True,
			"time_delay": 1
		})

		self.baseEvent.mouse_over_element({
			"selector":"class_name",
			"locator":"shop_name_select",
			"log_status": True
		})


		self.baseEvent.click_element({
			"selector":"xpath",
			"locator":"//*[@id='the_menu']/li[1]/ul/li[3]/a",
			"log_status": True,
		})

		self.baseEvent.mouse_over_element({
			"selector":"xpath",
			"locator":"//*[@id='the_menu']/li[2]",
			"log_status": True,
			"time_delay": 1
		})

		self.baseEvent.click_element({
			"selector":"xpath",
			"locator":"//*[@id='the_menu']/li[2]/ul/li[2]/a",
			"log_status": True,
			"time_delay": 3
		})

		self.baseEvent.click_element({
			"selector":"xpath",
			"locator":"//*[@id='list_order']/table/tbody/tr[2]/td[2]/a",
			"log_status": True,
			"time_delay": 1
		})
		
		time.sleep(5);