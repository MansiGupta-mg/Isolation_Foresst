import pandas as pd
import os
import numpy as np

# Stratified sampling to keep fraud ratio consistent
def prepare_subset():
    input_path = os.path.join("data", "creditcard.csv")
    output_path = os.path.join("data", "fraud_subset.csv")
    
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found. Please run download_data.py first.")
        return

    print("Loading full dataset...")
    df = pd.read_csv(input_path)
    
    print(f"Full dataset shape: {df.shape}")
    
    # Stratified sample
    # target column is 'Class' (0 = legitimate, 1 = fraud)
    # We want 10,000 rows max
    N = 10000
    
    if len(df) > N:
        print(f"Sampling {N} rows (stratified)...")
        # specific random state for reproducibility
        df_subset = df.groupby('Class', group_keys=False).apply(lambda x: x.sample(min(len(x), int(N * len(x)/len(df))), random_state=42))
        
        # If we slightly missed the count due to effective rounding, just take head or random sample again to fix strict size if needed, 
        # but groupby apply usually gets close. 
        # Let's ensure exact N by simple sampling if needed, but prioritizing stratified.
        # simpler approach for sk-learn users: train_test_split but here we just want a subset.
        
        from sklearn.model_selection import train_test_split
        # stratify sample
        _, df_subset = train_test_split(df, test_size=N, stratify=df['Class'], random_state=42)
        
    else:
        df_subset = df.copy()

    print(f"Subset shape: {df_subset.shape}")
    print("Class distribution in subset:")
    print(df_subset['Class'].value_counts(normalize=True))
    
    df_subset.to_csv(output_path, index=False)
    print(f"Saved subset to {output_path}")

if __name__ == "__main__":
    prepare_subset()
