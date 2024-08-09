import os
import re

def convert_to_static_tag(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Define the header and footer sections
    header_pattern = re.compile(r'<header>.*?</header>', re.DOTALL)
    footer_pattern = re.compile(r'<!-- Start Footer.*?<!-- End Footer -->', re.DOTALL)

    # Check if the content contains the header and footer sections
    if header_pattern.search(content) and footer_pattern.search(content):
        # Replace the header and footer with block content tags
        content = header_pattern.sub('{% block content %}', content)
        content = footer_pattern.sub('{% endblock %}', content)

        # Add the extends statement at the top of the file
        content = '{% extends \'base.html\' %}\n\n' + content

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Processed and modified {file_path}")
    else:
        print(f"No matching header and footer found in {file_path}")

def process_html_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                convert_to_static_tag(file_path)

if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))
    process_html_files(directory)
    print("Processing completed.")
