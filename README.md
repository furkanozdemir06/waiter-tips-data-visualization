# 🍽️ Waiter Tips Analysis

An exploratory data analysis and interactive visualization project that investigates the factors influencing restaurant tipping behavior.

The project combines a **Jupyter Notebook for detailed Exploratory Data Analysis (EDA)** with an **interactive Streamlit dashboard** that allows users to explore how bills, party size, meal time, customer profiles, and smoking status relate to gratuity behavior.

## 📌 Project Overview

The main goal of this project is to understand what drives restaurant tips by analyzing transactional and customer-related variables.

The analysis explores questions such as:

- Does a higher total bill lead to a higher tip?
- How does party size relate to tipping behavior?
- Are there differences in tips between lunch and dinner?
- Does tipping behavior vary by day of the week?
- Are there differences between smoker and non-smoker groups?
- How do customer characteristics relate to tip amount and tip percentage?

The project uses both statistical exploration and interactive visualizations to reveal patterns in restaurant tipping behavior.

## 📊 Dataset

The project uses:

```text
waitertips.csv
```

The dataset contains **244 observations and 7 original features**:

| Column | Description |
|---|---|
| `total_bill` | Total restaurant bill in dollars |
| `tip` | Tip amount in dollars |
| `sex` | Customer sex category |
| `smoker` | Whether the customer is a smoker |
| `day` | Day of the week |
| `time` | Meal time, such as Lunch or Dinner |
| `size` | Number of people in the party |

The Streamlit application also creates an additional feature:

```text
tip_percent = tip / total_bill × 100
```

The notebook reports **no missing values** in the dataset.

## 📈 Key Dataset Statistics

Some descriptive statistics from the notebook include:

| Metric | Average |
|---|---:|
| Total Bill | **$19.79** |
| Tip | **$3.00** |
| Party Size | **2.57 people** |

The numerical correlation analysis shows:

- `total_bill` vs. `tip`: approximately **0.68**
- `total_bill` vs. `size`: approximately **0.60**
- `tip` vs. `size`: approximately **0.49**

This suggests that tip amount is most strongly associated with the size of the total bill among the numeric variables analyzed.

## 🔎 Exploratory Data Analysis

The Jupyter Notebook (`WaiterTips.ipynb`) includes:

- Dataset inspection
- Shape and data type analysis
- Missing-value checks
- Descriptive statistics
- Numeric correlation analysis
- Correlation heatmap
- Tip frequency analysis
- Meal-time distribution
- Customer sex distribution
- Smoker vs. non-smoker analysis
- Day-of-week analysis
- Party-size analysis
- Tip distribution histogram
- Total-bill distribution
- Total bill vs. tip scatter plot
- Sex-based tip comparisons
- Meal-time tip comparisons
- Day-based tip comparisons
- Smoker-based spending comparisons
- Pie and donut charts
- Box plots
- Violin plots
- Pair plots
- Scatter-matrix visualization
- Sunburst visualization
- Interactive 3D visualization

## 💡 Main Insight

The exploratory analysis suggests that gratuity behavior is not random.

The **total bill is one of the strongest factors associated with tip amount**, while party size, meal timing, customer groups, and other categorical variables reveal additional behavioral patterns.

The notebook uses both traditional statistical visualizations and interactive multidimensional charts to explore these relationships from different perspectives.

## 🖥️ Streamlit Dashboard

The project also includes an interactive Streamlit application (`waitertips.py`) for exploring the dataset dynamically.

### Sidebar Filters

Users can filter the data by:

- Day
- Meal time
- Sex
- Smoker status

All dashboard metrics and charts automatically update based on the selected filters.

## 📌 Dashboard KPIs

The application displays four key metrics:

- Number of parties
- Average total bill
- Average tip
- Average tip percentage

## 📊 Dashboard Sections

The application is divided into four tabs:

### 1. Overview

The Overview section includes:

- Tip distribution histogram
- Total bill vs. tip scatter plot
- Linear trend line
- Numeric correlation matrix

### 2. Compare Groups

Users can dynamically compare groups based on:

- Day
- Meal time
- Sex
- Smoker status
- Party size

The dashboard displays:

- Average tip amount by group
- Tip-percentage distribution using box plots

### 3. Breakdown

A hierarchical Sunburst chart visualizes total tips through the following structure:

```text
Day
 └── Meal Time
      └── Sex
           └── Smoker Status
```

This makes it easier to explore how multiple categorical variables contribute to overall tipping patterns.

### 4. Data

The final tab displays the filtered dataset directly inside the application.

Users can also export the currently filtered data as:

```text
tips_filtered.csv
```

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Plotly
- Streamlit
- Jupyter Notebook

## 📁 Project Structure

```text
waiter-tips-analysis/
│
├── WaiterTips.ipynb
├── waitertips.py
├── waitertips.csv
└── README.md
```

## ⚙️ Installation

Clone or download the project and install the required Python libraries:

```bash
pip install pandas numpy matplotlib seaborn plotly streamlit jupyter
```

Make sure `waitertips.csv` is located in the same directory as `waitertips.py` and `WaiterTips.ipynb`.

## 🚀 Running the Project

### Run the Streamlit Dashboard

```bash
streamlit run waitertips.py
```

Streamlit will start a local server and open the interactive dashboard in your browser.

### Run the Jupyter Notebook

```bash
jupyter notebook WaiterTips.ipynb
```

Run the notebook cells to reproduce the complete exploratory analysis and visualizations.

## 🎯 Project Purpose

This project demonstrates practical skills in:

- Exploratory Data Analysis
- Data visualization
- Correlation analysis
- Customer behavior analysis
- Categorical data comparison
- Interactive visualization
- Dashboard development
- Feature engineering
- Streamlit application development
- Communicating analytical insights
---

Built with Python and Streamlit to explore the factors that influence restaurant tipping behavior. 🍽️💵📊
