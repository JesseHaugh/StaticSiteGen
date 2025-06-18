
def split_nodes_imageold(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        node_key = extract_markdown_images(old_node.text)
        sections = old_node.text.replace("![","&~&").replace("](","&~&").replace(")","&~&").split("&~&")
        split_node = []
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if (sections[i], sections[i+1]) in node_key:
                split_node.append(TextNode(sections[i], TextType.IMAGE, sections[i+1]))
                continue
            if (any(sections[i] in tu for tu in node_key)):
                continue
            else:
                split_node.append(TextNode(sections[i], TextType.TEXT))
        new_nodes.extend(split_node)
    return new_nodes
            
def split_nodes_linkold(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        node_key = extract_markdown_links(old_node.text)
        sections = old_node.text.replace("[","&~&").replace("](","&~&").replace(")","&~&").split("&~&")
        split_node = []
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if (sections[i], sections[i+1]) in node_key:
                split_node.append(TextNode(sections[i], TextType.LINK, sections[i+1]))
                continue
            if (any(sections[i] in tu for tu in node_key)):
                continue
            else:
                split_node.append(TextNode(sections[i], TextType.TEXT))
        new_nodes.extend(split_node)
    return new_nodes


                

    


# Old Personal Code
#def split_nodes_delimiter(old_nodes, delimiter, text_type):
#    new_nodes = []
#    delim_char = ""
#    for node in old_nodes:
#        for char in node.text.split(" "):
#            if delimiter in char:
#                delim_char = char.replace(delimiter,"")
#                break
#        split_node = node.text.split(delimiter)
#        for split in split_node:
#            if delim_char in split and delim_char != "":
#                new_nodes.append(TextNode(split,text_type))
#                delim_char = ""
#            else:
#                if split != "":
#                    new_nodes.append(TextNode(split,TextType.TEXT))
#    return new_nodes
