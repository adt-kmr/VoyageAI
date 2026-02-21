"""
AIPROJECT - Professional Structure Reorganizer
Run this script from inside your AIPROJECT folder:
    python reorganize_project.py
"""

import os
import shutil

# ─────────────────────────────────────────────
# 1.  FOLDER STRUCTURE CREATE KARO
# ─────────────────────────────────────────────
folders = [
    "data/raw",
    "data/processed",
    "notebooks",
    "results/csv",
    "results/plots",
    "src",
    "reports",
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"✅ Created folder: {folder}")

# ─────────────────────────────────────────────
# 2.  FILE MAPPING  (source → destination)
# ─────────────────────────────────────────────
file_moves = {
    # RAW DATA
    "dataset.csv": "data/raw/dataset.csv",

    # PROCESSED DATA
    "finalclusteringdataset.csv": "data/processed/finalclusteringdataset.csv",

    # RESULT CSVs
    "dbscan_results.csv":        "results/csv/dbscan_results.csv",
    "gmm_results.csv":           "results/csv/gmm_results.csv",
    "hierarchical_results.csv":  "results/csv/hierarchical_results.csv",
    "kmeans_results.csv":        "results/csv/kmeans_results.csv",

    # PLOTS / PNGs
    "algo_comparison.png":              "results/plots/algo_comparison.png",
    "algo_quality_summary.png":         "results/plots/algo_quality_summary.png",
    "bic_aic_plot.png":                 "results/plots/bic_aic_plot.png",
    "booking_vs_frequency.png":         "results/plots/booking_vs_frequency.png",
    "cross_algo_heatmap.png":           "results/plots/cross_algo_heatmap.png",
    "persona_graphs_dbscan.png":        "results/plots/persona_graphs_dbscan.png",
    "persona_graphs_gmm.png":           "results/plots/persona_graphs_gmm.png",
    "persona_graphs_hierarchical.png":  "results/plots/persona_graphs_hierarchical.png",
    "persona_graphs_kmeans.png":        "results/plots/persona_graphs_kmeans.png",
    "silhouette_davies_comparison.png": "results/plots/silhouette_davies_comparison.png",

    # NOTEBOOKS
    "business_analysis.ipynb":           "notebooks/01_business_analysis.ipynb",
    "datagenfinal.ipynb":                "notebooks/02_data_generation.ipynb",
    "preprocessing.ipynb":               "notebooks/03_preprocessing.ipynb",
    "kmeans_clustering.ipynb":           "notebooks/04_kmeans_clustering.ipynb",
    "dbscan_clustering.ipynb":           "notebooks/05_dbscan_clustering.ipynb",
    "hierarchical_clustering.ipynb":     "notebooks/06_hierarchical_clustering.ipynb",
    "gaussian_mixture_clustering.ipynb": "notebooks/07_gmm_clustering.ipynb",
}

# ─────────────────────────────────────────────
# 3.  FILES MOVE KARO
# ─────────────────────────────────────────────
print("\n📦 Moving files...\n")
for src, dst in file_moves.items():
    if os.path.exists(src):
        shutil.move(src, dst)
        print(f"  ✅ Moved:    {src}  →  {dst}")
    else:
        print(f"  ⚠️  Missing:  {src}  (skipped)")

# ─────────────────────────────────────────────
# 4.  requirements.txt AUTO-GENERATE KARO
# ─────────────────────────────────────────────
requirements = """# Core
numpy>=1.24
pandas>=2.0
scikit-learn>=1.3
scipy>=1.11

# Clustering extras
hdbscan

# Visualisation
matplotlib>=3.7
seaborn>=0.12
plotly>=5.15

# Notebooks
jupyter
ipykernel

# Utilities
tqdm
joblib
"""
with open("requirements.txt", "w") as f:
    f.write(requirements)
print("\n✅ requirements.txt created")

# ─────────────────────────────────────────────
# 5.  .gitignore UPDATE KARO
# ─────────────────────────────────────────────
gitignore_content = """# Python
__pycache__/
*.py[cod]
*.egg-info/
dist/
build/

# Virtual env
.venv/
env/
venv/

# Jupyter
.ipynb_checkpoints/
*.ipynb_checkpoints

# Data (large files - optional)
# data/raw/*.csv

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
.idea/
"""
with open(".gitignore", "w") as f:
    f.write(gitignore_content)
print("✅ .gitignore updated")

