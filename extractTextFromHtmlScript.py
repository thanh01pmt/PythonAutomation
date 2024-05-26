import re
from bs4 import BeautifulSoup

# Function to extract text from all tags in a given HTML content
def extract_text_from_all_tags(html_content):
    """
    This function extracts text from all tags in a given HTML content.
    It uses BeautifulSoup to parse the HTML content and extract text from all tags.
    It also handles ordered and unordered lists and formats the result as a markdown list.
    """
    # Initialize BeautifulSoup with the HTML content and 'html.parser'
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Initialize an empty string to store the extracted text
    text = ''
    
    # Iterate through all tags in the HTML content
    for tag in soup.find_all():
        # Check if the tag is an image ('img')
        if tag.name == 'img':
            # If the image has an 'alt' attribute, add it to the text
            if 'alt' in tag.attrs:
                text += 'Hình.' + tag['alt'] + '(' + tag['src'] + ') '
        # Check if the tag is one of the supported text-containing tags
        elif tag.name in ['p', 'div', 'span', 'a', 'em', 'strong', 'i', 'b', 'u', 'sub', 'sup', 'code', 'pre', 'blockquote', 'q', 'cite', 'mark', 'ins', 'del', 's', 'strike', 'small', 'big', 'abbr', 'acronym', 'dfn', 'kbd', 'samp', 'var', 'time', 'progress', 'meter', 'label', 'legend', 'caption', 'thead', 'tbody', 'tfoot', 'th', 'td', 'tr', 'colgroup', 'col', 'li', 'dd', 'dt']:
            # Add the text content of the tag to the extracted text
            text += tag.get_text() + ' '
        # Check if the tag is an ordered list ('ol')
        elif tag.name == 'ol':
            # Initialize a counter for the list items
            counter = 1
            # Iterate through all list items ('li') in the ordered list
            for li in tag.find_all('li'):
                # Add the list item number and text to the extracted text
                text += f'{counter}. {li.get_text()} '
                # Increment the counter
                counter += 1
        # Check if the tag is an unordered list ('ul')
        elif tag.name == 'ul':
            # Iterate through all list items ('li') in the unordered list
            for li in tag.find_all('li'):
                # Add a bullet point and the list item text to the extracted text
                text += f'- {li.get_text()} '
            
    # Return the extracted text after stripping leading and trailing whitespaces
    return text.strip()

# Example usage:

filePath = '/Users/tonypham/Documents/Books/OPS/glossary.html'
with open(filePath, 'r') as f:
    html_content = f.read()
    text = extract_text_from_all_tags(html_content)
    print('Text:', text)
    # Mở file với chế độ ghi ('w')
    with open(filePath + '.txt', 'w') as f:
        # Ghi nội dung text vào file
        f.write(text)