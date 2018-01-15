import unittest
import calculateEloLadder
import pandas

class TestCalculateELoLadder(unittest.TestCase):

	def test_importPlayers_columnSize_and_rowSize(self):
		result = calculateEloLadder.importPlayers()
		expectedColumnSize = 5
		# Check if get expected result
		self.assertNotEqual(1, result.shape[0])
		self.assertEqual(expectedColumnSize, result.shape[1])

	def 

	
if __name__ == '__main__':
	unittest.main()