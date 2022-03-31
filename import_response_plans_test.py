from import_response_plans import import_response_plans, update_response_plan
import unittest

class TestResponsePlans(unittest.TestCase):
    def test_tac_1(self):
        data = import_response_plans()
        self.assertEqual(data['SNO911']['TAC-1']['BLS'], [["Aid Unit", "Engine", "Ladder"]])
    
    def test_create_new_agency(self):
        update_response_plan('ValleyCOM', 'Test_Zone', 'Test', ['Engine'])
        data = import_response_plans()
        self.assertEqual(data['VALLEYCOM']['TEST_ZONE']['TEST'], ['Engine'])
    
    def test_create_new_zone(self):
        update_response_plan('ValleyCOM', 'Test_Zone2', 'Test', ['Engine'])
        data = import_response_plans()
        self.assertEqual(data['VALLEYCOM']['TEST_ZONE']['TEST'], ['Engine'])
        self.assertEqual(data['VALLEYCOM']['TEST_ZONE2']['TEST'], ['Engine'])
    
    def test_add_plan_to_zone(self):
        update_response_plan('ValleyCom', 'Test_zone', 'test2', ['Engine', 'Aid Unit'])
        data = import_response_plans()
        self.assertEqual(data['VALLEYCOM']['TEST_ZONE']['TEST2'], ['Engine', 'Aid Unit'])
    
    def test_update_existing_plan(self):
        update_response_plan('ValleyCOM', 'Test_Zone', 'Test2', ['Engine', ['Aid Unit', 'Medic Unit']])
        data = import_response_plans()
        self.assertEqual(data['VALLEYCOM']['TEST_ZONE']['TEST'], ['Engine'])
        self.assertEqual(data['VALLEYCOM']['TEST_ZONE']['TEST2'], ['Engine', ['Aid Unit', 'Medic Unit']])
        self.assertEqual(data['SNO911']['TAC-1']['BLS'], [["Aid Unit", "Engine", "Ladder"]])
        

if __name__ == '__main__':
    unittest.main()
