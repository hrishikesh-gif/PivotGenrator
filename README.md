
# 📊 Excel / CSV Data Extractor & Pivot Generator

A lightweight **Streamlit-based web application** that automates the extraction, summarization, and pivot table generation from raw Excel and CSV files.
Built to eliminate repetitive manual reporting and deliver **client-ready Excel reports in under a minute**.

---

## 🚀 Overview

The **Excel / CSV Data Extractor & Pivot Generator** is designed for inventory and operations teams who regularly work with large datasets.
Instead of manually creating pivots, calculating totals, and formatting reports, this tool handles everything automatically through a simple web interface.

---

## ✨ Features

* Upload **multiple Excel (.xlsx) or CSV (.csv) files**
* Automatic **pivot table generation**
* Store-wise quantity aggregation
* Automatic **Grand Total column**
* Automatic **Grand Sum row**
* Timestamped Excel output files
* Download processed reports instantly
* Simple, non-technical user interface

---

## 🛠️ Tech Stack

* **Language:** Python
* **Framework:** Streamlit
* **Libraries:**

  * `pandas`
  * `openpyxl`
  * `streamlit`
* **Platform:** Local machine (Web-based UI)

---

## 📂 Project Structure

```text
├── main.py                # Streamlit application
├── processed_files/       # Auto-generated output files
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## ⚙️ Installation

Follow these steps to run the project locally:

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/excel-csv-pivot-generator.git
cd excel-csv-pivot-generator
```

### 2️⃣ Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Streamlit app using:

```bash
streamlit run main.py
```

Once started, the app will open automatically in your browser.

---

## 📘 Usage Guide

1. Launch the application.
2. Upload one or more **Excel or CSV files**.
3. The system will:

   * Read the data
   * Generate pivot tables
   * Calculate totals
   * Create a formatted Excel report
4. Click **Download** to get the processed file instantly.

> ⏱️ Typical processing time: **less than 1 minute per report**

---

## 📊 Input Data Requirements

The input file must contain the following columns:

* `Product`
* `Description`
* `UPC`
* `Size`
* `Store`
* `Qty`

> ⚠️ Column names must be consistent for accurate processing.

---

## 🧪 Testing & Validation

* Verified pivot results against manual Excel reports
* Tested with multiple file sizes and formats
* Validated grand totals and summary rows

---

## 📈 Performance Impact

| Process Type     | Time Taken    |
| ---------------- | ------------- |
| Manual Reporting | 1 – 1.5 hours |
| Automated Tool   | < 1 minute    |

---

## ⚠️ Limitations

* Assumes consistent column naming
* Extremely large files may slightly increase processing time
* Designed for internal reporting use

---

## 🤝 Contributing (Optional)

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a pull request

---

## 📄 License

This project is an **internal organizational tool**.
For external or commercial use, please define an appropriate license.

---

## 👤 Author & Acknowledgements

**Hrishikesh Tayade**

* Design
* Development
* Testing

Special thanks to the **Inventory Management Team** for requirements and validation.

---

## 📚 References

* Pandas Documentation
* Streamlit Documentation
* OpenPyXL Documentation

---

