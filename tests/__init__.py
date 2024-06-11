##########################################################################################
# textkernel/tests/__init__.py
##########################################################################################

import unittest

from tests.test_name_grammar  import *  # noqa: F401 F403
from tests.test_value_grammar import *  # noqa: F401 F403
from tests.test_from_text     import *  # noqa: F401 F403
from tests.test_from_file     import *  # noqa: F401 F403

##########################################################################################
# Perform unit testing if executed from the command line
##########################################################################################

if __name__ == '__main__':
    unittest.main()

##########################################################################################
