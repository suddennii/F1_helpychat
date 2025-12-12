from src.pages.side_menu_page import SideMenuPage
from src.utils import driver, test_login_admin_success

class TestSideMenuNavigation:
    def setup_method(self, method, driver, test_login_admin_success):
        print("\n-- Setup: 드라이버 초기화 ---")
        self.driver = driver

        self.side_menu = SideMenuPage(self.driver)

    def teardown_method(self, method):
        print("\n--- Teardown: 드라이버 종료 ---")
        self.driver.quit()

    def test_navigate_to_new_chat(self):
        driver = self.driver

        print("✅ 액션: 에이전트 탐색 버튼 클릭 시도")
        self.side_menu.click_agent_search_btn()

        expected_agent_url = "/ai-helpy-chat/agents"
        current_url = driver.current_url
        self.assertIn(expected_agent_url, current_url, 
                      f"❌ 에이전트 탐색 페이지로 이동 실패. 현재 URL: {current_url}")
        print("✅ 검증 성공: 에이전트 탐색 페이지로 이동했습니다.")

        print("✅ 액션: 새 대화 버튼 클릭 시도")
        self.side_menu.click_new_chat_btn()

        expected_chat_url = "/ai-helpy-chat"
        current_url = driver.current_url
        # 원본 코드의 'assert agent_url in current_url' 오류 수정 및 검증
        self.assertIn(expected_chat_url, current_url, 
                      f"❌ 새 대화 페이지로 이동 실패. 현재 URL: {current_url}")
        print("✅ 검증 성공: 새 대화 페이지로 이동했습니다.")
