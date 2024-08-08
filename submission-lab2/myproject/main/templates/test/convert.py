import os
import re

def convert_to_static_tag(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Convert src and href attributes
    content = re.sub(r'src="([^"]+)"', r'src="{% static \'\1\' %}"', content)
    content = re.sub(r'href="([^"]+)"', r'href="{% static \'\1\' %}"', content)
    content = re.sub(r'url\("([^"]+)"\)', r'url("{% static \'\1\' %}")', content)
    
    # Ensure no nested {% static %} tags
    content = re.sub(r'{% static \'[{% static ]+\' ([^%]+) %}\' %}', r'{% static \'\1\' %}', content)
    content = content.replace("\\", "")  # Remove any escaped characters

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def process_html_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                convert_to_static_tag(file_path)
                print(f"Processed {file_path}")

if __name__ == "__main__":
    directory = os.path.dirname(os.path.abspath(__file__))
    process_html_files(directory)
    print("Processing completed.")
