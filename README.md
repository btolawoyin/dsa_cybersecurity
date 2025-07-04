
# 📱 Android Forensics Timeline Correlation Tool

This project is part of a cybersecurity forensics investigation. It provides a Python-based tool for **correlating Android call logs, SMS records, and app usage patterns** from CSV data exported during mobile device analysis.

## 🔍 Project Purpose

The objective is to identify behavioural patterns by analysing:
- Call activity (incoming, outgoing, missed)
- SMS communications (sent and received)
- App usage events (open, close, time in foreground)

This helps forensic investigators and analysts visualise user activity over time, detect suspicious patterns, and provide context to specific events.

---

## 🗂️ Project Structure

```
ForensicsAnalysis/
│
├── data/                      # Folder for CSV datasets (not tracked by Git)
│   ├── CallLog.csv
│   ├── SMS_Messages.csv
│   └── AppUsage.csv
│
├── main.py                    # Main Python script for correlation and visualisation
├── requirements.txt           # Python dependencies
├── .gitignore                 # Files/folders excluded from Git
└── README.md                  # This file
```

---

## 🛠️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/btolawoyin/dsa_cybersecurity.git
cd dsa_cybersecurity/ForensicsAnalysis
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv .venv
.venv\Scripts\Activate     # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your CSV Data

Place your data files inside the `/data` folder:

- `CallLog.csv`
- `SMS_Messages.csv`
- `AppUsage.csv`

Ensure each CSV includes a timestamp column such as `Date`, `timestamp_start`, etc.

---

## 🚀 Running the Analysis

Run the main script:

```bash
python main.py
```

This will:
- Load the data
- Merge all events into a single timeline
- Visualise the correlation between calls, texts, and app usage with a scatter plot

---

## 📊 Example Output

A forensic timeline showing when each communication or app event occurred:

```
| Time             | Event Type | Details              |
|------------------|------------|-----------------------|
| 2025-06-30 14:10 | Call       | Outgoing: +234801...  |
| 2025-06-30 14:11 | App        | WhatsApp opened       |
| 2025-06-30 22:15 | SMS        | Sent to +234902...    |
```

---

## ⚙️ Dependencies

- `pandas`
- `matplotlib`
- `seaborn`

You can install them via:

```bash
pip install pandas matplotlib seaborn
```

---

## 🧠 Future Enhancements

- Integration with SQLite or MongoDB for persistent storage
- Jupyter Notebook interface
- Support for browser history, contacts, and media artefacts
- Automated artefact parsing from Android forensic images

---

## 🛡️ Legal Disclaimer

This project is for **educational and lawful forensic investigation purposes only**. Any use outside ethical and legal boundaries is strictly discouraged.

---

## 👨🏽‍💻 Author

**Bukola Tolawoyin**  
Cybersecurity & Forensics Researcher | Software Engineer | Agricultural Investor  
🔗 [LinkedIn](https://www.linkedin.com/in/your-profile) (update your link)

---

## 📄 License

MIT License – see `LICENSE` file for details.
