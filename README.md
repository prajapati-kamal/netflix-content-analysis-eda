# 🎬 Netflix Content Analysis & EDA

Exploratory Data Analysis (EDA) on the Netflix Movies & TV Shows dataset using Python (pandas + matplotlib). Visualizes content type distribution, content ratings, and movie duration.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

## 📌 Project Overview

This project explores the Netflix content dataset to visualize:

- The distribution of **Movies vs. TV Shows**
- The breakdown of **content ratings** (TV-MA, PG-13, etc.)
- The **duration distribution** of movies

---

## 📂 Dataset

- **Source:** [Netflix Movies and TV Shows Dataset (Kaggle)](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- **File:** `netflix_titles.csv`
- **Key Columns Used:** `type`, `rating`, `duration`

> ⚠️ Dataset not included in this repo. Download from Kaggle and place it at the path referenced in `main.py`.

---

## 🛠️ Tech Stack

- **Language:** Python 3.10+
- **Libraries:** `pandas`, `matplotlib`

---

## 📁 Project Structure

```
netflix-content-analysis-eda/
│
├── data/
│   └── netflix_titles.csv          # Raw dataset (not included, download from Kaggle)
│
├── images/
│   ├── Movies_vs_TV_Shows.png
│   ├── Content_Ratings_Pie.png
│   └── Movies_Duration_Histogram.png
│
├── main.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🚀 Getting Started

```bash
git clone https://github.com/<your-username>/netflix-content-analysis-eda.git
cd netflix-content-analysis-eda
pip install -r requirements.txt
python main.py
```

Update the CSV path in `main.py` to point to your local copy of `netflix_titles.csv` before running.

---

## 📊 Current Visualizations

| Chart | Type | Status |
|---|---|---|
| Movies vs TV Shows | Bar Chart | ✅ Working (see note below on "Web Series") |
| Content Ratings | Pie Chart | ✅ Working (labels overlap for small slices — see Known Issues) |
| Movie Duration | Histogram | ✅ Working |

---

## ⚠️ Known Issues

This project is still a work in progress. Current known issues in `main.py` and its outputs:

1. **"Web Series" is not real data.** The script manually injects a `Web Series` category with a hardcoded value of `500`:
   ```python
   web_series_count = pd.Series({'Web Series': 500})
   ```
   The Netflix dataset only contains `Movie` and `TV Show` as `type` values — there is no `Web Series` field. This value is fabricated and should be removed so the "Movies vs TV Shows" chart reflects real counts only.

2. **Aggressive `dropna()` reduces the dataset unnecessarily.** All rows missing *any* of `type`, `title`, `director`, `cast`, `country`, `date_added`, `release_year`, `rating`, `duration`, or `listed_in` are dropped up front — even for charts that don't use most of those columns (e.g. the ratings pie chart doesn't need `director` or `cast`). This has caused inconsistent output between runs, including an empty/broken duration histogram in one export.

3. **No country-wise chart yet.** One exported image is labeled "Top 15 Countries by Number of Shows," but it currently just re-plots the Movie/TV Show/Web Series type counts — the `country` column isn't being used. A real top-countries chart (splitting multi-country rows and counting each separately) still needs to be implemented.

4. **Pie chart label overlap.** Content ratings with very small percentages (e.g. `NC-17`, `TV-Y7-FV`) overlap and become unreadable. Consider grouping rare ratings into an "Other" category or using a legend instead of inline labels.

**Planned fixes:** remove the fabricated Web Series data, clean per-chart instead of globally, implement a real Top 10 Countries chart, and improve pie chart label readability.

---

## 🤝 Contributing

1. Fork the repository
2. Create a branch (`git checkout -b feature/your-feature`)
3. Commit your changes
4. Open a Pull Request

---

## 📄 License

Licensed under the **MIT License** — see [LICENSE](LICENSE).

---

## 🙌 Acknowledgements

Dataset provided by [Shivam Bansal on Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)