# ─────────────────────────────────────────────
# 6.  README.md BANAO
# ─────────────────────────────────────────────
readme = """# 🏨 Hotel Booking Customer Segmentation

> Clustering-based customer segmentation using multiple unsupervised learning algorithms  
> to uncover hidden booking patterns and enable data-driven business decisions.

---

## 📌 Problem Statement
Hotels struggle to personalise offers for diverse customers.  
This project segments hotel customers based on booking behaviour using **K-Means, DBSCAN,
Hierarchical Clustering, and Gaussian Mixture Models (GMM)**, then compares their performance.

---

## 📁 Project Structure
```
AIPROJECT/
├── data/
│   ├── raw/                  # Original dataset
│   └── processed/            # Cleaned & feature-engineered data
├── notebooks/
│   ├── 01_business_analysis.ipynb
│   ├── 02_data_generation.ipynb
│   ├── 03_preprocessing.ipynb
│   ├── 04_kmeans_clustering.ipynb
│   ├── 05_dbscan_clustering.ipynb
│   ├── 06_hierarchical_clustering.ipynb
│   └── 07_gmm_clustering.ipynb
├── results/
│   ├── csv/                  # Cluster label outputs
│   └── plots/                # All visualisations
├── src/                      # Reusable Python modules
├── reports/                  # Final summary & insights
├── requirements.txt
└── README.md
```

---

## 🧪 Algorithms Used
| Algorithm | Best For |
|-----------|----------|
| K-Means | Compact, spherical clusters |
| DBSCAN | Noise/outlier detection |
| Hierarchical | Dendrogram-based grouping |
| GMM | Soft probabilistic assignments |

---

## 📊 Key Results
- Best algorithm: *(update after evaluation)*
- Number of optimal clusters: *(update)*
- Key personas identified: *(e.g., Budget Traveller, Luxury Guest, Frequent Booker)*

---

## 🚀 How to Run

```bash
# 1. Clone the repo
git clone https://github.com/your-username/AIPROJECT.git
cd AIPROJECT

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate      # Mac/Linux
.venv\\Scripts\\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Open notebooks in order
jupyter notebook
```

---

## 🛠 Tech Stack
`Python` · `Scikit-learn` · `Pandas` · `NumPy` · `Matplotlib` · `Seaborn` · `Jupyter`

---

## 👤 Author
**Your Name** · [LinkedIn](https://linkedin.com) · [GitHub](https://github.com)
"""
with open("README.md", "w") as f:
    f.write(readme)
print("✅ README.md created")

# ─────────────────────────────────────────────
# 7.  src/ HELPER MODULE BANAO
# ─────────────────────────────────────────────
clustering_utils = '''"""
src/clustering_utils.py
Reusable helper functions for all clustering notebooks.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import silhouette_score, davies_bouldin_score, calinski_harabasz_score


def load_and_scale(filepath: str):
    """Load CSV and return scaled features + original df."""
    df = pd.read_csv(filepath)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df.select_dtypes(include=[np.number]))
    return df, X_scaled, scaler


def evaluate_clustering(X, labels, algo_name: str) -> dict:
    """Print and return clustering quality metrics."""
    mask = labels != -1          # exclude DBSCAN noise
    metrics = {}
    if mask.sum() > 1:
        metrics["silhouette"]       = silhouette_score(X[mask], labels[mask])
        metrics["davies_bouldin"]   = davies_bouldin_score(X[mask], labels[mask])
        metrics["calinski_harabasz"]= calinski_harabasz_score(X[mask], labels[mask])

    print(f"\\n📊 {algo_name} Metrics")
    print(f"  Silhouette Score       : {metrics.get('silhouette', 'N/A'):.4f}")
    print(f"  Davies-Bouldin Score   : {metrics.get('davies_bouldin', 'N/A'):.4f}")
    print(f"  Calinski-Harabasz Score: {metrics.get('calinski_harabasz', 'N/A'):.4f}")
    return metrics


def plot_clusters_2d(X_2d, labels, title: str, save_path: str = None):
    """Quick 2-D scatter plot of cluster assignments."""
    plt.figure(figsize=(8, 5))
    palette = sns.color_palette("tab10", len(set(labels)))
    for idx, label in enumerate(sorted(set(labels))):
        mask = labels == label
        lname = f"Noise" if label == -1 else f"Cluster {label}"
        plt.scatter(X_2d[mask, 0], X_2d[mask, 1],
                    color=palette[idx], label=lname, alpha=0.6, s=30)
    plt.title(title, fontsize=14, fontweight="bold")
    plt.legend()
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150)
        print(f"  💾 Plot saved → {save_path}")
    plt.show()
'''

with open("src/clustering_utils.py", "w") as f:
    f.write(clustering_utils)
print("✅ src/clustering_utils.py created")

print("\n" + "="*50)
print("🎉 PROJECT RESTRUCTURED SUCCESSFULLY!")
print("="*50)
print("\nNext steps:")
print("  1. cd into AIPROJECT folder")
print("  2. python reorganize_project.py")
print("  3. git add . && git commit -m 'refactor: professional project structure'")
print("  4. git push")