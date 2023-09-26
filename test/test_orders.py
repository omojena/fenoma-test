import unittest

from fastapi import HTTPException

from services.orders import solution_orders


class SolutionOrdersTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_total_revenue(self):
        orders = [
            {"status": "completed", "price": 10, "quantity": 2},
            {"status": "pending", "price": 5, "quantity": 3},
            {"status": "completed", "price": 8, "quantity": 1}
        ]
        criterion = "completed"
        expected_result = {"total_revenue": 28}

        result = solution_orders(orders, criterion)
        self.assertEqual(result, expected_result)

    def test_invalid_orders(self):
        orders = [
            {"status": "completed", "price": -10, "quantity": 2},
            {"status": "pending", "price": 5, "quantity": 3},
            {"status": "completed", "price": 8, "quantity": -1}
        ]
        criterion = "completed"

        with self.assertRaises(HTTPException) as context:
            solution_orders(orders, criterion)

        self.assertEqual(context.exception.status_code, 400)
        self.assertEqual(context.exception.detail, "price and quantity invalid")


if __name__ == '__main__':
    unittest.main()
