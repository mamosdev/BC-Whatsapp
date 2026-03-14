import pandas as pd
import time
import random
import re

from tqdm import tqdm

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# =====================
# CONFIG
# =====================

FILE_EXCEL = "data.xlsx"
STATUS_TARGET = ["Lulus"]
# Isikan Link dibawah ini
LINK_GRUP = "https://chat.whatsapp.com/ISI_LINK"

DELAY_MIN = 6
DELAY_MAX = 10


# =====================
# TEMPLATE PESAN
# =====================

PESAN = """Assalamu'alaikum {nama}

Selamat! Anda dinyatakan LULUS seleksi PMBM MAN 1 Surakarta.

Silakan bergabung ke grup berikut:
{link}

Terima kasih."""


# =====================
# FORMAT NOMOR
# =====================

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

    return bool(re.fullmatch(r"62\d{9,13}", n))


# =====================
# LOAD DATA
# =====================

data = pd.read_excel(FILE_EXCEL)

data = data[data["Status"].isin(STATUS_TARGET)]

print("Total target:",len(data))


# =====================
# DRIVER
# =====================

driver = webdriver.Edge()

wait = WebDriverWait(driver,30)

driver.get("https://web.whatsapp.com")

input("Scan QR lalu tekan ENTER...")


# =====================
# LOG DATA
# =====================

log_sukses = []
log_gagal = []


# =====================
# LOOP KIRIM
# =====================

for _,row in tqdm(data.iterrows(), total=len(data)):

    nama = row["Nama Lengkap"]

    nomor = format_nomor(row["Telepon"])

    if not nomor_valid(nomor):

        log_gagal.append((nama,nomor,"Nomor tidak valid"))
        continue


    pesan = PESAN.format(
        nama=nama,
        link=LINK_GRUP
    )


    url = f"https://web.whatsapp.com/send?phone={nomor}"


    try:

        driver.get(url)


        box = wait.until(
            EC.presence_of_element_located(
                (By.XPATH,'//div[@contenteditable="true"]')
            )
        )


        for baris in pesan.split("\n"):
            box.send_keys(baris)
            box.send_keys(Keys.SHIFT, Keys.ENTER)

        box.send_keys(Keys.ENTER)


        log_sukses.append((nama,nomor))

        print("✓ Terkirim:",nama)


    except Exception as e:

        log_gagal.append((nama,nomor,"Gagal kirim"))

        print("✗ Gagal:",nomor)


    delay = random.randint(DELAY_MIN,DELAY_MAX)

    time.sleep(delay)


# =====================
# SIMPAN LOG
# =====================

pd.DataFrame(
    log_sukses,
    columns=["Nama","Nomor"]
).to_excel("sukses.xlsx",index=False)


pd.DataFrame(
    log_gagal,
    columns=["Nama","Nomor","Error"]
).to_excel("gagal.xlsx",index=False)


print("\n===================================")
print("SELESAI")
print("Sukses :",len(log_sukses))
print("Gagal  :",len(log_gagal))
print("===================================")
