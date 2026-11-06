"""Energy Analyst programming exercise."""

# ---------------------------------------------------------------------------
# Parameters (edit these to run on another system)
# ---------------------------------------------------------------------------
from pathlib import Path

DATA_DIR = Path(__file__).parent / "data" / "historicalPriceData"
OUTPUT_DIR = Path(__file__).parent / "output"

# Required packages: see requirements.txt (pandas, numpy, matplotlib)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


if __name__ == "__main__":
    main()
