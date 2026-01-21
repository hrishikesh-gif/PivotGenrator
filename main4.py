import streamlit as st
import pandas as pd
from datetime import datetime
import os

st.title("Excel/CSV Pivot Generator V2")

uploaded_files = st.file_uploader(
    "Upload one or more Excel or CSV files",
    type=["xlsx", "csv"],
    accept_multiple_files=True
)

save_folder = "processed_files"
os.makedirs(save_folder, exist_ok=True)

if uploaded_files:
    st.success(f"{len(uploaded_files)} file(s) uploaded successfully!")

    for file in uploaded_files:
        # Read file
        if file.name.endswith(".csv"):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)

        # Validate required columns
        required_cols = {"Product", "Description", "UPC", "Size", "Store", "Qty"}
        if not required_cols.issubset(df.columns):
            st.error(f"{file.name}: Missing required columns. Skipping file.")
            continue

        df["Store"] = df["Store"].astype(str)

        # Create pivot
        pivot = df.pivot_table(
            index=["Product", "Description", "UPC", "Size"],
            columns="Store",
            values="Qty",
            aggfunc="sum",
            fill_value=0
        ).reset_index()

        # 🔍 UI MOVEMENT LOGIC (NO EXCEL CHANGES)
        x_columns = [col for col in pivot.columns if col.endswith("X")]

        file_has_movement = False

        if len(x_columns) > 1:
            st.warning(
                f"⚠️ {file.name}: Multiple X columns found ({', '.join(x_columns)}). "
                f"Please check this file manually."
            )
            file_has_movement = True

        elif len(x_columns) == 1:
            x_col = x_columns[0]
            if (pivot[x_col] != 0).any():
                file_has_movement = True

        # Save Excel (unchanged)
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_filename = f"{file.name.split('.')[0]}_extracted_{timestamp}.xlsx"
        output_path = os.path.join(save_folder, output_filename)
        pivot.to_excel(output_path, index=False)

        # UI RESULT
        if file_has_movement:
            st.error(f"🚨 Movement detected in file: {file.name}")
        else:
            st.success(f"✅ No movement detected in file: {file.name}")

        # Download button
        with open(output_path, "rb") as f:
            st.download_button(
                label=f"Download {output_filename}",
                data=f,
                file_name=output_filename,
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                key=output_filename
            )
