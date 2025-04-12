# 📊 User Demographics Analysis

A data analytics project focused on understanding user behavior across different cities using engagement metrics like session count, engagement time, and new vs returning user patterns. The project also explores clustering techniques and funnel visualization to derive actionable business insights.

---

## 🔍 Project Overview

This project analyzes a dataset of user demographics and activity metrics to:
- Understand user engagement across cities
- Identify high-value user segments
- Visualize city-level differences in engagement
- Provide insights for targeted marketing and budget allocation
- Perform clustering to group cities based on user behavior

---

## 📁 Dataset

The dataset used is `user-demographics.csv` and contains the following key columns:
- `Town/City`
- `Users`
- `New users`
- `Engaged sessions`
- `Engagement rate`
- `Engaged sessions per user`
- `Average engagement time`
- `Event count`

---

## 📊 Key Insights

- **Top Cities**: Hyderabad, Bengaluru, and Chennai have the highest number of users.
- **Engagement Rate**: Highest in Chennai and Hyderabad.
- **Engaged Sessions per User**: Bengaluru leads, indicating high user interaction.
- **Average Engagement Time**: Cities like Istanbul and Jaipur show deep user interest.
- **Event Count**: Hyderabad and Bengaluru dominate in overall user activity.
- **New vs Returning Users**: Most cities are skewed towards new users, suggesting growth but highlighting a retention challenge.

---

## 📈 Visualizations

The following charts and visualizations are generated:
- Top 20 Cities by Number of Users
- Engagement Rate & Sessions per User per City
- Average Engagement Time per City
- New vs Returning Users
- Event Count Distribution
- Correlation Heatmap of Engagement Metrics
- Clustering (KMeans with PCA)
- User Funnel (via Sankey Diagram)

---

## 🧠 Advanced Analysis

### 1. 📦 Segmentation for Budget Allocation
Users and cities are segmented into:
- **High Engagement Users**
- **New Users**
- **Returning Users**
- **Low / Medium / High User Cities**

Each segment is analyzed with suggested **marketing strategies and budget allocation**.

### 2. 📉 Clustering
Cities are clustered into 3 behavioral groups using:
- StandardScaler normalization
- KMeans clustering
- PCA for 2D visualization

### 3. 🔄 Funnel Analysis
Sankey diagram displays user transition:
- From Total Users → New/Returning → Engaged Users

---

## 🧰 Tech Stack

- **Python**
- **Pandas**, **NumPy** – data wrangling
- **Matplotlib**, **Seaborn**, **Plotly** – data visualization
- **Scikit-learn** – clustering and PCA
- **Jupyter Notebook / Google Colab**

---

## 🚀 Getting Started

### Prerequisites
Install the required libraries:
```bash
pip install pandas seaborn matplotlib scikit-learn plotly
```

### Running the Project
1. Place the `user-demographics.csv` file in the same directory.
2. Run the Python script or load the `.ipynb` version in Jupyter/Colab.
3. Explore charts and outputs interactively.

---

## 🧩 Folder Structure

```
├── user_demographics_analysis.py
├── user-demographics.csv
├── README.md
```

---

## 📌 Future Improvements

- Automate loading of new datasets from APIs
- Add web-based dashboard (Streamlit or Dash)
- Perform time-series analysis if historical data becomes available
- Implement advanced clustering (DBSCAN, hierarchical)

---

## 📬 Connect

For suggestions, improvements, or collaborations:

**Priyanshu Sethi**  
[Your GitHub Profile](https://github.com/PRIYANSHUSETHI)  
[Your LinkedIn](https://www.linkedin.com/in/priyanshu-sethi-bitsh/)
