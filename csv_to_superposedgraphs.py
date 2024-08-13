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

    csv_to_superposed(args.input_csv_path, args.output_filename) 

def csv_to_superposed(input_csv_path, output_filename):

    lst_lcornea_loaded = []
    lst_rcornea_loaded = []

    with open(input_csv_path, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            lst_rcornea_loaded.append(float(row[1]))
            lst_lcornea_loaded.append(float(row[2]))

    # creates subplots
    fig, axs = plt.subplots(2, 1, figsize=(18, 12), sharex=True)  # 2 rows, 1 column, shared x-axis

    # plot lcornea on first plot
    axs[0].plot(lst_lcornea_loaded, label='Left Cornea')
    axs[0].set_ylabel('Mask Area')  
    axs[0].legend()

    # plot rcornea on second plot
    axs[1].plot(lst_rcornea_loaded, label='Right Cornea', color='darkorange')
    axs[1].set_xlabel('Files Processed') 
    axs[1].set_ylabel('Mask Area') 
    axs[1].legend()

    fig.suptitle('Cornea Mask Areas Over Files')

    plt.tight_layout()
    plt.savefig(output_filename, dpi=300)
    plt.show()
    plt.close(fig)

if __name__ == '__main__':
    main()