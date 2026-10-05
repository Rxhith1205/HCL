from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# =========================================================
# YOUR MOBILE NUMBER
# =========================================================
MOBILE_NUMBER = "9940700636"

# =========================================================
# START CHROME
# =========================================================
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
options.add_argument(r"--user-data-dir=C:\selenium\flipkart_profile")

driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 30)

try:

    # =====================================================
    # STEP 1 - OPEN FLIPKART
    # =====================================================
    print("STEP 1: Opening Flipkart...")
    driver.get("https://www.flipkart.com/")

    time.sleep(5)

    # =====================================================
    # STEP 2 - CLICK LOGIN
    # =====================================================
    print("STEP 2: Clicking Login...")

    login = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "//a[normalize-space()='Login'] | "
                "//button[normalize-space()='Login']"
            )
        )
    )

    driver.execute_script(
        "arguments[0].click();",
        login
    )

    print("Login clicked.")
    time.sleep(4)

    # =====================================================
    # STEP 3 - FIND PHONE NUMBER FIELD
    # =====================================================
    print("STEP 3: Finding phone number field...")

    phone_box = None

    # -----------------------------------------------------
    # METHOD 1: maxlength 10
    # -----------------------------------------------------
    selectors = [
        "//input[@maxlength='10']",
        "//input[@maxlength='10' and @type='text']",
        "//input[@maxlength='10' and @type='tel']",
        "//input[contains(@placeholder,'Phone')]",
        "//input[contains(@name,'phone')]",
        "//input[contains(@name,'mobile')]",
        "//input[contains(@autocomplete,'tel')]"
    ]

    for xpath in selectors:

        try:

            elements = driver.find_elements(
                By.XPATH,
                xpath
            )

            for element in elements:

                if element.is_displayed() and element.is_enabled():

                    phone_box = element

                    print("Phone field found using:")
                    print(xpath)

                    break

            if phone_box is not None:
                break

        except Exception:
            pass

    # -----------------------------------------------------
    # METHOD 2: Find input near "Phone Number" text
    # -----------------------------------------------------
    if phone_box is None:

        print("Trying Phone Number label...")

        try:

            phone_label = driver.find_element(
                By.XPATH,
                "//*[normalize-space()='Phone Number']"
            )

            # Search inputs in the label's nearby parent containers
            parents = [
                phone_label.find_element(By.XPATH, "./.."),
                phone_label.find_element(By.XPATH, "../.."),
                phone_label.find_element(By.XPATH, "../../.."),
                phone_label.find_element(By.XPATH, "../../../..")
            ]

            for parent in parents:

                inputs = parent.find_elements(
                    By.TAG_NAME,
                    "input"
                )

                for element in inputs:

                    if element.is_displayed() and element.is_enabled():

                        phone_box = element
                        print("Phone field found near Phone Number label.")
                        break

                if phone_box is not None:
                    break

        except Exception as e:

            print("Label search failed:", e)

    # =====================================================
    # METHOD 3: PRINT ALL VISIBLE INPUTS
    # =====================================================
    if phone_box is None:

        print()
        print("No phone field found using normal selectors.")
        print("Checking visible input elements...")
        print()

        all_inputs = driver.find_elements(
            By.TAG_NAME,
            "input"
        )

        count = 0

        for element in all_inputs:

            try:

                if element.is_displayed():

                    count += 1

                    print(
                        "VISIBLE INPUT",
                        count,
                        "| type =",
                        element.get_attribute("type"),
                        "| maxlength =",
                        element.get_attribute("maxlength"),
                        "| placeholder =",
                        element.get_attribute("placeholder"),
                        "| name =",
                        element.get_attribute("name"),
                        "| autocomplete =",
                        element.get_attribute("autocomplete")
                    )

            except Exception:
                pass

    # =====================================================
    # STEP 4 - ENTER MOBILE NUMBER
    # =====================================================
    if phone_box is None:

        print()
        print("==============================================")
        print("PHONE FIELD COULD NOT BE LOCATED")
        print("==============================================")
        print("Browser will remain open.")
        print()
        print("The important thing is that Login is working.")
        print("Do NOT close Chrome.")
        print()

        input("Press ENTER only after inspecting the page...")

    else:

        print()
        print("STEP 4: Entering mobile number...")

        # Scroll to field
        driver.execute_script(
            "arguments[0].scrollIntoView({block:'center'});",
            phone_box
        )

        time.sleep(1)

        # Click
        ActionChains(driver).move_to_element(
            phone_box
        ).click().perform()

        time.sleep(0.5)

        # Clear
        phone_box.clear()

        # Type mobile number
        phone_box.send_keys(MOBILE_NUMBER)

        print("Mobile number entered successfully!")

        time.sleep(2)

        # =================================================
        # STEP 5 - CLICK CONTINUE
        # =================================================
        print("STEP 5: Clicking Continue...")

        continue_button = wait.until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "//button[normalize-space()='Continue']"
                )
            )
        )

        driver.execute_script(
            "arguments[0].click();",
            continue_button
        )

        print("Continue clicked.")

        # =================================================
        # STEP 6 - OTP
        # =================================================
        print()
        print("==============================================")
        print("OTP SENT TO YOUR MOBILE")
        print("==============================================")

        time.sleep(3)

        otp = input(
            "Enter OTP received on your mobile: "
        ).strip()

        # =================================================
        # STEP 7 - FIND OTP INPUTS
        # =================================================
        print("STEP 6: Finding OTP fields...")

        all_inputs = driver.find_elements(
            By.TAG_NAME,
            "input"
        )

        otp_inputs = []

        for element in all_inputs:

            try:

                if not element.is_displayed():
                    continue

                if not element.is_enabled():
                    continue

                inputmode = (
                    element.get_attribute("inputmode")
                    or ""
                ).lower()

                maxlength = (
                    element.get_attribute("maxlength")
                    or ""
                )

                placeholder = (
                    element.get_attribute("placeholder")
                    or ""
                ).lower()

                aria = (
                    element.get_attribute("aria-label")
                    or ""
                ).lower()

                if (
                    inputmode == "numeric"
                    or "otp" in placeholder
                    or "otp" in aria
                    or maxlength == "1"
                ):
                    otp_inputs.append(element)

            except Exception:
                pass

        # =================================================
        # STEP 8 - TYPE OTP
        # =================================================
        if len(otp_inputs) == 1:

            otp_inputs[0].click()
            otp_inputs[0].send_keys(otp)

            print("OTP entered.")

        elif len(otp_inputs) >= len(otp):

            for i, digit in enumerate(otp):

                otp_inputs[i].click()
                otp_inputs[i].send_keys(digit)

            print("OTP entered into separate boxes.")

        else:

            print("OTP field not automatically detected.")
            print("Please enter OTP manually in Chrome.")

        # =================================================
        # STEP 9 - VERIFY
        # =================================================
        time.sleep(1)

        try:

            verify = wait.until(
                EC.element_to_be_clickable(
                    (
                        By.XPATH,
                        "//button[normalize-space()='Verify']"
                    )
                )
            )

            driver.execute_script(
                "arguments[0].click();",
                verify
            )

            print("Verify clicked.")

        except Exception:

            print("Verify button was not detected.")
            print("Please click Verify manually.")

        # =================================================
        # STEP 10 - FINISH
        # =================================================
        time.sleep(5)

        print()
        print("==============================================")
        print("LOGIN PROCESS COMPLETED")
        print("==============================================")

        input("Press ENTER to close Chrome...")

except Exception as e:

    print()
    print("==============================================")
    print("ERROR")
    print("==============================================")
    print(type(e).__name__)
    print(str(e))
    print()
    print("Chrome will remain open.")

    input("Press ENTER to close Chrome...")

finally:

    try:
        driver.quit()
    except:
        pass