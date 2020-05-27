import unittest

import asserts
import masTest

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromModule(asserts))
    suite.addTests(loader.loadTestsFromModule(masTest))
    runner = unittest.TextTestRunner(verbosity=3)
    results = runner.run(suite)
