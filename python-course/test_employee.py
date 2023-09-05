import unittest
import Employee_Unit
from unittest.mock import patch
class TestEmployee (unittest.TestCase):
    # this method will run before test and second method run after that single test finished
    # def setUp(self):
    #     self.emp1 = Employee_Unit.Employee_Unit("coronary","schafer",50000)
    #     self.emp2 = Employee_Unit.Employee_Unit("rachel","sharma",60000)
    #     print("SetUp")
    #     return super().setUp()

    # def tearDown(self):
    #     self.emp1 =  None
    #     self.emp2 = None
    #     print("TearDown")
    #     return super().tearDown()

    @classmethod
    def setUpClass(cls) -> None:
        cls.emp1 = Employee_Unit.Employee_Unit("coronary","schafer",50000)
        cls.emp2 = Employee_Unit.Employee_Unit("rachel","sharma",60000)
        print("Inside SetUp")
        return super().setUpClass()
    
    @classmethod
    def tearDownClass(cls) -> None:
        cls.emp1 = None
        cls.emp2 = None
        print("Outside SetUp")
        return super().tearDownClass()
    
    def test_email(self):
        print("Email")
        emp1 = self.emp1
        self.assertEqual(emp1.email,'coronary.schafer@gmail.com')
        emp1.first = "John"
        emp1.last = "toronto"
        self.assertEqual(emp1.email,'John.toronto@gmail.com')
    
    def test_fullname(self):
        print("Test Fullname")
        print(self.emp1.full_name)

    def test_monthly_schedule(self):
        with patch('Employee_Unit.requests.get') as mock_get:
            mock_get.return_value.ok = True
            mock_get.return_value.text = "Success"
            sh = self.emp1.monthly_schedule(33)
            print("Monthly = ",sh)
            mock_get.assert_called_with('https://google.com/?q=facebook')
            self.assertEqual(sh,"Success")

            mock_get.return_value.ok = False
            sh = self.emp2.monthly_schedule(33)
            print("Monthly = ",sh)
            mock_get.assert_called_with('https://google.com/?q=facebook')
            self.assertEqual(sh,"Bad Response")
if __name__ == '__main__':
    unittest.main()