import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("This is a Tag", "value", "children", "props")
        node2 = HTMLNode("This is a Tag", "value", "children",  "props")
        self.assertEqual(node, node2)
    
    def test_neq(self):
        node = HTMLNode("This is a Tag", "value", "children", "props")
        node2 = HTMLNode("This is a Tag1", "value2", "children1",  "props1")
        self.assertNotEqual(node, node2)

    def test_dicteq(self):
        node = HTMLNode("This is a Tag", "", "children", {"href": "https://www.google.com", "target": "_blank"})
        node2 = HTMLNode("This is a Tag", "", "children",  {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node, node2)

    def test_nonetest(self):
        node = HTMLNode("This is a Tag", "value")
        node2 = HTMLNode("This is a Tag", "value")
        self.assertEqual(node, node2)

    def test_props_to_html(self):
        node = HTMLNode("This is a Tag", "", "children", {"href": "https://www.google.com", "target": "_blank"}).props_to_html()
        node2 = HTMLNode("This is a Tag", "", "children",  {"href": "https://www.google.com", "target": "_blank"}).props_to_html()
        self.assertEqual(node, node2)

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, None, {'class': 'primary'})",
        )
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    def test_leaf_to_html_none(self):
        node = LeafNode(None, "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "Click me!")



if __name__ == "__main__":
    unittest.main()