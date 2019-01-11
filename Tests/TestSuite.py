import unittest
from Tests.TestClass import TestClass
import os


class Snapshots(unittest.TestCase):
    def cleanup(self):
        for root, dirs, files in os.walk('../Snapshots'):
            for f in files:
                os.unlink(os.path.join(root, f))


def suite():
    suite = unittest.TestSuite()
    suite.addTest(Snapshots('cleanup'))
    suite.addTest(TestClass('test_01_login'))
    suite.addTest(TestClass('test_02_create_contact'))
    suite.addTest(TestClass('test_03_delete_contact'))
    suite.addTest(TestClass('test_04_create_ticket'))
    suite.addTest(TestClass('test_05_delete_ticket'))
    suite.addTest(TestClass('test_06_create_deal'))
    suite.addTest(TestClass('test_07_delete_deal'))
    suite.addTest(TestClass('test_08_create_snippet'))
    suite.addTest(TestClass('test_09_delete_snippet'))
    suite.addTest(TestClass('test_10_create_company'))
    suite.addTest(TestClass('test_11_delete_company'))
    suite.addTest(TestClass('test_12_create_document'))
    suite.addTest(TestClass('test_13_delete_document'))
    suite.addTest(TestClass('test_14_create_task'))
    suite.addTest(TestClass('test_15_delete_task'))
    suite.addTest(TestClass('test_16_create_template'))
    suite.addTest(TestClass('test_17_delete_template'))
    suite.addTest(TestClass('test_18_create_report'))
    suite.addTest(TestClass('test_19_delete_report'))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(failfast=True)
    runner.run(suite())