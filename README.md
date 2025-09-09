# 🦠 Sentiment Analysis on COVID-19 Tweets (`sentiment_analysis_covid`)

End-to-end NLP pipeline to classify tweet sentiment (Negative / Neutral / Positive) on the **COVID-19 NLP Text Classification** dataset.  
Includes modular Python scripts for **preprocessing**, **feature engineering**, **model training**, and **evaluation**, plus a Jupyter notebook for exploration.

---

## Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Repository Structure](#repository-structure)
- [Setup](#setup)
- [Quickstart](#quickstart)
- [Usage (Scripts)](#usage-scripts)
- [Usage (Notebook)](#usage-notebook)
- [Configuration](#configuration)
- [Results](#results)
- [Reproducibility](#reproducibility)
- [Roadmap](#roadmap)
- [License](#license)

---

## Overview
This repository implements a classic text-classification workflow:

1. **Preprocessing** – cleaning tweets: lowercasing, URL/mention/hashtag removal, punctuation & stopword handling, tokenization.
2. **Feature Engineering** – TF-IDF (unigram–trigram) and optional dense embeddings.
3. **Models** – **Naive Bayes**, **Linear SVM**, **Random Forest**, and a simple **Neural Network** (optional).
4. **Evaluation** – accuracy, precision, recall, F1, and confusion matrix + per-class report.

---

## Dataset
- **Source**: *COVID-19 NLP Text Classification* (Kaggle, `datatattle/covid-19-nlp-text-classification`)  
- **Target**: `Sentiment` ∈ {Negative, Neutral, Positive}  
- **Text Field**: `OriginalTweet` (or `tweet`)  
> Download via Kaggle CLI or the Kaggle website, then place CSVs in `data/`.

---
