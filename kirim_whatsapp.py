import pandas as pd
import time
import random
import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# ========================
# CONFIG
# ========================

FILE_EXCEL = "data.xlsx"
STATUS_TARGET = ["Berkas"]

# Isikan Link Group
LINK_GRUP = "https://chat.whatsapp.com/ISI_LINK"

DELAY_MIN = 7
DELAY_MAX = 12

# ========================
# PESAN
# ========================

PESAN = """Assalamu'alaikum {nama} 

Selamat! Anda dinyatakan LULUS seleksi PMBM MAN 1 Surakarta. 

Silakan bergabung ke grup berikut: 
{link} 

Terima kasih.
"""

# ========================
# FORMAT NOMOR
# ========================

def format_nomor(n):

    n = str(n)

    n = n.replace(" ","")
    n = n.replace("-","")

    if n.startswith("08"):
        n = "62"+n[1:]

    if n.startswith("+"):
        n = n[1:]

    return n

def nomor_valid(n):

    return bool(re.fullmatch(r"62\d{9,12}", n))

# ========================
# LOAD DATA
# ========================

data = pd.read_excel(FILE_EXCEL)

data = data[data["Status"].isin(STATUS_TARGET)]

print("Total target:",len(data))

# ========================
# DRIVER
# ========================

driver = webdriver.Edge()

wait = WebDriverWait(driver,30)

driver.get("https://web.whatsapp.com")

input("Scan QR lalu tekan ENTER...")

# ========================
# LOOP
# ========================

for _,row in data.iterrows():

    nama = row["Nama Lengkap"]
    nomor = format_nomor(row["Telepon"])

    if not nomor_valid(nomor):

        print("Skip nomor invalid:",nomor)
        continue

    pesan = PESAN.format(
        nama=nama,
        link=LINK_GRUP
    )

    url = f"https://web.whatsapp.com/send?phone={nomor}"

    try:

        driver.get(url)

        # tunggu chatbox muncul
        box = wait.until(
            EC.presence_of_element_located((By.XPATH,'//div[@contenteditable="true"]'))
        )

        # kirim pesan
        box.send_keys(pesan)
        box.send_keys(Keys.ENTER)

        print("Terkirim:",nama)

    except Exception as e:

        print("Gagal:",nomor)

    delay = random.randint(DELAY_MIN,DELAY_MAX)

    time.sleep(delay)

print("Selesai")