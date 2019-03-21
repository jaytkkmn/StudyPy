import csv
import argparse
import pandas as pd

def SearchByPM(pm):
    df = pd.read_csv('database.csv')
    result = df[df['PM'] == pm]
    print(result)
    file_title = 'output.txt'
    for row in result.values:
        row.tofile(file_title, sep=",", format="%s")
    '''
    pm = input("Enter the Name of PM(ex: Sam Chiu):")
    with open('database.csv', newline='') as csvfile:
        rows = csv.DictReader(csvfile)
        for row in rows:
            if row['PM'] == pm:
                print(row['Name'])
    '''
def SearchByProduct(product):
    df = pd.read_csv('database.csv')
    result = df[df['Name'] == product]
    print(result)
    for row in result.values:
        file_title = 'output.txt'
        row.tofile(file_title, sep=",", format="%s")


def UsePandas():
    df = pd.read_csv('database.csv')
    #print(df)
    #select_df = pd.DataFrame(df)
    #print(select_df.ix[:, 1].notnull())

    result = df[df['Name'] == 'M-900']
    for row in result.values:
        file_title = 'output.txt'
        row.tofile(file_title, sep=",", format="%s")

    """
    with open("Output.txt", "w") as text_file:
        result = df[df['Name'] == 'M-900']
        text_file.write(result)
        print(result)
    #print(df[df['PM'] =='Sam Chiu'])
    """

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-pm", help="Search By PM", type=str)
    parser.add_argument("-pd", help="Search By Product", type=str)
    args = parser.parse_args()

    if args.pm:
        SearchByPM(args.pm)
    if args.pd:
        SearchByProduct(args.pd)
