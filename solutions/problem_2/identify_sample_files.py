import os
import fnmatch
import argparse


parser = argparse.ArgumentParser(description='Identify sample files with fewer entries than a given value.')

parser.add_argument('--dir', type=str, required=True, help='Path to the directory containing the sample files')
parser.add_argument('--min_values', type=int, default=100, help='Minimum number of values that should be contained in a sample file')

args = parser.parse_args()

dir = args.dir
min_values = args.min_values

def find_files(directory, pattern='*'):
    '''Recursively finds all files matching the pattern.'''
    files = []
    for root, dirnames, filenames in os.walk(directory):
        for filename in fnmatch.filter(filenames, pattern):
            files.append(os.path.join(root, filename))
    return files

def get_file_wordcount(filename):
    cnt = 0
    with open(filename,'r') as file:
        content = file.read()
        lines = content.split()
        for word in lines:
            cnt += 1
    return filename, cnt

files = find_files(dir)

def main():
    num_defective_files = 0
    try:
        for filename in files:
            (fn, cnt) = get_file_wordcount(filename)
            if cnt < min_values:
                print(f'File {fn} contains {cnt} values.')
                num_defective_files +=1
        if num_defective_files > 0:
            print(f'WARNING: {num_defective_files} files containing fewer than {min_values} values were detected.')
        else:
            print('All sample files OK.')
    except:


if __name__ == '__main__':
    main()





