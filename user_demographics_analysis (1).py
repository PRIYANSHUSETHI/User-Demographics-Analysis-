# -*- coding: utf-8 -*-
"""USER DEMOGRAPHICS ANALYSIS.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LotwP5fLwFp7ROqhE8bsXq2acHiMImKQ
"""

import pandas as pd

data = pd.read_csv("user-demographics.csv")

print(data.head())

print(data.describe())

"""### **Key Observations from Summary Statistics**

- **Users**
  - Count ranges from **12 to 75,090**  
  - **Mean:** 258.60 users  
  - Indicates a **wide disparity** in user distribution; a few cities have a large user base while most have significantly fewer users

- **New Users**
  - Range: **5 to 72,162**  
  - **Mean:** 239.22  
  - Follows a similar pattern as total users, suggesting **growth is concentrated in a few cities**

- **Engaged Sessions**
  - Range: **0 to 84,798**  
  - **Mean:** 244.54  
  - Some cities show **zero engaged sessions**, possibly indicating new onboarding or low activity

- **Engagement Rate**
  - Range: **0 to 1**  
  - **Mean:** 0.52  
  - Shows a **moderate average engagement**, but the wide range points to **inconsistent user experience across cities**

- **Engaged Sessions per User**
  - Range: **0 to 13.29**  
  - **Mean:** 0.85  
  - Reflects **low frequency of engagement** per user in most cities

- **Average Engagement Time**
  - Range: **0 to 6,895.55 seconds (~1.9 hours)**  
  - **Mean:** 101.30 seconds (~1.7 minutes)  
  - Indicates that **a few users are highly engaged**, but most spend relatively little time

- **Event Count**
  - Range: **36 to 776,356**  
  - **Mean:** 2,276.55  
  - Suggests a **heavy-tailed distribution**, with a small number of cities contributing to the majority of events
"""

import seaborn as sns
import matplotlib.pyplot as plt

top_cities = data.sort_values(by='Users', ascending=False).head(20)

plt.figure(figsize=(12, 8))
sns.barplot(y=top_cities['Town/City'], x=top_cities['Users'], palette='viridis')
plt.xlabel('Number of Users')
plt.ylabel('Town/City')
plt.title('Top 20 Cities by Number of Users')
plt.show()

"""Hyderabad, Bengaluru, and Chennai are the top three cities with the highest number of users, significantly outpacing other cities. There is a steep drop-off in user count after these top cities, indicating a **concentration of users in major urban centers**, with **much fewer users** in other regions."""

plt.figure(figsize=(12, 8))
sns.barplot(y=top_cities['Town/City'], x=top_cities['Engagement rate'], palette='spring')
plt.xlabel('Engagement Rate')
plt.ylabel('Town/City')
plt.title('Engagement Rate in Top 20 Cities by Number of Users')
plt.show()

"""Key findings indicate that Chennai, Hyderabad, and Bengaluru exhibit the highest engagement rates, suggesting that users in these cities are more actively interacting with the website’s content."""

plt.figure(figsize=(12, 8))
sns.barplot(y=top_cities['Town/City'], x=top_cities['Engaged sessions per user'], palette='flare')
plt.xlabel('Engaged Sessions per User')
plt.ylabel('Town/City')
plt.title('Engaged Sessions per User in Top 20 Cities by Number of Users')
plt.show()

"""Key findings indicate that Bengaluru and Hyderabad have the highest engaged sessions per user, suggesting that users in these cities interact frequently with the website."""

plt.figure(figsize=(12, 8))
sns.barplot(y=top_cities['Town/City'], x=top_cities['Average engagement time'], palette='crest')
plt.xlabel('Average Engagement Time (seconds)')
plt.ylabel('Town/City')
plt.title('Average Engagement Time in Top 20 Cities by Number of Users')
plt.show()

"""Key findings include Istanbul, Jaipur, and Bhubaneswar showing the highest average engagement times, indicating that users in these cities spend more time engaged on the website."""

top_cities['Returning users'] = top_cities['Users'] - top_cities['New users']

top_cities_melted = top_cities.melt(id_vars='Town/City', value_vars=['New users', 'Returning users'],
                                    var_name='User Type', value_name='Count')

plt.figure(figsize=(14, 10))
sns.barplot(y='Town/City', x='Count', hue='User Type', data=top_cities_melted, palette='viridis')
plt.xlabel('Number of Users')
plt.ylabel('Town/City')
plt.title('New Users vs Returning Users in Top 20 Cities by Number of Users')
plt.legend()
plt.show()

"""The data shows that the majority of users in most cities are **new users**, with **Hyderabad, Bengaluru, and Chennai** having the highest counts. This indicates that these cities are experiencing significant growth in attracting **first-time visitors**. On the other hand, the proportion of **returning users** is much smaller across all cities, suggesting an opportunity to focus on **improving user retention strategies**."""

plt.figure(figsize=(12, 8))
sns.barplot(y=top_cities['Town/City'], x=top_cities['Event count'], palette='magma')
plt.xlabel('Event Count')
plt.ylabel('Town/City')
plt.title('Event Count in Top 20 Cities by Number of Users')
plt.show()

