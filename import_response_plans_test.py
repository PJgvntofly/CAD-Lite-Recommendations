from import_response_plans import import_response_plans, update_response_plan
import unittest

class TestResponsePlans(unittest.TestCase):
    def test_tac_1(self):
        data = import_response_plans()
        self.assertEqual(data['SNO911']['TAC-1']['BLS'], [["Aid Unit", "Engine", "Ladder"]])
    
    def test_create_new_agency(self):
        update_response_plan('ValleyCOM', 'Test', 'Engine')
        data = import_response_plans()
        self.assertEqual(data['VALLEYCOM']['TEST'], ['Engine'])
    def test_create_new_plan(self):
        update_response_plan('ValleyCOM', 'Test2', 'Engine')
        data = import_response_plans()
        self.assertEqual(data['VALLEYCOM']['TEST'], ['Engine'])
        self.assertEqual(data['VALLEYCOM']['TEST2'], ['Engine'])
    def test_update_existing_plan(self):
        update_response_plan('ValleyCOM', 'Test2', ['Engine', 'Aid Car'])
        data = import_response_plans()
        self.assertEqual(data['VALLEYCOM']['TEST'], ['Engine'])
        self.assertEqual(data['VALLEYCOM']['TEST2'], ['Engine', 'Aid Car'])
        self.assertEqual(data['SNO911']['TAC-1']['BLS'], [["Aid Unit", "Engine", "Ladder"]])
        

if __name__ == '__main__':
    unittest.main()
