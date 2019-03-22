import argparse
import pandas as pd


def search_by_pm(pm):
    df = pd.read_csv('database.csv')
    result = df[df['PM'] == pm]
    result = result.fillna("")
    result.to_html('output.html')

def search_by_product(product):
    df = pd.read_csv('database.csv')
    result = df[df['Name'] == product]
    result = result.fillna("")
    result.to_html('output.html')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-pm", help="Search By PM", type=str)
    parser.add_argument("-pds", help="Search By Product", type=str)
    args = parser.parse_args()

    if args.pm:
        search_by_pm(args.pm)
    if args.pds:
        search_by_product(args.pds)
