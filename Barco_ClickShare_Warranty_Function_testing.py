from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from BeautifulReport import BeautifulReport
from webdriver_manager.chrome import ChromeDriverManager
import time
import unittest

## 設定Chrome的瀏覽器彈出時遵照的規則
## 這串設定是防止瀏覽器上頭顯示「Chrome正受自動控制」
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

## 關閉自動記住密碼的提示彈窗
options.add_experimental_option("prefs", {
                                "profile.password_manager_enabled": False, "credentials_enable_service": False})
##  Common Config
input_valid_value = "1863552437"
Description = "CLICKSHARE CX-50 SET NA"
Part_number = "R9861522NA"
Delivery_date = "05/07/2020 00:00:00"
Installation_date = "09/28/2020 09:16:22"
Warranty_end_date = "09/27/2021 09:16:22"
Service_contract_end_date = "01/01/0001 00:00:00"
Valid_error_without_input = "Please specify a serial number"
Valid_error_with_too_short = "Minimum 6 characters required"
Valid_error_others = "Please enter a valid serial number"
Result_message = "We couldn't find a product with this serial number. Please double-check the serial number and try again."
Result_message_not_clickshare = "We couldn't find a Clickshare product with this serial number. Please double-check the serial number and try again."

## Page selector
ACCEPT_COOKIE_BUTTON = "onetrust-accept-btn-handler"
INPUT_SEARCH_FIELD = "//input[@id='SerialNumber']"
CHECK_WARRANTY_BUTTON = ".btn--arrow"
RESULT_BOX_FIELD = ".c-bb-tile--bordered"

VALID_ERROR_NO_INPUT = "/html/body/div[1]/div[2]/section/div/div[1]/div/div[2]/div[1]/div[1]/span[1]"
VALID_ERROR_TOO_SHORT = "/html/body/div[1]/div[2]/section/div/div[1]/div/div[2]/div[1]/div[1]/span[2]"
VALID_ERROR_OTHERS = "/html/body/div[1]/div[2]/section/div/div[1]/div/div[2]/div[1]/div[1]/span[3]"
RESULT_ERROR_TITLE_TEXT = "/html/body/div[1]/div[2]/section/div/div[2]/div/div/div/h2/span"

RESULT_TITLE_TEXT = "//html/body/div[1]/div[2]/section/div/div[2]/div/div/article/div/h2/span"
RESULT_DESCRIPTION_TEXT = "//html/body/div[1]/div[2]/section/div/div[2]/div/div/article/div/div/div[2]/dl/dd[1]"
RESULT_PART_NUMBER_TEXT = "/html/body/div[1]/div[2]/section/div/div[2]/div/div/article/div/div/div[2]/dl/dd[2]"
RESULT_DELIVERY_DATE_TEXT = "/html/body/div[1]/div[2]/section/div/div[2]/div/div/article/div/div/div[2]/dl/dd[3]"
RESULT_INSTALLATION_DATE_TEXT = "/html/body/div[1]/div[2]/section/div/div[2]/div/div/article/div/div/div[2]/dl/dd[4]"
RESULT_WARRANTY_END_DATE_TEXT = "/html/body/div[1]/div[2]/section/div/div[2]/div/div/article/div/div/div[2]/dl/dd[5]"
RESULT_CONTRACT_END_DATE = "/html/body/div[1]/div[2]/section/div/div[2]/div/div/article/div/div/div[2]/dl/dd[6]"
RESULT_MESSAGE_TEXT = "/html/body/div[1]/div[2]/section/div/div[2]/div/div/div/div/p"


