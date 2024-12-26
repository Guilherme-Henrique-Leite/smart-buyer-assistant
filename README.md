# Smart Buyer Assistant  [in progress...🚧]

The **Smart Buyer Assistant** is a product recommendation system that uses collaborative filtering to suggest personalized products to users based on their preferences and purchase behavior.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Dataset](#dataset)
3. [How to Run](#how-to-run)
---

## Project Overview

This project builds a recommendation system for e-commerce applications. It analyzes user-product interaction data (e.g., ratings, purchases) to recommend products that are likely to be of interest to the user. The main techniques used are:

- **Collaborative Filtering**: Recommends products based on similar users or similar products.
- **Data Preprocessing**: Cleans and prepares the dataset for analysis.
- **Evaluation Metrics**: Measures performance using metrics like Mean Absolute Error (MAE) or Precision.

---

## Dataset

The dataset used is the **Amazon Product Reviews** dataset, which contains user ratings for various products. Download it from Kaggle:

- **Dataset Link**: [Amazon Product Reviews](https://www.kaggle.com/datasets/skillsmuggler/amazon-ratings)

---

## How to Run

### 1. Clone the Repository

To start working with the project, clone this repository to your local machine:

```
git clone https://github.com/Guilherme-Henrique-Leite/smart-buyer-assistant.git
```

### 2. Set up the Environment
It is recommended to use a virtual environment to manage dependencies. If you're using pip, you can set up a virtual environment by running the following commands:
  ```
  python3 -m venv venv
  - source venv/bin/activate  # Or On Windows, use venv\Scripts\activate
  ```

Install the required dependencies:
  ```
  - pip install -r requirements.txt
  ```
