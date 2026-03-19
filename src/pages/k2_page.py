from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class K12Note:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    # ===== locators
    TOOL_TAB = (By.XPATH, "//span[text()='도구']")
    SN_TAB = (By.XPATH, "//p[text()='세부 특기사항']")
    GRADE_LV = (By.XPATH, "(//div[@role='combobox'])[2]")
    CT_SUB = (By.XPATH, "(//div[@role='combobox'])[3]")
    TIME = (By.XPATH, "(//div[@role='combobox'])[4]")
    ACHIEVE = (By.XPATH, "//input[@name='achievement_criteria']") # 성취기준
    CT_TAB = (By.XPATH, "//p[text()='수업지도안']")
    BG_TAB = (By.XPATH, "//p[text()='행동특성 및 종합의견']")
    SCHOOL_LV = (By.XPATH, "//div[@role='combobox'][1]") # 학교급 필드
    SUB = (By.XPATH, "(//div[@role='combobox'])[2]") # 과목 필드
    LISTBOX = (By.XPATH, "//ul[@role='listbox']") # 각 필드의 리스트 박스
    CHO = (By.XPATH, "//li[@role='option' and normalize-space(text())='초등']")
    KUK = (By.XPATH, "//li[@role='option' and normalize-space(text())='국어']")
    BTN_CREATE = (By.XPATH,"//button[normalize-space(text())='자동 생성']" )
    BTN_RECREATE = (By.XPATH,"//button[normalize-space(text())='다시 생성']" )
    BTN_DOWNLOAD=(By.XPATH, "//a[normalize-space(text())='생성 결과 다운받기']")
    JOONG = (By.XPATH, "//li[@role='option' and normalize-space(text())='중등']")
    SOO = (By.XPATH, "//li[@role='option' and normalize-space(text())='수학']")
    BTN_LOGOUT = (By.XPATH, "//p[text()='로그아웃']")
    BTN_RV_HISTORY = (By.XPATH, "//a[text()='Remove history']")
    STOP_ICON = (By.XPATH, "//*[@data-testid='stopIcon']" )
    SN_SUCCESS_MESSAGE = (By.XPATH, "//p[contains(text(),'입력하신 내용 기반으로 세부 특기사항을 생성했습니다.')]")
    CT_SUCCESS_MESSAGE = (By.XPATH, "//p[contains(text(),'입력하신 내용 기반으로 수업 지도안을 생성했습니다.')]")
    BG_SUCCESS_MESSAGE = (By.XPATH, "//p[contains(text(),'입력하신 내용 기반으로 행동특성 및 종합의견을 생성했습니다.')]")

    STOP_MESSAGE = (By.XPATH, "//div[contains(text(),'요청에 의해 답변 생성을 중지했습니다.')]")
    ADD_INPUT = (By.XPATH, "//textarea[@name='teacher_comment']") # 추가 입력

    # ===== actions
    
    def click_tool_tab(self): # 도구 탭 선택
        self.wait.until(EC.element_to_be_clickable(self.TOOL_TAB)).click()
    
    def click_SN_tab(self): # 세부 특기사항 탭 선택
        self.wait.until(EC.element_to_be_clickable(self.SN_TAB)).click()
    
    def click_CT_tab(self): # 수업 지도안 탭 선택
        self.wait.until(EC.element_to_be_clickable(self.CT_TAB)).click()

    def click_BG_tab(self): # 행동특성 및 종합의견 탭 선택
        self.wait.until(EC.element_to_be_clickable(self.BG_TAB)).click()

    def click_sch_lv(self): # 학교급 필드 클릭
        self.wait.until(EC.element_to_be_clickable(self.SCHOOL_LV)).click()
    
    def click_grade_lv(self): # 학년 선택
        self.wait.until(EC.element_to_be_clickable(self.GRADE_LV)).click()

    def click_time(self): # 시간 선택
        self.wait.until(EC.element_to_be_clickable(self.TIME)).click()

    def click_sub(self): # 과목 선택
        self.wait.until(EC.element_to_be_clickable(self.SUB))
        sub_elem = self.driver.find_element(*self.SUB)
        sub_elem.click()

    def CT_click_sub(self): # 수업지도안 과목 선택
        self.wait.until(EC.element_to_be_clickable(self.CT_SUB))
        sub_elem = self.driver.find_element(*self.CT_SUB)
        sub_elem.click()
    
    
    def select_cho(self): # 초등 선택
        self.wait.until(EC.element_to_be_clickable(self.CHO)).click()
    
    def select_kuk(self): # 국어 선택
        self.wait.until(EC.element_to_be_clickable(self.KUK)).click()

    def ele_achieve(self): # 성취기준 요소
        return self.driver.find_element(*self.ACHIEVE)
    
    def send_achieve(self): # 성취기준 입력
        return self.driver.find_element(*self.ACHIEVE).send_keys("덧셈가능")
    
    
    def SN_upload_exel_succes(self): # 정상 엑셀 파일 업로드
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.abspath(os.path.join(base_dir, "..", "resources", "student_evaluation_template.xlsx"))
        print("업로드 파일 경로:", file_path)
        print("존재 여부:", os.path.exists(file_path))  # True여야 정상
        upload_input = self.driver.find_element(By.XPATH, "//input[@type='file']")
        upload_input.send_keys(file_path)

    def BG_upload_exel_succes(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.abspath(os.path.join(base_dir, "..", "resources", "student_record_generation_template.xlsx"))
        print("업로드 파일 경로:", file_path)
        print("존재 여부:", os.path.exists(file_path))  # True여야 정상

        upload_input = self.driver.find_element(By.XPATH, "//input[@type='file']")
        upload_input.send_keys(file_path)


    def result_download(self): # 생성 결과 다운 받기 버튼 RETURN
        return self.wait.until(EC.element_to_be_clickable(self.BTN_DOWNLOAD))
    
    def sn_wait_success_message(self): # SN 생성 완료 메세지
        return self.wait.until(EC.visibility_of_all_elements_located(self.SN_SUCCESS_MESSAGE))
    
    def ct_wait_success_message(self): # CT 생성 완료 메세지
        return self.wait.until(EC.visibility_of_all_elements_located(self.CT_SUCCESS_MESSAGE))
    
    def bg_wait_success_message(self):
        return self.wait.until(EC.visibility_of_all_elements_located(self.BG_SUCCESS_MESSAGE))
    
    '''DORP BOX LIST 확인'''
    def get_sch_lvs(self): # 학교급 드롭박스의 값들
        options = self.driver.find_elements(By.XPATH, "//li[@role='option']")
        return [opt.text for opt in options]
    
    def get_subs(self): # 과목 드롭박스 값들
        self.wait.until(EC.element_to_be_clickable(self.SUB))
        options = self.driver.find_elements(By.XPATH, "//li[@role='option']")
        return [opt.text for opt in options]
    
    def CT_get_subs(self): # 과목 드롭박스 값들
        self.wait.until(EC.element_to_be_clickable(self.CT_SUB))
        options = self.driver.find_elements(By.XPATH, "//li[@role='option']")
        return [opt.text for opt in options]
    
    def get_grade_lvs(self): # 학년 드롭박스 값들
        options = self.driver.find_elements(By.XPATH, "//li[@role='option']")
        return [opt.text for opt in options]
    
    def get_times(self): # 시간 드롭박스 값들
        options = self.driver.find_elements(By.XPATH, "//li[@role='option']")
        return [opt.text for opt in options]

    def close_listbox(self): # BODY 클릭해서 LIST 닫기
        self.driver.find_element(By.TAG_NAME, "body").click()
    
    '''CLEAR 확인'''
    def sch_lv(self): # (삭제 예정)학교급 필드의 TXT 
        return self.driver.find_element(*self.SCHOOL_LV).text
    
    def sub_lv(self): # (삭제 예정)과목 필드의 TXT 
        return self.driver.find_element(*self.SUB).text
    
    def sch_lv_txt(self): # 학교급 필드의 TXT 
        return self.driver.find_element(*self.SCHOOL_LV).text
    
    def sub_lv_txt(self): # 과목 필드의 TXT 
        return self.driver.find_element(*self.SUB).text

    def grade_lv_txt(self):  # 학년 필드의 TXT 
        return self.driver.find_element(*self.GRADE_LV).text
    
    def time_txt(self): # 시간 필드의 TXT 
        return self.driver.find_element(*self.TIME).text
    
    def logout(self): # 프로필 박스의 로그 아웃 클릭
        btn_logout = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(self.BTN_LOGOUT))
        btn_logout.click()

    def profile_click(self): # 프로필 클릭
        self.driver.find_element(By.CSS_SELECTOR, '.MuiAvatar-root').click()

    def wait_generation_complete(self): # Stop icon이 보이지 않을 때까지 기다림
        return self.wait.until(EC.invisibility_of_element_located(self.STOP_ICON))

    '''CREATE FAIL'''
    # PDF 파일 업로드 (미지원 파일 첨부)
    def upload_pdf_succes(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.abspath(os.path.join(base_dir, "..", "resources", "project_OT.pdf"))
        print("업로드 파일 경로:", file_path)
        print("존재 여부:", os.path.exists(file_path))  # True여야 정상

        upload_input = self.driver.find_element(By.XPATH, "//input[@type='file']")
        upload_input.send_keys(file_path)

    ## 보완 필요
    def upload_largefile_succes(self): # 대용량 파일 첨부이나 대용량 파일 생성이 안되어서 보류 중
        base_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.abspath(os.path.join(base_dir, "..", "resources", "large_test.xlsx"))
        print("업로드 파일 경로:", file_path)
        print("존재 여부:", os.path.exists(file_path))  # True여야 정상

        upload_input = self.driver.find_element(By.XPATH, "//input[@type='file']")
        upload_input.send_keys(file_path)
    
    def click_stop_icon(self): # STOP ICON 눌러서 생성 중지 하기
        self.wait.until(EC.element_to_be_clickable(self.STOP_ICON)).click()

    def get_stop_message_text(self): # 생성 중지 메세지 가져오기
        try:
            return self.wait.until(EC.visibility_of_element_located(self.STOP_MESSAGE)).text
        except:
            return None
        
    def send_add_input(self): # 추가입력란에 값 입력
        self.wait.until(EC.visibility_of_element_located(self.ADD_INPUT)).send_keys("테스트입니다.")
    
    '''RECREATE'''
    def select_joong(self): # 중등 선택
        self.wait.until(EC.element_to_be_clickable(self.JOONG)).click()
    
    def select_soo(self): # 수학 선택
        self.wait.until(EC.element_to_be_clickable(self.SOO)).click()
    
    '''자동 생성/다시 생성 버튼 클릭'''
    def create_btn(self):
            wait = WebDriverWait(self.driver, 10)
            # 1) "자동 생성" 버튼이 있는 경우
            try:
                btn_create = wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='자동 생성']")))
                btn_create.click()
                return
            except:
                pass
            # 2) "다시 생성" 버튼이 있는 경우
            try:
                btn_recreate = wait.until(
                    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='다시 생성']")))
                btn_recreate.click()

                # 모달 등장 대기
                modal = wait.until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, ".MuiDialog-root")))

                # 모달 내부의 다시 생성 버튼 클릭
                button_in_modal = wait.until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//div[contains(@class,'MuiDialog-root')]//button[normalize-space(text())='다시 생성']")))
                button_in_modal.click()
                return
            except:
                pass

            raise Exception("자동 생성/다시 생성 버튼을 찾지 못했습니다.")

    def get_create_btn(self):
        return WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space(text())='자동 생성']"))
    )

    def get_recreate_btn(self):
                return WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[normalize-space(text())='다시 생성']"))
    )

    def btn_recreate(self):
        return self.wait.until(EC.element_to_be_clickable(self.BTN_RECREATE))
    
    # 히스토리 지우기 (재로그인 위함)
    def rv_history(self):
        return self.wait.until(EC.element_to_be_clickable(self.BTN_RV_HISTORY))
    
    


    

    

