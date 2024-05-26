# import os
# import subprocess

# def convert_html_to_markdown(html_file, markdown_file):
#     command = ['pandoc', html_file, '-t', 'markdown', '-o', markdown_file]
#     subprocess.run(command)

# # Example usage:
# html_file = "/Users/tonypham/Documents/Books/OPS/unit2.html"
# markdown_file = "/Users/tonypham/Documents/Books/OPS/unit2.md"
# convert_html_to_markdown(html_file, markdown_file)


import html2markdown

def html_to_markdown(html_file):
    with open(html_file, 'r') as f:
        html_content = f.read()
    
    markdown_content = html2markdown.convert(html_content)
    
    with open(html_file + '.md', 'w') as f:
        f.write(markdown_content)

html_to_markdown('/Users/tonypham/Documents/Books/OPS/glossary.html')