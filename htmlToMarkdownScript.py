import os
import subprocess

def convert_html_to_markdown(html_file, markdown_file):
    command = ['pandoc', html_file, '-t', 'markdown', '-o', markdown_file]
    subprocess.run(command)

# Example usage:
html_file = "/Users/tonypham/Documents/Books/OPS/unit2.html"
markdown_file = "/Users/tonypham/Documents/Books/OPS/unit2.md"
convert_html_to_markdown(html_file, markdown_file)