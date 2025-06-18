from enum import Enum
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"





def markdown_to_blocks(markdown):
    result = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block != "":
            result.append(block.strip())
    return result

def block_to_block_type(markdown):
    headings = ["# ","## ","### ","#### ", "##### ", "###### "]
    mark_list = markdown.split("\n")
    order_count = 1
    for head in headings:
        if head in markdown:
            return BlockType.HEADING
    if markdown[:3] and markdown[-3:] == "```":
        return BlockType.CODE
    for quote in mark_list:
        if quote[0] != ">":
            break
        if quote == mark_list[-1]:
            return BlockType.QUOTE
    for unordered in mark_list:
        if unordered[:2] != "- ":
            break
        if unordered == mark_list[-1]:
            return BlockType.UNORDERED_LIST
    for ordered in mark_list:
        if ordered[:3] != f"{order_count}. ":
            break
        order_count += 1
        if ordered == mark_list[-1]:
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_html(text):
    text_node = text_to_textnodes(text)
    html = ""
    for node in text_node:
        html_node = text_node_to_html_node(node)
        html += html_node.to_html()
    return html

def text_html_strip(text, delim):
    return text.strip(delim)

def text_html_replace(text, delim, replace):
    return text.replace(delim, replace)

def extract_ordered_list(text):
    matches = re.findall(r"^\s*\d+\.\s(.*)$", text, re.MULTILINE)
    return matches

def text_to_lists(text,block_type):
    if block_type == BlockType.UNORDERED_LIST:
        text_split = text.split("- ")
        children = []
        for split in text_split:
            if split != "":
                children.append(LeafNode("li", split.strip()))
        return ParentNode("ul", children)
    if block_type == BlockType.ORDERED_LIST:
        text_split = extract_ordered_list(text)
        children = []
        for split in text_split:
            children.append(LeafNode("li", split.strip()))
        return ParentNode("ol", children)
    

def text_to_children(text, block_type):
    if block_type == BlockType.HEADING:
        matches = re.findall(r"^\s*\#{1,6}\s(.*)$", text, re.MULTILINE)
        count = text.count("#")
        return LeafNode(f"h{count}",markdown_to_html(matches[0]))
    if block_type == BlockType.PARAGRAPH:
        text = text.replace("\n", " ")
        return LeafNode("p",markdown_to_html(text))
    if block_type == BlockType.QUOTE:
        text = text_html_strip(text, "> ")
        return LeafNode("blockquote", markdown_to_html(text))
    if block_type == BlockType.ORDERED_LIST or BlockType.UNORDERED_LIST:
        return text_to_lists(text, block_type)


def markdown_to_html_node(markdown):
    new_node = []
    mark_block = markdown_to_blocks(markdown)
    for block in mark_block:
        block_type = block_to_block_type(block)
        if block_type != BlockType.CODE:
            node = text_to_children(block,block_type)
            new_node.append(node)
        else:
            code_node = [LeafNode("code",block.lstrip("```\n").rstrip("```"))]
            new_node.append(ParentNode("pre",code_node))

    return ParentNode("div",new_node)


