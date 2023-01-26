from get_recommendations import get_recommendations
from import_response_plans import update_response_plan, import_response_plans
import unittest

class TestRecommendations(unittest.TestCase):
    def test_med1_ba0001(self):
        recommendation = get_recommendations('MED1', 'BA0001')
        self.assertEqual(recommendation, "MED1: ['M1', 'E2']")
    def test_bls1_lf258(self):
        recommendation = get_recommendations('BLS1', 'LF258')
        self.assertEqual(recommendation, "BLS1: ['L14']")
    def test_bls1_tf161(self):
        recommendation = get_recommendations('BLS1', 'TF161')
        self.assertEqual(recommendation, "BLS1: ['M18']")
    def test_mvc_df414(self):
        recommendation = get_recommendations('MVC', 'DF414')
        self.assertEqual(recommendation, "MVC: ['E21', 'M21']")
    def test_update_mvc_rfa(self):
        update_response_plan('SNO911', '31D01_rfa', 'MVC', [['Engine', 'Ladder'], 'Aid Unit'])
        data = import_response_plans()
        self.assertEqual(data['SNO911']['31D01_RFA']['MVC'], [['Engine', 'Ladder'], 'Aid Unit'])
    def test_updated_mvc_df414(self):
        recommendation = get_recommendations('MVC', 'DF414')
        self.assertEqual(recommendation, "MVC: ['E21', 'A15']")

if __name__ == '__main__':
    unittest.main()