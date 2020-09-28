import unittest
from xmlrunner import xmlrunner
from accountSignupTest import MbrTest


mbr_test_job = unittest.TestLoader().loadTestsFromTestCase(MbrTest)
mbr_test_job_job = unittest.TestSuite([mbr_test_job])

xmlrunner.XMLTestRunner(verbosity=2, output= 'test-reports').run(mbr_test_job_job)

