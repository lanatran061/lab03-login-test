# 🧪 Lab 03 – Login Page Automation Test (Selenium)

## 📖 Overview
A simple automated testing project using **Python + Selenium WebDriver** to validate a sample login page.  
The script performs 6 automated test cases such as valid login, invalid password, empty fields, and UI link checks.

---

## 🎯 Objectives
- Practice **software testing automation** using Selenium.  
- Understand how to write and run functional test cases.  
- Capture screenshots as evidence for each test result.  
- Learn to use **locators** effectively (`By.ID`, `By.CSS_SELECTOR`).  

---

## ⚙️ Tools & Technologies
- **Python 3**
- **Selenium WebDriver**
- **webdriver-manager**
- **Google Chrome**
- **PlantUML** (for Use Case diagram)

---

## 🚀 Usage

```bash
# Run all Selenium tests
python3 test_login_form.py
```

---

## 🧩 Test Cases
| ID | Name | Description |
|----|------|--------------|
| TC01 | Login successfully | Valid username & password |
| TC02 | Invalid password | Wrong password entered |
| TC03 | Empty fields | No input provided |
| TC04 | Forgot password | Click the “Forgot password” link |
| TC05 | Sign-up | Click the “Create an account” link |
| TC06 | Social login | Click Facebook, Twitter, Google buttons |

---

## 💻 Installation & Setup

```bash
# Clone the project (or download)
git clone https://github.com/<your-username>/lab03-login-test.git
cd lab03-login-test
```

### (Optional) Create virtual environment
python3 -m venv venv
source venv/bin/activate

### Install dependencies
pip install selenium webdriver-manager

---

## 📜 License
This project is for **educational purposes only**.  
© 2025 — *Introduction to Software Engineering, Posts and Telecommunication Institute of Technology HCM.*

---

## 👤 Author
**Trần Nguyễn Lan Anh**  
Student — Posts and Telecommunication Institute of Technology HCM
📅 October 2025
