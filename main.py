import requests
from bs4 import BeautifulSoup
import re

# Your Google Apps Script API endpoint
API_URL = "https://script.google.com/macros/s/AKfycbzeQjgDyDx9iJqQPflDPHz7-Y2COSPTMEawqqvYgLdzYnxRlXLh4KNonlruuJUxR7Y55w/exec"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# ---------- CLEAN TITLE ----------
def clean_title(title):
    return re.sub(r"^\s*\d+\.\s*", "", title).strip()

# ---------- GENERIC TABLE PARSER ----------
def parse_table(soup, base_url, portal_name):
    table = soup.find("table", {"id": "activeTenders"})
    if not table:
        return []

    tenders = []
    rows = table.find_all("tr")

    for row in rows:
        tds = row.find_all("td")
        if len(tds) != 4:
            continue

        a_tag = tds[0].find("a")
        if not a_tag:
            continue

        title = clean_title(a_tag.text.strip())
        link = base_url + a_tag["href"]
        tender_id = tds[1].text.strip()
        start_date = tds[2].text.strip()
        end_date = tds[3].text.strip()

        tenders.append({
            "title": title,
            "link": link,
            "tender_id": tender_id,
            "start_date": start_date,
            "end_date": end_date,
            "portal": portal_name
        })

    return tenders


# ---------- SCRAPER 1: eProcure (GoI) ----------
def scrape_eprocure_goi():
    url = "https://eprocure.gov.in/eprocure/app"
    base = "https://eprocure.gov.in"

    html = requests.get(url, headers=HEADERS).text
    soup = BeautifulSoup(html, "html.parser")

    return parse_table(soup, base, "eProcure (GoI)")


# ---------- SCRAPER 2: Rajasthan eProcure ----------
def scrape_rajasthan():
    url = "https://eproc.rajasthan.gov.in/nicgep/app"
    base = "https://eproc.rajasthan.gov.in"

    html = requests.get(url, headers=HEADERS).text
    soup = BeautifulSoup(html, "html.parser")

    return parse_table(soup, base, "Rajasthan eProcure")


# ---------- SCRAPER 3: Delhi eProcure ----------
def scrape_delhi():
    url = "https://govtprocurement.delhi.gov.in/nicgep/app"
    base = "https://govtprocurement.delhi.gov.in"

    html = requests.get(url, headers=HEADERS).text
    soup = BeautifulSoup(html, "html.parser")

    return parse_table(soup, base, "Delhi eProcure")


# ---------- PUSH TO SHEET ----------
def push_to_google_sheet(tender):
    """
    Now main Sheet will treat TITLE as UNIQUE KEY.
    If title exists → Update the row.
    If not → Append as new entry.
    """

    try:
        response = requests.post(API_URL, json=tender)
        print(f"{tender['title']} → {response.text}")
    except Exception as e:
        print("Upload error:", e)


# ---------- MAIN ----------
if __name__ == "__main__":
    print("\n========== SCRAPING GOVT PORTALS ==========\n")

    tenders_goi = scrape_eprocure_goi()
    tenders_raj = scrape_rajasthan()
    tenders_delhi = scrape_delhi()

    all_tenders = tenders_goi + tenders_raj + tenders_delhi

    print(f"Total Tenders Collected: {len(all_tenders)}")

    print("\n========== UPLOADING TO GOOGLE SHEET ==========\n")

    for t in all_tenders:
        push_to_google_sheet(t)

    print("\n✔ Completed!\n")