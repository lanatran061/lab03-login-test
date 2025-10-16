import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# ===== Global configuration =====
BASE_URL = "file://" + os.path.abspath("test_login_page.html")
SCREENSHOT_DIR = "screenshots"
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

USERNAME = "admin"
PASSWORD = "1234"

# ===== Hàm khởi tạo trình duyệt (setup) =====
def get_driver():
    """Mở Chrome và trả về đối tượng điều khiển trình duyệt."""
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),  # Tự động setup ChromeDriver
        options=options
    )
    driver.maximize_window()  # Phóng to cửa sổ Chrome
    return driver


# ===== Screenshot helper =====
def snap(driver, name):
    """Chụp ảnh màn hình trang hiện tại và lưu trong thư mục screenshots/."""
    path = os.path.join(SCREENSHOT_DIR, f"{name}.png")
    driver.save_screenshot(path)
    print(f"Screenshot saved: {path}")


# ===== Test 1: Valid login =====
def test_login_success():
    driver = get_driver()
    driver.get(BASE_URL)  # Mở trang login

    # Nhập username và password hợp lệ
    driver.find_element(By.ID, "username").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "login").click()

    time.sleep(1)  # Chờ trang phản hồi
    msg = driver.find_element(By.ID, "message").text
    snap(driver, "login_success")

    assert "Login successful" in msg
    print("✅ Test 1: Login success → PASS")
    driver.quit()



# ===== Test 2: Invalid password =====
def test_invalid_password():
    driver = get_driver()
    driver.get(BASE_URL)

    driver.find_element(By.ID, "username").send_keys(USERNAME)
    driver.find_element(By.ID, "password").send_keys("wrongpass")
    driver.find_element(By.ID, "login").click()

    time.sleep(1)
    msg = driver.find_element(By.ID, "message").text
    snap(driver, "invalid_password")

    assert "Invalid" in msg
    print("✅ Test 2: Invalid password → PASS")
    driver.quit()


# ===== Test 3: Empty fields =====
def test_empty_fields():
    driver = get_driver()
    driver.get(BASE_URL)

    driver.find_element(By.ID, "login").click()
    time.sleep(1)

    msg = driver.find_element(By.ID, "message").text
    snap(driver, "empty_fields")

    assert "Please enter" in msg
    print("✅ Test 3: Empty fields → PASS")
    driver.quit()


# ===== Test 4: Forgot password link =====
def test_forgot_password_link():
    driver = get_driver()
    driver.get(BASE_URL)

    driver.find_element(By.ID, "forgot").click()
    time.sleep(1)
    msg = driver.find_element(By.ID, "message").text
    snap(driver, "forgot_password")

    assert "Forgot password" in msg
    print("✅ Test 4: Forgot Password → PASS")
    driver.quit()


# ===== Test 5: Sign-up link =====
def test_signup_link():
    driver = get_driver()
    driver.get(BASE_URL)

    driver.find_element(By.ID, "signup").click()
    time.sleep(1)
    msg = driver.find_element(By.ID, "message").text
    snap(driver, "signup")

    assert "Sign-up" in msg
    print("✅ Test 5: Sign Up → PASS")
    driver.quit()


# ===== Test 6: Social login buttons =====
def test_social_buttons():
    driver = get_driver()
    driver.get(BASE_URL)

    socials = ["fb", "tw", "gg"]
    for s in socials:
        driver.find_element(By.ID, s).click()
        time.sleep(0.5)
        msg = driver.find_element(By.ID, "message").text
        snap(driver, f"social_{s}")

        assert "login clicked" in msg
        print(f"✅ Test 6: Social button {s.upper()} → PASS")

    driver.quit()


# ===== Run all tests =====
if __name__ == "__main__":
    print("\n🚀 Running Selenium tests on local HTML page ...\n")
    test_login_success()
    test_invalid_password()
    test_empty_fields()
    test_forgot_password_link()
    test_signup_link()
    test_social_buttons()
    print("\n🎯 All 6 tests completed successfully.\n")
