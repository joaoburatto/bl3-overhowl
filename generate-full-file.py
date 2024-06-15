
import os
 
def concatenate_files(input_folder, output_file):
    with open(output_file, 'w') as outfile:
        for filename in os.listdir(input_folder):
            file_path = os.path.join(input_folder, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as infile:
                    content = infile.read()
                    outfile.write(content)
                outfile.write("\n")  
 
input_folder = 'add your input folder'
output_file = 'add your output folder and output file with format extention'

concatenate_files(input_folder, output_file)
