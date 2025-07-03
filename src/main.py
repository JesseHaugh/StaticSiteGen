from textnode import TextNode, TextType
import os
import shutil
import re
from block_markdown import markdown_to_html_node
import sys

full_final_path = "docs/"
full_content_path = "content/"
full_template_path = "template.html"

def main():
    basepath = sys.argv[1]
    clear_dir(full_final_path)
    copy_dir("./static/", full_final_path)
    generate_page(full_content_path,full_template_path,full_final_path, basepath)


def clear_dir(path):
    if os.path.exists(path) is True:
        shutil.rmtree(path)
    os.mkdir(path)

def copy_dir(copy_path,final_path):
    dir_list = os.listdir(copy_path)
    for file in dir_list:
        if os.path.isfile(copy_path+file):
            shutil.copy(copy_path+file, final_path+file)
        else:
            os.mkdir(final_path+file)
            copy_dir(f"{copy_path}{file}/", f"{final_path}{file}/")
    
def extract_title(markdown):
    match = re.findall(r"^\#{1}\s(.*)$", markdown, re.MULTILINE)
    if match == []:
        raise Exception("No Title")
    return match[0].strip()

def generate_page(from_path, template_path, dest_path, basepath="/"):
    print(f"Generating Page from {from_path} to {dest_path} using {template_path}")
    dir_list = os.listdir(from_path)
    for file in dir_list:
        if os.path.isfile(from_path+file):
            with open(from_path+file) as f:
                markdown = f.read()
            with open(template_path) as f:
                template = f.read()
            title = extract_title(markdown)
            content = markdown_to_html_node(markdown)
            html = content.to_html()
            template = template.replace('href="/', f'href="{basepath}').replace('src="/',f'src="{basepath}').replace("{{ Title }}", title).replace("{{ Content }}", html)
            with open(dest_path+file.replace(".md", ".html"), "w") as f:
                f.write(template)
        else:
            os.mkdir(dest_path+file)
            generate_page(f"{from_path}{file}/", template_path, f"{dest_path}{file}/", basepath)


main()