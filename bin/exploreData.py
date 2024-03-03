"""
Compute basic statistics about peaks in a bed file
"""

# Import modules
import argparse
import pandas as pd

# Parse args
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--filePath", help="Path to bed file")
args = parser.parse_args()

# Explore Data
data = pd.read_csv(args.filePath, sep='\t', header=None)
print(f"Basic information from:\t{args.filePath}")
print(f"Number of peaks:\t{data.shape[0]}")
print(f"Sum of peak lengths:\t{sum(lenghts := data[2] - data[1])}") # Columns 1 and 2 correspond to sequence start and end
for key,value in lenghts.describe().to_dict().items():
    print(f"{key} peak length:\t{value}")
