from pytest import mark
from pytest_powerpack import ComparisonFiles

from .conftest import check_node

from codesynth.lib import (
    InlineTextNode,
    CurlyBracketBlockNode,
)


@mark.powerpack_compare_file("foo.c")
def test_braces(powerpack_comparison_files: ComparisonFiles):
    """
    Generate C function with an "if" check.
    """

    foo = CurlyBracketBlockNode(
        descriptor="int foo(int a)",
        spacer="\n",
        children=[
            InlineTextNode("// only print if zero"),
            CurlyBracketBlockNode(
                descriptor="if (a == 0)",
                children=[InlineTextNode('printf("Got zero");')],
            ),
            InlineTextNode("return a + 1;"),
        ],
    )

    check_node(foo, powerpack_comparison_files)
