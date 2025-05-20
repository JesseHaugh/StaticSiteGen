

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
        for prop in self.props:
            html += f' {prop}="{self.props[prop]}"'    
        return html
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, children=None, props=None):
        super().__init__(tag, value, children, props)
    
    def to_html(self):
        if self.tag == "p":
            return f"<p>{self.value}</p>"
        if self.tag == "a":
            return f'<a href="{self.children["href"]}">{self.value}</a>'
        if self.tag is None:
            return self.value
        
