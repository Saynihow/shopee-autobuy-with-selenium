from datetime import datetime
from login import email,password,phone,cookie
from selenium.webdriver.chrome import options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import undetected_chromedriver as UC

# product_url = input("Enter Product URL: ")
# or you can replace product url here
product_url = "https://shopee.tw/product-i.11527054.15736618630"  # TODO change this

UC.TARGET_VERSION = 92
options = UC.ChromeOptions()
options.add_argument('--disable-extensions')

def loginWithEmail():
    driver.get("https://shopee.co.id/buyer/login")
    login_email = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, 'loginKey')))
    login_email.send_keys(email)
    login_password = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, 'password')))
    login_password.send_keys(password)
    login_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/form/div/div[2]/button')))
    driver.execute_script("arguments[0].click();", login_button)
    print('Login with Email Successful')
    time.sleep(3)
    if (driver.current_url == "https://shopee.co.id/verify/ivs?is_initial=true"):
        login_verify = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/div[2]/div/button')))
        driver.execute_script("arguments[0].click();", login_verify)
    time.sleep(3)
    print("Need email verification")
    while driver.current_url == "https://shopee.co.id/verify/link":
        continue
    time.sleep(3)
    print("Login Verification Successful")
    with open('cookie.txt', 'w') as f:
        f.write(driver.get_cookies())

def loginWithHandphone():
    driver.get("https://shopee.co.id/buyer/login/otp")
    login_phone = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.NAME, 'phone')))
    login_phone.send_keys(phone)
    login_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/form/div/div[2]/button')))
    driver.execute_script("arguments[0].click();", login_button)
    verif_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/aside/div[1]/div/div[2]/button[2]')))
    driver.execute_script("arguments[0].click();", verif_button)
    time.sleep(3)
    print("Need OTP verification")
    while driver.current_url == "https://shopee.co.id/buyer/login/otp":
        continue
    time.sleep(3)
    if (driver.current_url == "https://shopee.co.id/verify/ivs?is_initial=true"):
        login_verify = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div/div[1]/div/div[2]/div/button')))
        driver.execute_script("arguments[0].click();", login_verify)
    time.sleep(3)
    print("Need email verification")
    while driver.current_url == "https://shopee.co.id/verify/link":
        continue
    time.sleep(3)
    print("Login Verification Successful")
    with open('cookie.txt', 'w') as f:
        f.write(driver.get_cookies())

def loginWithCookie(driver):
    driver.get("https://shopee.tw")
    driver.add_cookie({'name': 'SPC_EC', 'value': cookie})
    driver.get_cookies()
    time.sleep(3)
    print("Login with Cookie Successful")

