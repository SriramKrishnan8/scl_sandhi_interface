#!/usr/bin/env python3

import unittest
import sandhi_words as sw

class TestSandhi(unittest.TestCase):
    
    def test_sandhi(self):
        self.assertEqual(sw.sandhi_join("rAma", "AlayaH", False), "rAmAlayaH", "Should be \"rAmAlayaH\"")
        self.assertEqual(sw.sandhi_join("lakRmIvAn", "SuBalakRaNaH", False), "lakRmIvAFCuBalakRaNaH", "Should be \"lakRmIvAFCuBalakRaNaH\"")
    

if __name__ == '__main__':
    unittest.main()
