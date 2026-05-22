"""
UI automation testing menggunakan Selenium WebDriver.
Menggunakan situs the-internet.herokuapp.com yang disediakan
khusus untuk latihan automation testing.
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    """Setup dan teardown WebDriver untuk setiap test."""
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(10)

    yield driver

    driver.quit()


class TestLogin:
    """Test suite untuk pengujian fitur login."""

    URL = "https://the-internet.herokuapp.com/login"

    def test_login_page_loads(self, driver):
        """Memastikan halaman login berhasil dimuat."""
        driver.get(self.URL)
        assert "The Internet" in driver.title

    def test_login_with_valid_credentials(self, driver):
        """Login dengan kredensial valid harus berhasil."""
        driver.get(self.URL)
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        success_msg = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.success"))
        )
        assert "You logged into a secure area" in success_msg.text

    def test_login_with_invalid_username(self, driver):
        """Login dengan username salah harus gagal."""
        driver.get(self.URL)
        driver.find_element(By.ID, "username").send_keys("wronguser")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        error_msg = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.error"))
        )
        assert "Your username is invalid" in error_msg.text

    def test_login_with_invalid_password(self, driver):
        """Login dengan password salah harus gagal."""
        driver.get(self.URL)
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("wrongpassword")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        error_msg = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".flash.error"))
        )
        assert "Your password is invalid" in error_msg.text

    def test_logout_works(self, driver):
        """Logout setelah login berhasil mengarahkan ke halaman login."""
        driver.get(self.URL)
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".button.secondary.radius"))
        )
        driver.find_element(By.CSS_SELECTOR, ".button.secondary.radius").click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("/login")
        )
        assert "/login" in driver.current_url


class TestCheckboxes:
    """Test suite untuk pengujian checkbox."""

    URL = "https://the-internet.herokuapp.com/checkboxes"

    def test_checkbox_page_loads(self, driver):
        """Memastikan halaman checkbox berhasil dimuat."""
        driver.get(self.URL)
        checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
        assert len(checkboxes) == 2

    def test_check_first_checkbox(self, driver):
        """Centang checkbox pertama harus berhasil."""
        driver.get(self.URL)
        checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
        if not checkboxes[0].is_selected():
            checkboxes[0].click()
        assert checkboxes[0].is_selected()

    def test_uncheck_second_checkbox(self, driver):
        """Hapus centang checkbox kedua harus berhasil."""
        driver.get(self.URL)
        checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
        if checkboxes[1].is_selected():
            checkboxes[1].click()
        assert not checkboxes[1].is_selected()


class TestDropdown:
    """Test suite untuk pengujian dropdown."""

    URL = "https://the-internet.herokuapp.com/dropdown"

    def test_dropdown_page_loads(self, driver):
        """Memastikan halaman dropdown berhasil dimuat."""
        driver.get(self.URL)
        dropdown = driver.find_element(By.ID, "dropdown")
        assert dropdown.is_displayed()

    def test_select_option_from_dropdown(self, driver):
        """Memilih opsi dari dropdown harus berhasil."""
        from selenium.webdriver.support.ui import Select

        driver.get(self.URL)
        dropdown = Select(driver.find_element(By.ID, "dropdown"))
        dropdown.select_by_visible_text("Option 1")

        selected = dropdown.first_selected_option
        assert selected.text == "Option 1"