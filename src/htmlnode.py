

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    def __eq__(self, other):
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
            )
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
    def to_html(self):
        raise NotImplementedError("to_html methond not implemented")
    
    def props_to_html(self):
        html = ""
        if self.props is None:
            return html
        for prop in self.props:
            html += f' {prop}="{self.props[prop]}"'    
        return html
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode-to_HTML: No Value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag},{self.value},{self.props})"
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"
    
    def to_html(self):
        result = ""
        if self.tag is None:
            raise ValueError("ParentNode: No Tag value")
        if self.children is None:
            raise ValueError("ParentNode: No Children")
        for child in self.children:
            result += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{result}</{self.tag}>"
    

   