## 我們如果要將CASE拆成幾個不同的方法，需要用一個Unitest Class包覆起來
## 然後加上修飾符@classmethod
class Test(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        ## 定義WebDriver以及ActionsChain的變數便於後頭應用        
        self.driver = webdriver.Chrome(chrome_options=options)
        self.action = ActionChains(self.driver)
        self.URL = "https://www.barco.com/en/clickshare/support/warranty-info"
        self.driver.get(self.URL)
        self.driver.maximize_window()
    
    @classmethod
    def tearDownClass(self):
        ## 所有case跑完後就退出瀏覽器
        self.driver.quit()
        
    ## Test Case 的命名方式務必以「test_001_* ~ test_099_*」為主，讓Parser依照順序走
    ## """裡面的註解就是report產生後的CASE描述文字。
    def test_F001_RAT_Barco_clickshare_warrenty_input_empty(self):
        """
        [RAT]前往Barco,並輸入empty value "",並檢查結果
        """

        input_value = ""
        accept_cookie = self.driver.find_element_by_id(ACCEPT_COOKIE_BUTTON)
        input_search = self.driver.find_element_by_xpath(INPUT_SEARCH_FIELD)
        checkWarrenty_button = self.driver.find_element_by_css_selector(CHECK_WARRANTY_BUTTON)
        
        time.sleep(2)
        ## 等待頁面中的HTML，ID = 'search'這個元素出現後才執行動作
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of(input_search)
            )
        finally:
            time.sleep(2)
        ## 接受Accept cookie
        accept_cookie.click()

        ## 檢查SerialNumber欄位存在
        self.assertEqual(input_search.is_displayed(),True,"input field should be display")
        input_search.send_keys(input_value)

        ## 找到搜尋按鈕後，確認存在
        self.assertEqual(checkWarrenty_button.is_displayed(),True,"Get info button should be display")
        checkWarrenty_button.click()
        
        ## 等待結果秀出來
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, VALID_ERROR_NO_INPUT))
            )
        finally:
            time.sleep(2)

        ## 確認文字結果
        valid_error_result = self.driver.find_element_by_xpath(VALID_ERROR_NO_INPUT)
        self.assertEqual(valid_error_result.text,Valid_error_without_input,"Supposed to be as same as valid error message")

    def test_F002_RAT_Barco_clickshare_warrenty_input_too_short(self):
        """
        [RAT]前往Barco,並輸入太短,不足6碼 value "12345",並檢查結果
        """

        input_value = "12345"

        self.driver.refresh()
        time.sleep(3)
        
        ## 等待頁面中的HTML，ID = 'search'這個元素出現後才執行動作
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, INPUT_SEARCH_FIELD))
                #EC.visibility_of(input_search)
            )
        finally:
            time.sleep(2)

        input_search = self.driver.find_element_by_xpath(INPUT_SEARCH_FIELD)
        checkWarrenty_button = self.driver.find_element_by_css_selector(CHECK_WARRANTY_BUTTON)

        ## 檢查SerialNumber欄位存在
        self.assertEqual(input_search.is_displayed(),True,"input field should be display")
        input_search.send_keys(input_value)

        ## 找到搜尋按鈕後，確認存在
        self.assertEqual(checkWarrenty_button.is_displayed(),True,"Get info button should be display")
        checkWarrenty_button.click()
        
        ## 等待結果秀出來
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, VALID_ERROR_TOO_SHORT))
            )
        finally:
            time.sleep(2)

        ## 確認文字結果
        valid_error_result = self.driver.find_element_by_xpath(VALID_ERROR_TOO_SHORT)
        self.assertEqual(valid_error_result.text,Valid_error_with_too_short,"Supposed to be as same as valid error message")



    def test_F003_RAT_Barco_clickshare_warrenty_input_too_long(self):
        """
        [RAT]前往Barco,並輸入超過20位數 "123456789012345678901",並檢查結果
        """

        input_value = "123456789012345678901"
        self.driver.refresh()
        time.sleep(3)
        
        ## 等待頁面中的HTML，ID = 'search'這個元素出現後才執行動作
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, INPUT_SEARCH_FIELD))
                #EC.visibility_of(input_search)
            )
        finally:
            time.sleep(2)

        input_search = self.driver.find_element_by_xpath(INPUT_SEARCH_FIELD)
        checkWarrenty_button = self.driver.find_element_by_css_selector(CHECK_WARRANTY_BUTTON)

        ## 檢查SerialNumber欄位存在
        self.assertEqual(input_search.is_displayed(),True,"input field should be display")
        input_search.send_keys(input_value)

        ## 找到搜尋按鈕後，確認存在
        self.assertEqual(checkWarrenty_button.is_displayed(),True,"Get info button should be display")
        checkWarrenty_button.click()
        
        ## 等待結果秀出來
        try:
            element = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, RESULT_BOX_FIELD))
            )
        finally:
            time.sleep(2)
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,RESULT_ERROR_TITLE_TEXT))
            )
        finally:
            time.sleep(2)

        ## 確認文字結果
        valid_error_result = self.driver.find_element_by_xpath(VALID_ERROR_OTHERS)
        self.assertEqual(valid_error_result.text,Valid_error_others,"Supposed to be as same as valid error message")

        result_title = self.driver.find_element_by_xpath(RESULT_ERROR_TITLE_TEXT)
        result_Message = self.driver.find_element_by_xpath(RESULT_MESSAGE_TEXT)

        self.assertEqual(result_title.text,input_value,"Supposed to be as same as input value")
        self.assertEqual(result_Message.text,Result_message,"Supposed to be as same as result message")
        
    def test_F004_RAT_Barco_clickshare_warrenty_input_all_integer(self):
        """
        [RAT]前往Barco,並輸入全都是數字 "123456",並檢查結果
        """

        input_value = "123456"
        self.driver.refresh()
        time.sleep(3)
        
        ## 等待頁面中的HTML，ID = 'search'這個元素出現後才執行動作
        try:
            element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, INPUT_SEARCH_FIELD))
                #EC.visibility_of(input_search)
            )
        finally:
            time.sleep(2)

        input_search = self.driver.find_element_by_xpath(INPUT_SEARCH_FIELD)
        checkWarrenty_button = self.driver.find_element_by_css_selector(CHECK_WARRANTY_BUTTON)

        ## 檢查SerialNumber欄位存在
        self.assertEqual(input_search.is_displayed(),True,"input field should be display")
        input_search.send_keys(input_value)

        ## 找到搜尋按鈕後，確認存在
        self.assertEqual(checkWarrenty_button.is_displayed(),True,"Get info button should be display")
        checkWarrenty_button.click()
        
        ## 等待結果秀出來
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, RESULT_BOX_FIELD))
            )
        finally:
            time.sleep(2)
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,RESULT_ERROR_TITLE_TEXT))
            )
        finally:
            time.sleep(2)

        ## 確認文字結果
        result_title = self.driver.find_element_by_xpath(RESULT_ERROR_TITLE_TEXT)
        result_Message = self.driver.find_element_by_xpath(RESULT_MESSAGE_TEXT)

        self.assertEqual(result_title.text,input_value,"Supposed to be as same as input value")
        self.assertEqual(result_Message.text,Result_message,"Supposed to be as same as result message")

    def test_F005_RAT_Barco_clickshare_warrenty_input_all_alphabet(self):
        """
        [RAT]前往Barco,並輸入全都營文字母 "abcdef",並檢查結果
        """

        input_value = "abcdef"
        self.driver.refresh()
        time.sleep(3)
        
        ## 等待頁面中的HTML，ID = 'search'這個元素出現後才執行動作
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, INPUT_SEARCH_FIELD))
                #EC.visibility_of(input_search)
            )
        finally:
            time.sleep(2)

        input_search = self.driver.find_element_by_xpath(INPUT_SEARCH_FIELD)
        checkWarrenty_button = self.driver.find_element_by_css_selector(CHECK_WARRANTY_BUTTON)

        ## 檢查SerialNumber欄位存在
        self.assertEqual(input_search.is_displayed(),True,"input field should be display")
        input_search.send_keys(input_value)

        ## 找到搜尋按鈕後，確認存在
        self.assertEqual(checkWarrenty_button.is_displayed(),True,"Get info button should be display")
        checkWarrenty_button.click()
        
        ## 等待結果秀出來
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, RESULT_BOX_FIELD))
            )
        finally:
            time.sleep(2)
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,RESULT_ERROR_TITLE_TEXT))
            )
        finally:
            time.sleep(2)

        ## 確認文字結果
        result_title = self.driver.find_element_by_xpath(RESULT_ERROR_TITLE_TEXT)
        result_Message = self.driver.find_element_by_xpath(RESULT_MESSAGE_TEXT)

        self.assertEqual(result_title.text,input_value,"Supposed to be as same as input value")
        self.assertEqual(result_Message.text,Result_message,"Supposed to be as same as result message")

    def test_F006_RAT_Barco_clickshare_warrenty_input_Capital_alphabet(self):
        """
        [RAT]前往Barco,並輸入大小寫英文字母 "ABcdeF",並檢查結果
        """

        input_value = "ABcdeF"
        self.driver.refresh()
        time.sleep(3)
        
        ## 等待頁面中的HTML，ID = 'search'這個元素出現後才執行動作
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, INPUT_SEARCH_FIELD))
                #EC.visibility_of(input_search)
            )
        finally:
            time.sleep(2)

        input_search = self.driver.find_element_by_xpath(INPUT_SEARCH_FIELD)
        checkWarrenty_button = self.driver.find_element_by_css_selector(CHECK_WARRANTY_BUTTON)

        ## 檢查SerialNumber欄位存在
        self.assertEqual(input_search.is_displayed(),True,"input field should be display")
        input_search.send_keys(input_value)

        ## 找到搜尋按鈕後，確認存在
        self.assertEqual(checkWarrenty_button.is_displayed(),True,"Get info button should be display")
        checkWarrenty_button.click()
        
        ## 等待結果秀出來
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, RESULT_BOX_FIELD))
            )
        finally:
            time.sleep(2)
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,RESULT_ERROR_TITLE_TEXT))
            )
        finally:
            time.sleep(2)

        ## 確認文字結果
        result_title = self.driver.find_element_by_xpath(RESULT_ERROR_TITLE_TEXT)
        result_Message = self.driver.find_element_by_xpath(RESULT_MESSAGE_TEXT)

        self.assertEqual(result_title.text,input_value,"Supposed to be as same as input value")
        self.assertEqual(result_Message.text,Result_message,"Supposed to be as same as result message")

    def test_F007_RAT_Barco_clickshare_warrenty_input_dash(self):
        """
        [RAT]前往Barco,並輸入"-" 在裡面 "123456-",並檢查結果
        """

        input_value = "123456-"
        self.driver.refresh()
        time.sleep(3)
        
        ## 等待頁面中的HTML，ID = 'search'這個元素出現後才執行動作
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, INPUT_SEARCH_FIELD))
                #EC.visibility_of(input_search)
            )
        finally:
            time.sleep(2)

        input_search = self.driver.find_element_by_xpath(INPUT_SEARCH_FIELD)
        checkWarrenty_button = self.driver.find_element_by_css_selector(CHECK_WARRANTY_BUTTON)

        ## 檢查SerialNumber欄位存在
        self.assertEqual(input_search.is_displayed(),True,"input field should be display")
        input_search.send_keys(input_value)

        ## 找到搜尋按鈕後，確認存在
        self.assertEqual(checkWarrenty_button.is_displayed(),True,"Get info button should be display")
        checkWarrenty_button.click()
        
        ## 等待結果秀出來
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, RESULT_BOX_FIELD))
            )
        finally:
            time.sleep(2)
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH,RESULT_ERROR_TITLE_TEXT))
            )
        finally:
            time.sleep(2)

        ## 確認文字結果
        result_title = self.driver.find_element_by_xpath(RESULT_ERROR_TITLE_TEXT)
        result_Message = self.driver.find_element_by_xpath(RESULT_MESSAGE_TEXT)

        self.assertEqual(result_title.text,input_value,"Supposed to be as same as input value")
        self.assertEqual(result_Message.text,Result_message_not_clickshare,"Supposed to be as same as result message")

    def test_F008_RAT_Barco_clickshare_warrenty_input_punctuation(self):
        """
        [RAT]前往Barco,並輸入標點符號 在裡面 "!@#$%^",並檢查結果
        """

        input_value = "!@#$%^"
        self.driver.refresh()
        time.sleep(3)
        
        ## 等待頁面中的HTML，ID = 'search'這個元素出現後才執行動作
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, INPUT_SEARCH_FIELD))
                #EC.visibility_of(input_search)
            )
        finally:
            time.sleep(2)

        input_search = self.driver.find_element_by_xpath(INPUT_SEARCH_FIELD)
        checkWarrenty_button = self.driver.find_element_by_css_selector(CHECK_WARRANTY_BUTTON)

        ## 檢查SerialNumber欄位存在
        self.assertEqual(input_search.is_displayed(),True,"input field should be display")
        input_search.send_keys(input_value)

        ## 找到搜尋按鈕後，確認存在
        self.assertEqual(checkWarrenty_button.is_displayed(),True,"Get info button should be display")
        checkWarrenty_button.click()
        
        ## 等待結果秀出來
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, RESULT_BOX_FIELD))
            )
        finally:
            time.sleep(2)

        ## 確認文字結果
        valid_error_result = self.driver.find_element_by_xpath(VALID_ERROR_OTHERS)
        self.assertEqual(valid_error_result.text,Valid_error_others,"Supposed to be as same as valid error message")

        result_title = self.driver.find_element_by_xpath(RESULT_ERROR_TITLE_TEXT)
        result_Message = self.driver.find_element_by_xpath(RESULT_MESSAGE_TEXT)

        self.assertEqual(result_title.text,input_value,"Supposed to be as same as input value")
        self.assertEqual(result_Message.text,Result_message,"Supposed to be as same as result message")

    def test_F009_RAT_Barco_clickshare_warrenty_input_int_alpha_punctuation(self):
        """
        [RAT]前往Barco,並輸入數字、英文、標點符號 在裡面 "12abcd@",並檢查結果
        """

        input_value = "12abcd@"
        self.driver.refresh()
        time.sleep(3)
        
        ## 等待頁面中的HTML，ID = 'search'這個元素出現後才執行動作
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, INPUT_SEARCH_FIELD))
                #EC.visibility_of(input_search)
            )
        finally:
            time.sleep(2)

        input_search = self.driver.find_element_by_xpath(INPUT_SEARCH_FIELD)
        checkWarrenty_button = self.driver.find_element_by_css_selector(CHECK_WARRANTY_BUTTON)

        ## 檢查SerialNumber欄位存在
        self.assertEqual(input_search.is_displayed(),True,"input field should be display")
        input_search.send_keys(input_value)

        ## 找到搜尋按鈕後，確認存在
        self.assertEqual(checkWarrenty_button.is_displayed(),True,"Get info button should be display")
        checkWarrenty_button.click()
        
        ## 等待結果秀出來
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, RESULT_BOX_FIELD))
            )
        finally:
            time.sleep(2)

        ## 確認文字結果
        valid_error_result = self.driver.find_element_by_xpath(VALID_ERROR_OTHERS)
        self.assertEqual(valid_error_result.text,Valid_error_others,"Supposed to be as same as valid error message")

        result_title = self.driver.find_element_by_xpath(RESULT_ERROR_TITLE_TEXT)
        result_Message = self.driver.find_element_by_xpath(RESULT_MESSAGE_TEXT)

        self.assertEqual(result_title.text,input_value,"Supposed to be as same as input value")
        self.assertEqual(result_Message.text,Result_message,"Supposed to be as same as result message")

    def test_F010_RAT_Barco_clickshare_warrenty_input_non_ASCII_char(self):
        """
        [RAT]前往Barco,並輸入non-ASCII char 在裡面 "123456測試",並檢查結果
        """

        input_value = "123456測試"
        self.driver.refresh()
        time.sleep(3)
        
        ## 等待頁面中的HTML，ID = 'search'這個元素出現後才執行動作
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, INPUT_SEARCH_FIELD))
                #EC.visibility_of(input_search)
            )
        finally:
            time.sleep(2)

        input_search = self.driver.find_element_by_xpath(INPUT_SEARCH_FIELD)
        checkWarrenty_button = self.driver.find_element_by_css_selector(CHECK_WARRANTY_BUTTON)

        ## 檢查SerialNumber欄位存在
        self.assertEqual(input_search.is_displayed(),True,"input field should be display")
        input_search.send_keys(input_value)

        ## 找到搜尋按鈕後，確認存在
        self.assertEqual(checkWarrenty_button.is_displayed(),True,"Get info button should be display")
        checkWarrenty_button.click()
        
        ## 等待結果秀出來
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, RESULT_BOX_FIELD))
            )
        finally:
            time.sleep(2)

        ## 確認文字結果
        valid_error_result = self.driver.find_element_by_xpath(VALID_ERROR_OTHERS)
        self.assertEqual(valid_error_result.text,Valid_error_others,"Supposed to be as same as valid error message")

        result_title = self.driver.find_element_by_xpath(RESULT_ERROR_TITLE_TEXT)
        result_Message = self.driver.find_element_by_xpath(RESULT_MESSAGE_TEXT)

        self.assertEqual(result_title.text,input_value,"Supposed to be as same as input value")
        self.assertEqual(result_Message.text,Result_message,"Supposed to be as same as result message")

    def test_F011_RAT_Barco_clickshare_warrenty_input_fullwidth_chars(self):
        """
        [RAT]前往Barco,並輸入全形char 在裡面 "１２３４５６７",並檢查結果
        """

        input_value = "１２３４５６７"
        self.driver.refresh()
        time.sleep(3)
        
        ## 等待頁面中的HTML，ID = 'search'這個元素出現後才執行動作
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, INPUT_SEARCH_FIELD))
                #EC.visibility_of(input_search)
            )
        finally:
            time.sleep(2)

        input_search = self.driver.find_element_by_xpath(INPUT_SEARCH_FIELD)
        checkWarrenty_button = self.driver.find_element_by_css_selector(CHECK_WARRANTY_BUTTON)

        ## 檢查SerialNumber欄位存在
        self.assertEqual(input_search.is_displayed(),True,"input field should be display")
        input_search.send_keys(input_value)

        ## 找到搜尋按鈕後，確認存在
        self.assertEqual(checkWarrenty_button.is_displayed(),True,"Get info button should be display")
        checkWarrenty_button.click()
        
        ## 等待結果秀出來
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, RESULT_BOX_FIELD))
            )
        finally:
            time.sleep(2)

        ## 確認文字結果
        valid_error_result = self.driver.find_element_by_xpath(VALID_ERROR_OTHERS)
        self.assertEqual(valid_error_result.text,Valid_error_others,"Supposed to be as same as valid error message")

        result_title = self.driver.find_element_by_xpath(RESULT_ERROR_TITLE_TEXT)
        result_Message = self.driver.find_element_by_xpath(RESULT_MESSAGE_TEXT)

        self.assertEqual(result_title.text,input_value,"Supposed to be as same as input value")
        self.assertEqual(result_Message.text,Result_message,"Supposed to be as same as result message")


basedir = "D:\auto_test"
if __name__ == '__main__':
    # 取得資料夾目錄底下，符合後面任何副檔名為.py，並進行所有test的測試項目
    test_suite = unittest.defaultTestLoader.discover(
        basedir, pattern='Barco_ClickShare_Warranty_Function_testing.py')

    # 測試結果加入到 BeautifulReport 套件內
    result = BeautifulReport(test_suite)

    # 結果產生Report 檔案名稱為 filename, 敘述為 description, log_path 預設放在跟目錄底下就行
    result.report(filename='Barco_assignment_report_02',
                  description='ClickShare_warranty_feature_testing', log_path='D:\auto_test')

# 啟動自動化指令，在終端機輸入: & C:/Users/你的使用者帳號/AppData/Local/Programs/Python/Python39/python.exe d:/auto_test/firstCase.py
