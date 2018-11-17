import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class team1cal2_ATS(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

   def test_cal2(self):
       user = "instructor"
       pwd = "instructor1a"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://127.0.0.1:8000/admin")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       elem.send_keys(Keys.RETURN)
       driver.get("http://127.0.0.1:8000/admin")
       assert "Logged In"
       time.sleep(5)
       elem = driver.find_element_by_xpath("/html/body/div/div[2]/div[1]/div[2]/table/tbody/tr[2]/td[1]/a").click()
       time.sleep(3)
       elem = driver.find_element_by_id("id_cust_name")
       elem.send_keys("b")
       elem = driver.find_element_by_id("id_product")
       elem.send_keys("tester")
       elem = driver.find_element_by_id("id_p_description")
       elem.send_keys("this is a test product decsription")
       elem = driver.find_element_by_id("id_quantity")
       elem.send_keys("2")
       elem = driver.find_element_by_id("id_charge")
       elem.send_keys("23.00")
       # elem = driver.find_element_by_id("id_account_number")
       # elem.send_keys("23")
       # elem = driver.find_element_by_id("id_city")
       # elem.send_keys("omaha")
       # elem = driver.find_element_by_id("id_state")
       # elem.send_keys("NE")
       # elem = driver.find_element_by_id("id_zipcode")
       # elem.send_keys("68104")
       # elem = driver.find_element_by_id("id_phone_number")
       # elem.send_keys("5555555555")
       time.sleep(3)
       elem = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div/form/div/div/input[1]").click()
       time.sleep(3)
       driver.get("http://127.0.0.1:8000/product_list")
       time.sleep(7)


   def tearDown(self):
       self.driver.close()

if __name__ == "__main__":
   unittest.main()