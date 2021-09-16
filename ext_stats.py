import sys
import os


class NotValidDirectoryException(Exception):
    pass

def get_filepath():
    if len(sys.argv) > 1:
        if not os.path.isdir(sys.argv[1]):        
            raise NotValidDirectoryException
        filepath = sys.argv[1]
    else:
        filepath = '.'

    return filepath


def calculate_stats(key, output, size, max_size):
    stats_list = [1, size, size]  # list with 3 elements: count, max_size, total_size
    if not key in output:
        output[key] = stats_list
    else:           
        if size > max_size:
            max_size = size
            output[key][1] = max_size  # get max size
        output[key][0] += 1  # increment count      
        output[key][2] += size  # add to total size


def walk_dir_and_calculate():
    output = {}
    for path, dirs, files in os.walk(get_filepath()):
        max_size = 0
        for filename in files:
            key = os.path.splitext(filename)[1].lower()
            size = os.path.getsize(os.path.join(path, filename))

            calculate_stats(key, output, size, max_size)
    return output


def write_to_file(output):
    text = '{:>12} {:>12} {:>12} {:>12}\n'.format('Extension', 'Count', 'Max size', 'Total size')
    
    for key,value in output.items():
        line = '{:>12} {:>12} {:>12} {:>12}'.format(key, *value)
        print(line)
        text += line + '\n'
    
    with open("output.txt", "a") as text_file:
        text_file.write(text)



if __name__  == '__main__':
    output = walk_dir_and_calculate()
    write_to_file(output)
