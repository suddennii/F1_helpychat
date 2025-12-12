from selenium.webdriver.common.by import By

class SideMenuPage:
    def __init__(self, driver):
        self.driver = driver

    # 새 대화 버튼
    NEW_CHAT_BTN = (By.XPATH, "//a[@href='/ai-helpy-chat']")
    # 검색 버튼
    SEARCH_HISTORY_BTN = (By.XPATH, "//span[contains(text(), '검색')]/ancestor::div[2]")
    # 도구 버튼
    TOOLS_BTN = (By.XPATH, "//a[@href='/ai-helpy-chat/tools']")
    # 에이전트 탐색 버튼
    AGENT_SEARCH_BTN = (By.XPATH, "//a[@href='/ai-helpy-chat/agents']")

    def click_new_chat_btn(self):
        self.driver.find_element(*self.NEW_CHAT_BTN).click()

    def click_search_history_btn(self):
        self.driver.find_element(*self.SEARCH_HISTORY_BTN).click()

    def click_tools_btn(self):
        self.driver.find_element(*self.TOOLS_BTN).click()

    def click_agent_search_btn(self):
        self.driver.find_element(*self.AGENT_SEARCH_BTN).click()