def buyProduct(driver):
    variant_option = WebDriverWait(driver, 600).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'撫子色')]")))  # TODO change this
    driver.execute_script("arguments[0].click();", variant_option)

    buy_button = WebDriverWait(driver, 600).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.btn.btn-solid-primary.btn--l.rvHxix')))
    driver.execute_script("arguments[0].click();", buy_button)
    print("Product has added to cart")

    checkout_button = WebDriverWait(driver, 600).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.shopee-button-solid.shopee-button-solid--primary')))
    driver.execute_script("arguments[0].click();", checkout_button)
    print("Checkout Cart")

    """
    # use this if you want to use ShopeePay Payment Method
    payment_method = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.checkout-payment-setting__payment-methods-tab > span:nth-child(1) > button')))
    driver.execute_script("arguments[0].click();", payment_method)
    payment_option = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.stardust-radio-button.stardust-radio-button--checked > div > div')))
    driver.execute_script("arguments[0].click();", payment_option)
    print("Using ShopeePay Payment Method")
    """


    pay_method_variant_option = WebDriverWait(driver, 900).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'信用卡/金融卡')]")))
    driver.execute_script("arguments[0].click();", pay_method_variant_option)
    print("select pay method")

    credit_card_variant_option = WebDriverWait(driver, 900).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'台新國際商業銀行')]")))
    driver.execute_script("arguments[0].click();", credit_card_variant_option)
    print("select credit card")

    order_button = WebDriverWait(driver, 900).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.stardust-button.stardust-button--primary.stardust-button--large._1qSlAe')))
    driver.execute_script("arguments[0].click();", order_button)
    print("Order created")

    # # use this if you want to use Bank BRI(auto) Payment Method
    # payment_method = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.checkout-payment-setting__payment-methods-tab > span:nth-child(2) > button')))
    # driver.execute_script("arguments[0].click();", payment_method)
    # payment_option = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.bank-transfer-category__body > div:nth-child(5) > div > div.stardust-radio-button > div > div')))
    # driver.execute_script("arguments[0].click();", payment_option)
    # print("Using Bank BRI(auto) Payment Method")

    """
    # use this if you want to use Bank Mandiri(auto) Payment Method
    payment_method = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.checkout-payment-setting__payment-methods-tab > span:nth-child(2) > button')))
    driver.execute_script("arguments[0].click();", payment_method)
    payment_option = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.bank-transfer-category__body > div:nth-child(3) > div > div.stardust-radio-button > div > div')))
    driver.execute_script("arguments[0].click();", payment_option)
    print("Using Bank Mandiri(auto) Payment Method")
    """

    """
    # use this if you want to use Bank BCA(auto) Payment Method
    payment_method = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.checkout-payment-setting__payment-methods-tab > span:nth-child(2) > button')))
    driver.execute_script("arguments[0].click();", payment_method)
    payment_option = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.bank-transfer-category__body > div:nth-child(2) > div > div.stardust-radio-button > div > div')))
    driver.execute_script("arguments[0].click();", payment_option)
    print("Using Bank BCA(auto) Payment Method")
    """

    """
    # use this if you want to use Bank BNI(auto) Payment Method
    payment_method = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.checkout-payment-setting__payment-methods-tab > span:nth-child(2) > button')))
    driver.execute_script("arguments[0].click();", payment_method)
    payment_option = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.bank-transfer-category__body > div:nth-child(4) > div > div.stardust-radio-button > div > div')))
    driver.execute_script("arguments[0].click();", payment_option)
    print("Using Bank BNI(auto) Payment Method")
    """
    
    # order_button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#main > div > div._193wCc > div._1WlhIE > div.f23wB9 > div.PC1-mc > div._3swGZ9 > button')))
    # driver.execute_script("arguments[0].click();", order_button)
    # print("Order has been created")

def getSecond(time_str):
    h, m, s = time_str.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)

def main():
    driver = UC.Chrome(options=options)

    # use this if you want to login with email-password ->
    # loginWithEmail()
    # use this if you want to login with phone -> loginWithHandphone()
    loginWithCookie(driver)

    hour_now = int(time.strftime("%H", time.localtime()))
    minute_now = int(time.strftime("%M", time.localtime()))
    second_now = int(time.strftime("%S", time.localtime()))
    driver.get(product_url)
    # hour_buy = int(input("Enter Hour to Buy Product: "))
    buy_time_s = str(input("Enter time (%Y-%m-%d %H:%M:%S) to Buy Product: "))
    # time_str = str(hour_buy) + ":" + str(minute_buy) + ":" + str(0)
    time_to_buy = datetime.strptime(buy_time_s, '%Y-%m-%d %H:%M:%S')
    time_now = datetime.now()
    # time_sleep = getSecond(time_str) - getSecond(time_str_now) - 60
    
    # print("Wait until the time to buy")
    # if (time_sleep > 0):
    #     time.sleep(time_sleep)
    print(f'{time_to_buy=}')
    print(f'{time_now=}')
    remaining_seconds = (time_to_buy - time_now).total_seconds()
    if remaining_seconds > 60:
        time.sleep(remaining_seconds - 60)
        print("Prepare time. Refreshing browser")
        driver.refresh()

    remaining_seconds_2 = (time_to_buy - datetime.now()).total_seconds()
    time.sleep(remaining_seconds_2)

    # print("Prepare time. Refreshing browser")
    # while minute_now != minute_buy:
    #     minute_now = int(time.strftime("%M", time.localtime()))
    #     driver.refresh()

    buyProduct(driver)

if __name__ == "__main__":
    main()