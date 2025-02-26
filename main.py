import base64
import json
import os

def decode_and_save_markdown(data):
    # Create the directory if it doesn't exist
    os.makedirs('markdowns', exist_ok=True)
    
    # Load the JSON data
    entries = json.loads(data)
    
    for entry in entries:
        # Get the last part of the repoUrl
        repo_name = entry['repoUrl'].rstrip('/').split('/')[-1]
        
        # Decode the base64 markdown
        markdown_content = base64.b64decode(entry['markdownEncoded']).decode('utf-8')
        
        # Create the file
        filename = f"markdowns/{repo_name}.md"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print(f"Created file: {filename}")

# Example usage
with open('./data/markdown.json', 'r', encoding='utf-8') as f:
    data = f.read()
    decode_and_save_markdown(data)