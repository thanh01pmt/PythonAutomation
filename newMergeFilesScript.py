import os
import glob
import re

def get_file_list(directory, start_number, end_number):
    file_list = []
    for i in range(start_number, end_number):
        file_name = f'page-{i}.xhtml'
        file_path = os.path.join(directory, file_name)
        file_list.append(file_path)
    return file_list

def remove_absolute_positioning_attributes(html):
    """
    This function removes style attributes with absolute positioning and individual absolute positioning attributes from the given html string.
    """
    # Remove style attributes with absolute positioning
    html = re.sub(r'style="[^"]*position:absolute[^"]*"', '', html)
    # Remove individual absolute positioning attributes
    html = re.sub(r'left:[^;]+;', '', html)
    html = re.sub(r'top:[^;]+;', '', html)
    # html = re.sub(r'width:[^;]+;', '', html)
    # html = re.sub(r'height:[^;]+;', '', html)
    return html

def combine_xhtml_files(directory, files, output_name):
    with open(os.path.join(directory, output_name), "w") as outfile:
        outfile.write('<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8">\n<title>Combined XHTML</title>\n')
        outfile.write('<link rel="stylesheet" href="css/book.css" type="text/css"></link>\n<script src="js/book.js"></script>\n')
        outfile.write('<style>\nbody { max-width: 720px; }\n')
        outfile.write('img { max-width: 100%; height: auto; }\n')
        outfile.write('p { white-space: normal; }\n')
        outfile.write('</style>\n</head>\n<body>\n')
        for file in files:
            with open(os.path.join(directory, file), "r") as infile:
                content = infile.read()
                match = re.search(r"<body[^>]*>(.*?)</body>", content, re.DOTALL)
                if match:
                    body_content = match.group(1)
                    body_content = remove_absolute_positioning_attributes(body_content)
                    outfile.write(body_content)
        outfile.write('</body>\n</html>')

def process_split_index(split_index, directory):
    result = []
    for i in range(len(split_index) - 1):
        start_number = split_index[i]
        end_number = split_index[i + 1]
        file_list = get_file_list(directory, start_number, end_number)
        result.append(file_list)
    return result


# Example usage:
directory = "/Users/tonypham/Documents/Books/OPS"
base_name = "unit2"
output_name = ""
split_index = [175,310,431]

input_files = process_split_index(split_index, directory)


for files in input_files:
    output_name = f"{base_name}_{input_files.index(files) + 1}.html"
    combine_xhtml_files(directory, files, output_name)

