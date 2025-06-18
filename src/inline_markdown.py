import re
from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches




def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        node_key = extract_markdown_images(old_node.text)
        if node_key == []:
            new_nodes.append(old_node)
            continue
        og_text = old_node.text
        for key in node_key:
            section = og_text.split(f"![{key[0]}]({key[1]})",1)
            if len(section) < 2:
                raise ValueError("Too Few")
            if section[0] != "":
                new_nodes.append(TextNode(section[0], TextType.TEXT))
            new_nodes.append(TextNode(key[0], TextType.IMAGE, key[1]))
            og_text = section[1]
        if og_text != "":
            new_nodes.append(TextNode(og_text, TextType.TEXT))
    return new_nodes
            
def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        node_key = extract_markdown_links(old_node.text)
        if node_key == []:
            new_nodes.append(old_node)
            continue
        og_text = old_node.text
        for key in node_key:
            section = og_text.split(f"[{key[0]}]({key[1]})",1)
            if len(section) < 2:
                raise ValueError("Too Few")
            if section[0] != "":
                new_nodes.append(TextNode(section[0], TextType.TEXT))
            new_nodes.append(TextNode(key[0], TextType.LINK, key[1]))
            og_text = section[1]
        if og_text != "":
            new_nodes.append(TextNode(og_text, TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes,"`",TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes









