import os
import glob
import re

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

def combine_xhtml_files(directory, output_file):
    """
    This function combines all xhtml files in the given directory into a single file, while removing absolute positioning attributes and applying custom styles.
    """
    xhtml_files = glob.glob(os.path.join(directory, "*.xhtml"))
    # Sort the file names in ascending order
    xhtml_files.sort()
    with open(output_file, "w") as outfile:
        outfile.write('<!DOCTYPE html>\n<html>\n<head>\n<meta charset="UTF-8">\n<title>Combined XHTML</title>\n')
        outfile.write('<link rel="stylesheet" href="css/book.css" type="text/css"></link>\n<script src="js/book.js"></script>\n')
        outfile.write('<style>\nbody { max-width: 720px; }\n')
        outfile.write('img { max-width: 100%; height: auto; }\n')
        outfile.write('p { white-space: normal; }\n')
        outfile.write('</style>\n</head>\n<body>\n')
        for file in xhtml_files:
            with open(file, "r") as infile:
                content = infile.read()
                match = re.search(r"<body[^>]*>(.*?)</body>", content, re.DOTALL)
                if match:
                    body_content = match.group(1)
                    body_content = remove_absolute_positioning_attributes(body_content)
                    outfile.write(body_content)
        outfile.write('</body>\n</html>')

# Example usage:
directory = "/Users/tonypham/Documents/Books/OPS"
output_file = directory + "/glossary.html"
# output_file = "combined1.html"
combine_xhtml_files(directory, output_file)