# Fraud Detection Learning Demo

A beginner-friendly project demonstrating Fraud Detection pipelines using Python, Jupyter, and a simulated streaming architecture.

## Overview
This project helps students learn:
1. **Exploratory Data Analysis (EDA)** on financial data (PCA, t-SNE).
2. **Anomaly Detection** using Statistical methods (Z-Score) and Machine Learning (Isolation Forest).
3. **Streaming Pipelines**: Simulating real-time transaction monitoring and alerting.

## Setup
1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Download Data**:
   ```bash
   python get_data.py
   ```
3. **Prepare Subset** (Creates a balanced/stratified 10k row dataset):
   ```bash
   python prepare_subset.py
   ```

## Part 1: Notebook Demo
- **File**: `Exploration_and_Models.ipynb`
- **Goal**: Understand the data and models visually.
- **Run**:
  Generate the notebook (if not already):
  ```bash
  python create_notebook.py
  ```
  Then open in Jupyter:
  ```bash
  jupyter notebook Exploration_and_Models.ipynb
  ```

## Part 2: Streaming Simulation
Simulate a production environment where transactions arrive in real-time.

1. **Producer** (Simulates incoming data):
   *Already integrated into the detector workflow, but can be run standalone to test data flow.*
   ```bash
   python stream_simulation/producer.py
   ```

2. **Detector** (Runs the pipeline):
   *Consumes the stream, calculates sliding window statistics (Z-Scores), and flags anomalies.*
   ```bash
   python stream_simulation/detector.py
   ```
   *Output*: You will see transactions scrolling by with alerts for anomalies.

## Configuration
- `config/pipeline_config.yaml`: Adjust stream speed, window size.
- `config/alert_rules.yaml`: Adjust Z-score thresholds.

## Dataset
Sourced from [Kaggle Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud).
