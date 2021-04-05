import sys
import unittest
from tests.unit_tests.business_logic import test_helper_functions

if __name__=='__main__':
    suite = unittest.TestSuite()
    modules = [
        test_helper_functions
    ]

    for module in modules:
        suite.addTest(unittest.TestLoader().loadTestsFromModule(module))

    runner = unittest.TextTestRunner(verbosity=3)
    runner.run(suite)