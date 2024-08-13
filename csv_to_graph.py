import csv
import matplotlib.pyplot as plt
import argparse

def main():
    """
    take command line arguments input for the path of the csv file and name of the outputted graph(s)

    arguments:
        none
    """
    parser = argparse.ArgumentParser(description='processing csv files into a graph') # necessary for implementing command-line
    parser.add_argument('--input_csv_path', '-icp', type=str, help='path to csv') # adds argument input_csv_path to the parser
    parser.add_argument('--output_filename', '-of', type=str, help='name of graph file') # adds argument output_filename to the parser

    args = parser.parse_args() # allows us to use the arguments in the parser (args.argument_name)

    csv_to_graph(args.input_csv_path, args.output_filename) 

def csv_to_graph(input_csv_path, output_filename):

    lst_lcornea_loaded = []
    lst_rcornea_loaded = []

    with open(input_csv_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            lst_rcornea_loaded.append(float(row[1]))
            lst_lcornea_loaded.append(float(row[2]))

    fig, ax = plt.subplots(figsize=(18, 12))

    ax.plot(lst_lcornea_loaded, label='Left Cornea')

    ax.plot(lst_rcornea_loaded, label='Right Cornea', color='darkorange')

    ax.set_xlabel('Files Processed') 
    ax.set_ylabel('Mask Area') 
    ax.legend()

    fig.suptitle('Cornea Mask Areas Over Files')

    plt.tight_layout()
    plt.savefig(output_filename, dpi=300)
    plt.show()
    plt.close(fig)

if __name__ == '__main__':
    main()