from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
from selenium.common.exceptions import NoSuchElementException

class Login(unittest.TestCase):

	def setUp(self) -> None:
		self.driver = webdriver.Chrome()
		self.driver.get("https://the-internet.herokuapp.com/")
		self.driver.maximize_window()
		self.driver.find_element(By.LINK_TEXT, "Form Authentication").click()
		self.driver.implicitly_wait(2)

	def tearDown(self) -> None:
		self.driver.quit()

	def test_01(self):
		current_link = self.driver.current_url
		assert current_link == "https://the-internet.herokuapp.com/login", f"Expected the URL: 'https://the-internet.herokuapp.com/login' but got: {current_link}"

	def test_02(self):
		page_title = self.driver.title
		assert page_title == "The Internet", f"Expected the title 'The Internet' but got: {page_title}"

	def test_03(self):
		the_text = self.driver.find_element(By.XPATH, "//h2").text
		assert the_text == "Login Page", f"Expected the text 'Login Page' but got: {the_text}"

	def test_04(self):
		self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').is_displayed()

	def test_05(self):
		the_link = self.driver.find_element(By.LINK_TEXT, "Elemental Selenium").get_attribute('href')
		assert  the_link == "http://elementalselenium.com/", f"Expected the link 'http://elementalselenium.com/' but got: {the_link}"

	def test_06(self):
		self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
		self.driver.find_element(By.ID, 'flash').is_displayed()

	def test_07(self):
		self.driver.find_element(By.ID, 'username').send_keys('tomsmiths')
		self.driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!?')
		self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
		the_message = self.driver.find_element(By.ID, 'flash').text
		assert "Your username is invalid!" in the_message, f"Expected the message: ' Your username is invalid! ' but got: {the_message}"

	def test_08(self):
		self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
		self.driver.find_element(By.XPATH, '//a[@class="close"]').click()
		self.driver.implicitly_wait(2)
		not self.driver.find_element(By.ID, 'flash').is_displayed()

	def test_09(self):
		got_list = self.driver.find_elements(By.XPATH, '//label')
		assert got_list[0].text == 'Username', f"Expected: 'Username' but got: {got_list[0].text}"
		assert got_list[1].text == 'Password', f"Expected: 'Password' but got: {got_list[1].text}"

	def test_10(self):
		self.driver.find_element(By.ID, 'username').send_keys('tomsmith')
		self.driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
		self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
		self.driver.implicitly_wait(3)
		new_url = self.driver.current_url
		assert '/secure' in new_url, f"Expected '/secure' in the new url but got this url: {new_url}"
		self.driver.find_element(By.XPATH, '//*[@class="flash success"]').is_displayed()

	def test_11(self):
		self.driver.find_element(By.ID, 'username').send_keys('tomsmith')
		self.driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
		self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
		self.driver.implicitly_wait(3)
		self.driver.find_element(By.CLASS_NAME, 'icon-signout').click()
		back_url = self.driver.current_url
		assert back_url == "https://the-internet.herokuapp.com/login", f"Expected the url: 'https://the-internet.herokuapp.com/login' but got: {back_url}"

	def test_12(self):
		brelock = self.driver.find_element(By.XPATH, '//h4').text.split()
		master_key = None
		i = 0
		while ((i < len(brelock)) and (master_key == None)):
			self.driver.find_element(By.ID, 'username').send_keys('tomsmith')
			self.driver.find_element(By.ID, 'password').send_keys(brelock[i])
			self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
			self.driver.implicitly_wait(2)
			try:
				self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').is_displayed()
			except NoSuchElementException:
				master_key = brelock[i]
				break
			i += 1
			self.driver.find_element(By.ID, 'username').clear()
			self.driver.find_element(By.ID, 'password').clear()
		if master_key != None:
			print(f"Parola secreta este {master_key}")
		else:
			print('Nu am reusit sa gasesc parola')

