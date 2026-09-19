import unittest
from market_intelligence import Case, analyze_markets

class MarketTests(unittest.TestCase):
    def test_undersupplied_high_value_market_ranks_first(self):
        cases=[Case("Alpha","Commercial",100,20),Case("Alpha","Employment",100,20),Case("Beta","Maritime",200,2),Case("Beta","Maritime",200,2)]
        result=analyze_markets(cases)
        self.assertEqual(result[0].city,"Beta")
        self.assertEqual(result[0].top_case_type,"Maritime")
    def test_empty_input(self): self.assertEqual(analyze_markets([]),[])

if __name__=="__main__": unittest.main()
