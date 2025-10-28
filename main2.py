import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.title("Excel/CSV Data Extractor & Pivot Generator")

# File uploader (accept Excel + CSV)
uploaded_files = st.file_uploader(
    "Upload one or more Excel or CSV files",
    type=["xlsx", "csv"],
    accept_multiple_files=True
)

# Folder to save processed files
save_folder = "processed_files"
os.makedirs(save_folder, exist_ok=True)

if uploaded_files:
    st.success(f"{len(uploaded_files)} file(s) uploaded successfully!")
    
    for file in uploaded_files:
        # Detect file type and read accordingly
        if file.name.endswith('.csv'):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)
        
        # Ensure Store is string
        df['Store'] = df['Store'].astype(str)
        
        # Create pivot table
        pivot = df.pivot_table(
            index=['Product', 'Description', 'UPC', 'Size'],
            columns='Store',
            values='Qty',
            aggfunc='sum',
            fill_value=0
        ).reset_index()
        
        # Add Grand Total column
        store_columns = [col for col in pivot.columns if col not in ['Product', 'Description', 'UPC', 'Size']]
        pivot['Grand Total'] = pivot[store_columns].sum(axis=1)
        
        # Add Grand Sum row
        grand_sum = pivot[store_columns + ['Grand Total']].sum(numeric_only=True)
        grand_sum_row = pd.DataFrame([['Grand Sum', '', '', ''] + grand_sum.tolist()], columns=pivot.columns)
        pivot = pd.concat([pivot, grand_sum_row], ignore_index=True)
        
        # Save file with date-time stamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_filename = f"{file.name.split('.')[0]}extracted{timestamp}.xlsx"
        output_path = os.path.join(save_folder, output_filename)
        pivot.to_excel(output_path, index=False)
        
        # Show download button for each processed file
        st.subheader(f"Processed: {file.name}")
        with open(output_path, "rb") as f:
            st.download_button(
                label=f"Download {output_filename}",
                data=f,
                file_name=output_filename,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )