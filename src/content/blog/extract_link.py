import os
from bs4 import BeautifulSoup

def extract_links_from_html(html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parse HTML content
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all <a> tags with href attributes
    links = soup.find_all('a', href=True)

    # Extract href attributes from <a> tags
    extracted_links = [link['href'] for link in links]

    return extracted_links

def write_links_to_file(links, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for link in links:
            file.write(link + '\n')

def collect_links_from_folder(folder_path, output_file):
    all_links = set()  # To store unique links

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.html'):
            html_file = os.path.join(folder_path, file_name)
            try:
                links = extract_links_from_html(html_file)
                for link in links:
                    if 'answers' in link:
                        all_links.add(link)
            except Exception as e:
                print(f"Error processing '{html_file}': {e}")

    write_links_to_file(all_links, output_file)
    print(f"Links collected from HTML files in '{folder_path}' have been written to '{output_file}'.")

# Example usage:
folder_path = 'html_files'  # Replace with the path to your HTML files folder
output_file = 'collected_links.txt'  # Replace with the desired output text file path

collect_links_from_folder(folder_path, output_file)
