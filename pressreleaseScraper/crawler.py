import os
import logging
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

import passwords

# CONFIGURATION
PRESS_RELEASE_URL = "https://ir.porchgroup.com/investors/news/default.aspx"
CHECK_ELEMENT_CSS_SELECTOR = "a.evergreen-item-title.evergreen-news-link.evergreen-news-headline-link"
LAST_SEEN_FILE = "last_press_release.txt"

EMAIL_SENDER = "lmikkelc5@gmail.com"
EMAIL_RECIPIENTS = ["lmikkelc5@gmail.com"]
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

# LOGGING SETUP
logging.basicConfig(
    filename="press_release_watcher.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)


def get_latest_press_release():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    )

    driver = None
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(PRESS_RELEASE_URL)
        driver.implicitly_wait(10)

        element = driver.find_element(By.CSS_SELECTOR, CHECK_ELEMENT_CSS_SELECTOR)
        link = element.get_attribute("href")

        return link

    except Exception as e:
        logging.error(f"Error using Selenium to fetch page: {e}")
        return None

    finally:
        if driver:
            driver.quit()


def load_last_seen():
    if os.path.exists(LAST_SEEN_FILE):
        with open(LAST_SEEN_FILE, "r") as f:
            return f.read().strip()
    return ""


def save_last_seen(link):
    with open(LAST_SEEN_FILE, "w") as f:
        f.write(link)


def send_email(link):
    subject = "📰 New Press Release Alert from Porch Group"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    body = f"A new press release is available as of {timestamp}:\n\n{link}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = ", ".join(EMAIL_RECIPIENTS)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, passwords.EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECIPIENTS, msg.as_string())
            logging.info(f"Email sent with link: {link}")
    except Exception as e:
        logging.error(f"Error sending email: {e}")


def check_for_new_press_release():
    latest_link = get_latest_press_release()
    if not latest_link:
        logging.warning("Could not retrieve press release link.")
        return

    last_seen = load_last_seen()
    if latest_link != last_seen:
        logging.info(f"New press release found: {latest_link}")
        send_email(latest_link)
        save_last_seen(latest_link)
    else:
        logging.info(f"No new press release. Last seen: {last_seen}")


def send_email_test():
    subject = "🛠️ Press Release Watcher Test Ping"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    body = f"This is a test ping to confirm the watcher is running. Timestamp: {timestamp}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = ", ".join(EMAIL_RECIPIENTS)

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_SENDER, passwords.EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECIPIENTS, msg.as_string())
            logging.info(f"Test email sent at {timestamp}")
    except Exception as e:
        logging.error(f"Error sending test email: {e}")

# MAIN
if __name__ == "__main__":
    logging.info("---- Running Press Release Watcher ----")
    check_for_new_press_release()
    # send_email_test()
