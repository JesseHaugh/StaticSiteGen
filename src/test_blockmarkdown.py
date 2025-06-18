import unittest

from block_markdown import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode

class TestMarkDownBlock(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
    
    def test_block_to_blocktype_heading(self):
        block = "### HEADING TEST"
        b_type = block_to_block_type(block)
        self.assertEqual(
            b_type, BlockType.HEADING
        )
    
    def test_block_to_blocktype_code(self):
        block = "``` TEST CODE ```"
        b_type = block_to_block_type(block)
        self.assertEqual(
            b_type, BlockType.CODE
        )
    
    def test_block_to_blocktype_quote(self):
        block = "> TEST QUOTE\n> TEST THIS"
        b_type = block_to_block_type(block)
        self.assertEqual(
            b_type, BlockType.QUOTE
        )
    
    def test_block_to_blocktype_quote_false(self):
        block = "> TEST QUOTE\n TEST THIS"
        b_type = block_to_block_type(block)
        self.assertNotEqual(
            b_type, BlockType.QUOTE
        )

    def test_block_to_blocktype_unordered(self):
        block = "- TEST unordered\n- TEST THIS\n- what why"
        b_type = block_to_block_type(block)
        self.assertEqual(
            b_type, BlockType.UNORDERED_LIST
        )

    def test_block_to_blocktype_unordered_broken(self):
        block = "- TEST unordered\n- TEST THIS\n what why"
        b_type = block_to_block_type(block)
        self.assertNotEqual(
            b_type, BlockType.UNORDERED_LIST
        )

    def test_block_to_blocktype_ordered(self):
        block = "1. TEST unordered\n2. TEST THIS\n3. what why"
        b_type = block_to_block_type(block)
        self.assertEqual(
            b_type, BlockType.ORDERED_LIST
        )
    
    def test_block_to_blocktype_ordered_not(self):
        block = "1. TEST unordered\n2. TEST THIS\n4. what why"
        b_type = block_to_block_type(block)
        self.assertNotEqual(
            b_type, BlockType.ORDERED_LIST
        )

    def test_block_to_blocktype_paragraph(self):
        block = "Just a paragraph"
        b_type = block_to_block_type(block)
        self.assertEqual(
            b_type, BlockType.PARAGRAPH
        )

    def test_paragraphs(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_Lists(self):
        md = """
This is a Unordered List:

- Topic 1
- Topic 2
- Topic 3

This is a ordered list:

1. Topic 1
2. Topic 2
3. Topic 3
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is a Unordered List:</p><ul><li>Topic 1</li><li>Topic 2</li><li>Topic 3</li></ul><p>This is a ordered list:</p><ol><li>Topic 1</li><li>Topic 2</li><li>Topic 3</li></ol></div>",
        )
    def test_Headers(self):
        md = """
this is a Test header

# Header 1

This is a test paragraph

## Header 2
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>this is a Test header</p><h1>Header 1</h1><p>This is a test paragraph</p><h2>Header 2</h2></div>",
        )
    def test_quoteblock(self):
        md = """
this is a Test quote block

> Test Quote Block

test paragraph
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>this is a Test quote block</p><blockquote>Test Quote Block</blockquote><p>test paragraph</p></div>",
        )













if __name__ == "__main__":
    unittest.main()