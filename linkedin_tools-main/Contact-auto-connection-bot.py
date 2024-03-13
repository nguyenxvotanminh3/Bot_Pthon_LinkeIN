# """                            @                  @
#                                @@                @@
#                                @@@              @ @
#                @              &@ @@            @  @              #
#                 @@            @@  @@         *@   @            @@
#                 @@@@          @@   &@       @@    @          @@@(
#                  @@ (@%       @@@(             ,@@@        @  @@
#                   @&  @@@   @@@@@&   &@@@@@&   @@@@@@   @@@   @
#         #          @   @@@     @@@      @.     @@@     @@@  *@             #
#          @@@     @@@      @@#                       @@@      @@@        @@
#           @ *@  @@        #@                         @@         @@  @ %@  #
#            ,  @@         @@                           @@         @@     #
#             @*          &@                             @/          @@
#           @@            @@                             @@            @@
#           @@            @@           S1X3NSE           @@            @@
#             @@          .@                             @           @@
#               @@         @@                           @@         @@
#                 @@@        @%                        @        @@@
#                    &@@       @@                   @@       @@/
#                        &@@@     @@@           @@@     @@@%
#                              @@@@@@#   *#,   %@@@@@@
#
#
#
# ******** NOTE ********
#
# My contribution to the project started by "Python Simplified".
#     - updated the code to correct deprecated errors;
#     - added a page cycler."""
#
# import pandas as pd
# from fileinput import close
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# import time
# from msedge.selenium_tools import Edge, EdgeOptions
# import pandas as pd
# from tkinter import Tk, filedialog
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# # Khởi tạo Edge WebDriver
# options = EdgeOptions()
# # Thêm các tùy chọn tại đây nếu cần thiết
#
# # Khởi tạo đối tượng Edge WebDriver
#
#
# # Sử dụng driver cho các hoạt động cần thiết
#
# #open linkedin.com
# driver = Edge(executable_path= 'D:\QT\msedgedriver.exe', options=options)
# # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# driver.get("https://linkedin.com/")
#
# time.sleep(2)
#
# #find UN/PW fields on the page
# username = driver.find_element(By.XPATH, "//input[@name='session_key']")
# password = driver.find_element(By.XPATH, "//input[@name='session_password']")
#
# #*************** STEP 1 ****************
#
# #********************LOGIN INFORMATION****************
# #Input login credentials
# username.send_keys('cn868733@gmail.com')
# password.send_keys('123456987cong')
#
# time.sleep(2)
#
# #click the submit button to login
# submit = driver.find_element(By.XPATH, "//button[@type='submit']").click()
#
# #the number of pages to cycle through
# n_pages = 8
#
# #looping through page numbers, by adding the the range as a str at the end of the URL for page=n
# for n in range(1,n_pages):
#
#     #*************** STEP 2 ****************
#
#
# # Tạo cửa sổ Tkinter để chọn file từ máy tính
#   root = Tk()
#   root.withdraw()  # Ẩn cửa sổ chọn file mặc định
#
#   # Yêu cầu người dùng chọn file từ máy tính
#   excel_file_path = filedialog.askopenfilename(title="Chọn file Excel", filetypes=[("Excel files", "*.xlsx")])
#
#   # Kiểm tra nếu người dùng không chọn file, thoát chương trình
#   if not excel_file_path:
#     print("Không chọn file.")
#     exit()
#   try:
#     data = pd.read_excel(excel_file_path)
#     print(data['LinkedIn_Link'])
#
#     #Enter the URL for 2nd Connections
#     for index, row in data.iterrows():
#       link = row['LinkedIn_Link']  # Thay 'LinkedIn_Link' bằng tên cột chứa URL LinkedIn
#       # Kiểm tra URL của người dùng trên LinkedIn
#
#       # Mở URL trên trình duyệt
#       driver.get(link)
#       time.sleep(2)
#       # Tìm nút "Connect" và nhấn vào nó nếu có
#       try:
#         all_buttons = driver.find_elements_by_tag_name("button")
#         connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]
#         for btn in connect_buttons:
#           driver.execute_script("arguments[0].click();", btn)
#
#           time.sleep(2)
#           add_a_note_button = driver.find_element(By.XPATH, '//button[@aria-label="Add a note"]')
#           driver.execute_script("arguments[0].click();", add_a_note_button)
#           time.sleep(2)
#           # #find and click the Send now button
#           # send = driver.find_element (By.XPATH, "//button[@aria-label = 'Send now']")
#           # driver.execute_script("arguments[0].click();", send)
#             # Tìm ô nhập note và điền nội dung
#           note_input = driver.find_element(By.XPATH, "//textarea[@name='message']")
#           note_input.send_keys("Xin chào! Tôi muốn kết nối với bạn.")
#           time.sleep(2)
#
#           # Click 'Send' button
#           send_note = driver.find_element(By.XPATH, '//button[@aria-label="Send now"]')
#           driver.execute_script("arguments[0].click();", send_note)
#           time.sleep(2)
#
#           #if the contact has secrurity settings enabled,
#           #limiting adding to people they know, close the window and skip
#           close_btn = driver.find_element (By.XPATH, "//button[@aria-label = 'Dismiss']")
#           driver.execute_script("arguments[0].click();", close_btn)
#
#           time.sleep(2)
#       except Exception as e:
#         print(f"Không tìm thấy nút Connect hoặc có lỗi: {e}")
#   except Exception as e:
#         print(f"Không tìm thấy nút Connect hoặc có lỗi: {e}")
#
#
#
#           # Xử lý lỗi nếu không tìm thấy nút Connect hoặc có lỗi khác
#     # #Enter the URL for 2nd Connections
#     # driver.get("https://www.linkedin.com/search/results/people/?network=%5B%22S%22%5D&origin=FACETED_SEARCH&page=" + str(n))
#
#     # time.sleep(2)
#
#     # #find the connect button
#     # all_buttons = driver.find_elements_by_tag_name("button")
#     # connect_buttons = [btn for btn in all_buttons if btn.text == "Connect"]
#
#     # #loop through all connect buttons
#     # for btn in connect_buttons:
#     #     driver.execute_script("arguments[0].click();", btn)
#
#     #     time.sleep(2)
#
#     #     #find and click the Send now button
#     #     send = driver.find_element (By.XPATH, "//button[@aria-label = 'Send now']")
#     #     driver.execute_script("arguments[0].click();", send)
#
#     #     #if the contact has secrurity settings enabled,
#     #     #limiting adding to people they know, close the window and skip
#     #     close_btn = driver.find_element (By.XPATH, "//button[@aria-label = 'Dismiss']")
#     #     driver.execute_script("arguments[0].click();", close_btn)
#
#     #     time.sleep(2)
#
#
#
