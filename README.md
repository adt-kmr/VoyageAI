# Voyage AI - Traveller Segmentation Business Analysis

This project segments travellers into distinct customer personas using unsupervised machine learning. The goal is to help travel platforms better understand their users and make informed business decisions based on actual behaviour patterns.

---

## What This Project Does

The notebook loads clustering results from three algorithms, maps each traveller to a persona, and generates visual comparisons across algorithms. All results and plots are saved to the results folder.

---

## Dataset

- Total records: ~1,00,000 travellers
- Source: Pre-processed clustering output CSVs

---

## Features Used

| Feature | Description |
|---|---|
| trip_frequency | Number of trips booked by the user |
| average_booking_value | Average amount spent per booking |
| destination_diversity | Variety of destinations explored |
| session_duration | Time spent on the platform per session |
| search_behavior | User search activity and patterns |

---

## Traveller Personas

| Cluster | Persona |
|---|---|
| 0 | Frequent Travellers |
| 1 | Occasional Travellers |
| 2 | Travel Newbies |
| 3 | High Spenders |
| 4 | Budget Travellers |
| -1 | Unclassified (DBSCAN noise points) |

---

## Algorithms Compared

| Algorithm | Silhouette Score | Clusters Found |
|---|---|---|
| KMeans | 0.4482 | 5 |
| Hierarchical | 0.4819 | 3 |
| DBSCAN | 0.0193 | 38 |

Hierarchical clustering performed best on this dataset based on silhouette score. DBSCAN produced too many micro-clusters and a low score, making it less suitable for business persona mapping.

---

## Project Structure

```
AIProject/
│
├── .venv/                     # Python virtual environment
├── data/                      # Dataset folder
│   ├── processed/             # Processed datasets for modeling
│   │   └── finalclusteringdataset.csv
│   └── raw/                   # Raw original datasets
│       └── dataset.csv
│
├── notebooks/                 # Jupyter notebooks for analysis and modeling
│   ├── 01_business_analysis.ipynb
│   ├── 02_data_generation.ipynb
│   ├── 03_preprocessing.ipynb
│   ├── 04_kmeans_clustering.ipynb
│   ├── 05_dbscan_clustering.ipynb
│   ├── 06_hierarchical_clustering.ipynb
│   └── 07_gmm_clustering.ipynb
│
├── results/                   # Output results
│   ├── csv/                   # CSV files for clustering results
│   │   ├── dbscan_results.csv
│   │   ├── hierarchical_results.csv
│   │   └── kmeans_results.csv
│   └── plots/                  # Graphs and visualizations
│       ├── algo_comparison.png
│       ├── cross_algo_heatmap.png
│       ├── dbscan_persona_graphs.png
│       ├── hierarchical_persona_graphs.png
│       └── kmeans_persona_graphs.png
│
├── .gitignore                 # Git ignore file
├── README.md                  # Project documentation
└── requirements.txt           # Python dependencies

---

## How to Run

Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn
```

Make sure the CSV files are present in `results/csv/` with the following columns:

```
trip_frequency, average_booking_value, destination_diversity,
session_duration, search_behavior, Cluster
```

Open and run the notebook:

```bash
jupyter notebook notebooks/D1_business_analysis.ipynb
```

---

## Output Graphs

| File | Description |
|---|---|
| algo_comparison.png | Silhouette scores and cluster counts across all three algorithms |
| kmeans_persona_graphs.png | Persona profile charts for KMeans segmentation |
| hierarchical_persona_graphs.png | Persona profile charts for Hierarchical segmentation |
| dbscan_persona_graphs.png | Persona profile charts for DBSCAN segmentation |
| cross_algo_heatmap.png | Normalized feature means heatmap comparing all three algorithms |

---

## Tech Stack

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn

---

## Key Findings

- Hierarchical clustering produced the most meaningful and interpretable segments for this dataset.
- High Spenders and Frequent Travellers are the highest value segments for targeted campaigns.
- Budget Travellers form a large volume segment, suitable for discount and deal-based marketing.
- DBSCAN is not recommended for persona-based analysis on this data due to its low silhouette score and excessive cluster fragmentation.