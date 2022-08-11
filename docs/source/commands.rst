=======
Title
=======


Section A
-------

Section B
----------


"""
        self.assertEqual(expected, self.render_doc(doc))

    def test_nested_sections(self):
        doc = """

""""