"""
Unittest for the Basecode.py 
"""

import basecode


class TestBasecode:
	
	def test_add(self): 
		assert basecode.add(2,5) == 7
		
