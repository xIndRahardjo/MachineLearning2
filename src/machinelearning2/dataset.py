"""Dataset loading utilities."""

from pathlib import Path

import pandas as pd


def load_csv(path: str | Path, **kwargs: object) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame."""
    return pd.read_csv(path, **kwargs)
