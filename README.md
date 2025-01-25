# Smart Buyer Assistant

The **Smart Buyer Assistant** is a product recommendation system using collaborative filtering to provide personalized suggestions based on user preferences and purchasing behavior.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Dataset](#dataset)
4. [Installation and Setup](#installation-and-setup)
5. [Usage](#usage)
---

## Project Overview

This project offers a recommendation system for e-commerce platforms, analyzing user-product interactions to suggest products of interest.

---

## Features

- Personalized recommendations
- Data visualization
- Efficient data processing

---

## Dataset

Utilizes the **Amazon Product Reviews** dataset. [Access it on Kaggle](https://www.kaggle.com/datasets/skillsmuggler/amazon-ratings).

---

## Installation and Setup

1. **Clone the Repository**:
   ```
   git clone https://github.com/Guilherme-Henrique-Leite/smart-buyer-assistant.git
   ```

2. **Set up the Environment**:
   ```
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   pip install -r requirements.txt
   ```

---

## Usage

Run the main application:
```
streamlit run src/app/main.py
```

---

### Goals

Enhance shopping experiences with personalized recommendations using collaborative filtering.

### Technical Stack

- **Language**: Python
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Scikit-surprise

### Future Enhancements

- Improved user interface
