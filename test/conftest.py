"""
Common test functionality.
"""

import logging

from pytest import register_assert_rewrite

from codesynth.ast import BaseNode

pytest_plugins = ["pytest_powerpack"]
register_assert_rewrite("pytest_powerpack")

# only import after registering assert rewrite
from pytest_powerpack import ComparisonFiles, compare_files

logging.basicConfig(level=logging.DEBUG)


def check_node(node: BaseNode, comparison_files: ComparisonFiles):
    """
    Convenience function to render provided node and check it against
    the corresponding compare file.
    """
    node.render_file(comparison_files.build_file)
    compare_files(comparison_files)
