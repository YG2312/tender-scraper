# 🚀 Tender Scraper Automation System

An automated Python-based scraper that extracts live tender data from multiple Indian government portals and syncs it directly to Google Sheets.

---

## 🔥 Features

- 📡 Scrapes multiple government portals:
  - eProcure (GoI)
  - Rajasthan eProcure
  - Delhi eProcure

- ⚡ Real-time data extraction
- 🔄 Auto-sync with Google Sheets via API
- 🧠 Smart duplicate handling (based on title)
- ⏱️ Ready for cron-based automation (Render)

---

## 🛠️ Tech Stack

- Python
- Requests
- BeautifulSoup (lxml parser)
- Google Apps Script (for Sheets API)
- Render (for scheduling / cron jobs)

---

## 📊 Output

Each tender includes:
- Title
- Tender ID
- Start Date
- End Date
- Source Portal
- Direct Link

---

## ⚙️ How It Works

1. Scrapes HTML content from tender portals
2. Parses structured data from tables
3. Cleans and formats the data
4. Sends data to Google Sheets via API
5. Updates or inserts records automatically

---

## 🚀 Deployment

This project is deployed using **Render Cron Jobs**:

- Runs automatically at scheduled intervals
- No manual execution needed
- Fully serverless automation

---

## 📌 Use Cases

- Businesses tracking government tenders
- Automation agencies
- Data collection pipelines
- Lead generation systems

---

## 🔮 Future Improvements

- Add more state portals
- Replace scraping with direct API extraction
- Build dashboard UI for users
- Convert into SaaS product

---

## 👨‍💻 Author

Built by Yash Gupta
