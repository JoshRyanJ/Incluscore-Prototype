# scoring.py
import pandas as pd

# --- CSV SCORING ---
def calculate_csv_scores(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate an IncluScore for each row in the DataFrame.
    Expects the CSV to have columns: Accessibility, Affordability, Safety.
    Returns the DataFrame with a new 'IncluScore' column.
    """
    required_columns = ["Accessibility", "Affordability", "Safety"]

    # Check if all required columns are present
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    # Normalize scores (assuming scale 0–10) and average
    df["IncluScore"] = df[required_columns].mean(axis=1)
    return df


# --- SURVEY SCORING ---
def calculate_survey_score(accessibility: int, affordability: int, safety: int) -> float:
    """
    Calculate a single IncluScore from survey responses.
    Each input should be between 0 and 10.
    """
    return round((accessibility + affordability + safety) / 3, 2)