"""Hyderabad and Bengaluru lead significantly with the **highest event counts**, indicating a **high level of user interactions** in these cities. Chennai and Mumbai also show **substantial event counts**, reflecting **active user engagement**. In contrast, cities towards the lower end of the chart, such as **Bhubaneswar, Jaipur, and Istanbul**, have relatively **lower event counts**, suggesting **less user interaction** in these regions.

**User Segmentation by Cities for Budget Allocation**
"""

# high-Engagement Users
high_engagement_users = data[(data['Engaged sessions per user'] > data['Engaged sessions per user'].mean()) &
                             (data['Average engagement time'] > data['Average engagement time'].mean())]

# new Users
new_users = data[data['New users'] > (0.5 * data['Users'])]

# returning Users
returning_users = data[data['Users'] - data['New users'] > (0.5 * data['Users'])]

# categorize cities into high, medium, and low user count segments based on quantiles
user_quantiles = data['Users'].quantile([0.33, 0.67])
low_user_cities = data[data['Users'] <= user_quantiles[0.33]]
medium_user_cities = data[(data['Users'] > user_quantiles[0.33]) & (data['Users'] <= user_quantiles[0.67])]
high_user_cities = data[data['Users'] > user_quantiles[0.67]]

# summary of segments
segments_summary = {
    "High Engagement Users": len(high_engagement_users),
    "New Users": len(new_users),
    "Returning Users": len(returning_users),
    "Low User Cities": len(low_user_cities),
    "Medium User Cities": len(medium_user_cities),
    "High User Cities": len(high_user_cities)
}

segments_summary

"""To allocate the budget effectively across user segments, here’s a strategic approach based on their characteristics:

- **High Engagement Users**:  
  These users are already highly engaged and have a high likelihood of converting.  
  - **Budget Allocation**: Allocate a **substantial portion** to maintain and enhance their engagement.  
  - **Tactics**: Personalized ads, loyalty programs, exclusive offers, and premium experiences to strengthen their loyalty and increase conversions.

- **New Users**:  
  These users represent growth opportunities and require onboarding to become regular, engaged users.  
  - **Budget Allocation**: Invest in **onboarding efforts** to convert them into loyal users.  
  - **Tactics**: Welcoming campaigns, introductory offers, educational content, and seamless onboarding experiences to foster positive first impressions and boost retention.

- **Returning Users**:  
  Although the number is small, returning users represent loyalty and consistency.  
  - **Budget Allocation**: Invest in **retention strategies** to reward their continued engagement.  
  - **Tactics**: Personalized recommendations, loyalty rewards, exclusive content, and incentives for continued use to strengthen retention.

- **Low User Cities**:  
  These cities have **untapped potential** for user acquisition.  
  - **Budget Allocation**: Allocate a **smaller portion** of the budget for brand awareness campaigns and introductory offers.  
  - **Tactics**: Awareness and acquisition-focused campaigns, local partnerships, and incentives to attract new users.

- **Medium User Cities**:  
  These cities have moderate user bases and show growth potential.  
  - **Budget Allocation**: Allocate more budget to **nurture growth** and increase engagement.  
  - **Tactics**: Targeted ads, localized promotions, and campaigns that build on the existing user base to convert these cities into high-user cities.

- **High User Cities**:  
  These cities already have a large, engaged user base.  
  - **Budget Allocation**: Similar to high-engagement users, allocate a **substantial portion** to sustain high engagement.  
  - **Tactics**: Exclusive offers, community-building activities, and high-impact campaigns to maintain strong user involvement and prevent churn.
"""

import plotly.graph_objects as go

# Aggregating funnel data
total_users = data['Users'].sum()
new_users = data['New users'].sum()
returning_users = total_users - new_users
engaged_users = data[data['Engaged sessions'] > 0]['Users'].sum()

# Sankey flow values
labels = ["Total Users", "New Users", "Returning Users", "Engaged Users"]
sources = [0, 0, 0]  # All come from "Total Users"
targets = [1, 2, 3]  # Flow to New, Returning, Engaged
values = [new_users, returning_users, engaged_users]

fig = go.Figure(data=[go.Sankey(
    node=dict(pad=15, thickness=20, line=dict(color="black", width=0.5), label=labels),
    link=dict(source=sources, target=targets, value=values)
)])

fig.update_layout(title_text="User Funnel Flow", font_size=14)
fig.show()

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import seaborn as sns

# Features for clustering
features = ['Users', 'New users', 'Engaged sessions', 'Engagement rate',
            'Engaged sessions per user', 'Average engagement time', 'Event count']
X = data[features].dropna()

# Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply KMeans
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X_scaled)

data['Cluster'] = clusters

# Reduce to 2D using PCA for visualization
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)
data['PCA1'] = X_pca[:, 0]
data['PCA2'] = X_pca[:, 1]

# Plot clusters
plt.figure(figsize=(10, 7))
sns.scatterplot(data=data, x='PCA1', y='PCA2', hue='Cluster', palette='Set2', s=100)
plt.title('City Clustering Based on User Behavior')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.legend(title='Cluster')
plt.grid(True)
plt.show()

# Compute correlation matrix
corr = data[features].corr()

# Plot heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', square=True)
plt.title('Feature Correlation Matrix')
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()

