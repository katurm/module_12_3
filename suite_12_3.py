import unittest
import tests_12_1
import tests_12_2

testSuit = unittest.TestSuite()
testSuit.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
testSuit.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))

test = unittest.TextTestRunner(verbosity=2)
test.run(testSuit)
