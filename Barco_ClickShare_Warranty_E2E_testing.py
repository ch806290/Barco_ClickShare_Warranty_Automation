from selenium import webdriver
## BY: 也就是依照條件尋找元素中XPATH、CLASS NAME、ID、CSS選擇器等都會用到的Library
from selenium.webdriver.common.by import By
## keys: 鍵盤相關的Library
from selenium.webdriver.common.keys import Keys
## Select: 下拉選單相關支援，但前端框架UI工具不適用(ex: Quasar、ElementUI、Bootstrap)
from selenium.webdriver.support.ui import Select
## WebDriverWait: 等待頁面加載完成的顯性等待機制Library
from selenium.webdriver.support.ui import WebDriverWait
## ActionChains: 滑鼠事件相關
from selenium.webdriver.common.action_chains import ActionChains
## expected_conditions: 條件相關
from selenium.webdriver.support import expected_conditions as EC
## BeautifulReport: 產生自動測試報告套件
from BeautifulReport import BeautifulReport
## Chrome WebDriver 需要DRIVER Manager的支援
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
input_value = "1863552437"
Description = "CLICKSHARE CX-50 SET NA"
Part_number = "R9861522NA"
Delivery_date = "05/07/2020 00:00:00"
Installation_date = "09/28/2020 09:16:22"
Warranty_end_date = "09/27/2021 09:16:22"
Service_contract_end_date = "01/01/0001 00:00:00"

## Page selector
ACCEPT_COOKIE_BUTTON = "onetrust-accept-btn-handler"
INPUT_SEARCH_FIELD = "//input[@id='SerialNumber']"
CHECK_WARRANTY_BUTTON = ".btn--arrow"
RESULT_BOX_FIELD = ".c-bb-tile--bordered"

RESULT_TITLE_TEXT = "//html/body/div[1]/div[2]/section/div/div[2]/div/div/article/div/h2/span"
RESULT_DESCRIPTION_TEXT = "//html/body/div[1]/div[2]/section/div/div[2]/div/div/article/div/div/div[2]/dl/dd[1]"
RESULT_PART_NUMBER_TEXT = "/html/body/div[1]/div[2]/section/div/div[2]/div/div/article/div/div/div[2]/dl/dd[2]"
RESULT_DELIVERY_DATE_TEXT = "/html/body/div[1]/div[2]/section/div/div[2]/div/div/article/div/div/div[2]/dl/dd[3]"
RESULT_INSTALLATION_DATE_TEXT = "/html/body/div[1]/div[2]/section/div/div[2]/div/div/article/div/div/div[2]/dl/dd[4]"
RESULT_WARRANTY_END_DATE_TEXT = "/html/body/div[1]/div[2]/section/div/div[2]/div/div/article/div/div/div[2]/dl/dd[5]"
RESULT_CONTRACT_END_DATE = "/html/body/div[1]/div[2]/section/div/div[2]/div/div/article/div/div/div[2]/dl/dd[6]"


## 我們如果要將CASE拆成幾個不同的方法，需要用一個Unitest Class包覆起來
## 然後加上修飾符@classmethod
class Test(unittest.TestCase):
    @classmethod
    ## setUpClass這邊的設定是，可以讓所有Case進行過程中只開啟一次瀏覽器
    ## 執行時會依照這個順序循環一次 setUpClass > test > teardown
    ## self則是作為我們的區域參數來定義作用域
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
    def test_01_E2E_Barco_clickshare_warrenty_input_valid(self):
        """
        [E2E]前往Barco,並輸入合法serial number :1863552437,並檢查結果
        """

        accept_cookie = self.driver.find_element_by_id(ACCEPT_COOKIE_BUTTON)
        input_search = self.driver.find_element_by_xpath(INPUT_SEARCH_FIELD)
        checkWarrenty_button = self.driver.find_element_by_css_selector(CHECK_WARRANTY_BUTTON)
        result_box = self.driver.find_element_by_css_selector(RESULT_BOX_FIELD)
        
        
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
        ## 輸入valid input
        input_search.send_keys(input_value)


        ## 找到搜尋按鈕後，確認存在
        self.assertEqual(checkWarrenty_button.is_displayed(),True,"Get info button should be display")
        ## 點擊按鈕
        checkWarrenty_button.click()
        
        ## 等待結果秀出來
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, RESULT_BOX_FIELD))
            )
        finally:
            time.sleep(2)

        ## 確認文字結果
        result_title = self.driver.find_element_by_xpath(RESULT_TITLE_TEXT)
        result_Description = self.driver.find_element_by_xpath(RESULT_DESCRIPTION_TEXT)
        result_PartNumber = self.driver.find_element_by_xpath(RESULT_PART_NUMBER_TEXT)
        result_DeliveryDate = self.driver.find_element_by_xpath(RESULT_DELIVERY_DATE_TEXT)
        result_InstallationDate = self.driver.find_element_by_xpath(RESULT_INSTALLATION_DATE_TEXT)
        result_WarrantyEndDate = self.driver.find_element_by_xpath(RESULT_WARRANTY_END_DATE_TEXT)
        result_ContractEndDate = self.driver.find_element_by_xpath(RESULT_CONTRACT_END_DATE)


        self.assertEqual(result_title.text,input_value,"Supposed to be as same as input value")
        self.assertEqual(result_Description.text,Description,"Supposed to be as same as Description")
        self.assertEqual(result_PartNumber.text,Part_number,"Supposed to be as same as Part_number")
        self.assertEqual(result_DeliveryDate.text,Delivery_date,"Supposed to be as same as Delivery_date")
        self.assertEqual(result_InstallationDate.text,Installation_date,"Supposed to be as same as Installation_date")
        self.assertEqual(result_WarrantyEndDate.text,Warranty_end_date,"Supposed to be as same as Warranty_end_date")
        self.assertEqual(result_ContractEndDate.text,Service_contract_end_date,"Supposed to be as same as Service_contract_end_date")
    
        

# basedir就是存放所有TEST Case的目錄，讓它爬 pattern = '*.py'，所以要做哪個類別的測試就指定哪個前贅
basedir = "D:\Derrick_only\Practice\Homework\\auto_test"
if __name__ == '__main__':
    # 取得資料夾目錄底下，符合後面任何副檔名為.py，並進行所有test的測試項目
    test_suite = unittest.defaultTestLoader.discover(
        basedir, pattern='*.py')

    # 測試結果加入到 BeautifulReport 套件內
    result = BeautifulReport(test_suite)

    # 結果產生Report 檔案名稱為 filename, 敘述為 description, log_path 預設放在跟目錄底下就行
    result.report(filename='Barco_assignment_report_01',
                  description='ClickShare_warranty_feature_testing', log_path='D:\Derrick_only\Practice\Homework\\auto_test')

# 啟動自動化指令，在終端機輸入: & C:/Users/你的使用者帳號/AppData/Local/Programs/Python/Python39/python.exe d:/auto_test/firstCase.py
