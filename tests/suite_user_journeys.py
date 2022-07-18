"""
Test runner. Creates a suite of tests.
"""
from sys import path

path.append(path[0] + "/..")

from unittest import TestLoader, TestSuite, TextTestRunner

from test_comment_journey import TestComments
from test_topics_journey import TestTopics

if __name__ == "__main__":
    test_loader = TestLoader()
    test_suite = TestSuite(
        (
            test_loader.loadTestsFromTestCase(TestComments),
            test_loader.loadTestsFromTestCase(TestTopics),
        )
    )
    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)
