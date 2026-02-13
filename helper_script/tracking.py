# Imports
import pandas as pd
import sys


def stats(track_loc):
    df = pd.read_csv(track_loc)
    print(len(df['sessionId'].unique()))
    return


if __name__=="__main__":
    if len(sys.argv) < 1:
        print("Usage: add_reference.py <file_location>")
        sys.exit(1)

    tracking_loc = sys.argv[1]
    stats(tracking_loc)