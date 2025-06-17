# 📊 Netflix Data Exploration

This project performs exploratory data analysis (EDA) and visualization on a dataset of Netflix titles. 

## 🗂️ Project Structure

```

📁 
├── netflix_data.csv      # Netflix dataset
├── netflix_data.py         # Python script for the EDA and visualisations
├── netflix_data.R          # R-based visualisations using ggplot2
├── netflix_data.ipy          # An alternative Jupiter Notepad code for the python script
├── netflix_data.html          # The exported HTML file of the Jupyter notepad script
├── README.md               # Project documentation

````

---

## 📄 Dataset

**File:** `netflix_data.csv`  
**Source:** [Kaggle Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows)  
**Columns:**
- `show_id`: Unique ID
- `type`: Movie or TV Show
- `title`
- `director`
- `cast`
- `country`
- `date_added`
- `release_year`
- `rating`
- `duration`
- `listed_in`: Genre(s)
- `description`

---

## 🚀 Getting Started

### ✅ Requirements

**For Python:**
- pandas
- matplotlib
- seaborn

Install via pip:

```bash
pip install pandas matplotlib seaborn
````

**For R:**

* tidyverse
* plotly

Install in R:

```R
install.packages(c("tidyverse", "plotly"))
```

---


## 🚀 How to Run

### Step 1: Run the Python Script (`netflix_data.ipynb or netflix_data.py`)
* Launch Jupyter Lab by typing 'jupyter lab' in the command prompt (Windows) or terminal (Mac/Linux).
* Navigate to the directory where your netflix_data.ipynb file is located.
* Click on the file to open it in Jupyter Lab.
* Run the script inside the Jupyter lab
* Alternatively, using the terminal or command prompt, type
```bash
python netflix_data.py
```

This script:

* Loads, renames and preview the Netflix dataset.
* Cleans the dataset
* Performs some exploratory data analysis using descriptive statistics and charts
* Creates visualisations using matplotlib


Make sure the dataset exists in the same directory as the Python script:

```
netflix_data.csv
```

### Step 2: Run the R Script (`netflix_data.R`)

1. Open a terminal or command prompt.
2. Navigate to the folder containing `netflix_data.r`.
3. Run the script:
4. Alternatively, you can run it from an R environment like RStudio:


   ```r
   Rscript netflix_data.r
   ```

#### What it does:

This script:

* The script creates a bar chart showing the 10 most-watched genres





## 🤝 Contributing

Feel free to fork, clone, and extend this project! Suggestions and improvements are welcome.

---

## 📄 License

For improvements, feel free to open a pull request on my GitHub account or contact me directly - josephdokhare@gmail.com



