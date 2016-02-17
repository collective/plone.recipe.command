import unittest
import io
import sys
import tempfile

from plone.recipe.command import Recipe

test_cfg = '''
[buildout]
parts = template
offline = true

[template]
recipe = collective.recipe.template[genshi]:genshi
input = template.in
output = template
some-option = value
'''


class PloneRecipeCommandTest(unittest.TestCase):

    def test_test(self):
        out = tempfile.NamedTemporaryFile()
        recipe = Recipe(None, 'command',
                        {'command': 'echo "Install" > %s' % out.name,
                         'update-command': 'echo "Update" > %s' % out.name})
        recipe.install()

        out.flush()
        out.seek(0)
        output = out.read()
        self.assertEqual(output, 'Install\n')
        recipe.update()
        out.flush()
        out.seek(0)
        output = out.read()
        self.assertEqual(output, 'Update\n')
