import unittest


class ComputeTestClass(unittest.TestCase):
    def test_angle_v2(self):
        import compute
        import numpy as np
        print("각도계산테스트")
        TEST_DATA_A = np.array(([1,0],))
        TEST_DATA_B = np.array(([1,1],))
        self.assertEqual(compute.angle_v2(TEST_DATA_A,TEST_DATA_B), 45)

        TEST_DATA_A = np.array(([1,0],))
        TEST_DATA_B = np.array(([-1,0],))
        self.assertEqual(compute.angle_v2(TEST_DATA_A,TEST_DATA_B), 180)
        TEST_DATA_A = np.array(([0,1],))
        TEST_DATA_B = np.array(([1,0],))
        self.assertEqual(compute.angle_v2(TEST_DATA_A,TEST_DATA_B), -90)

class DataprocTestClass(unittest.TestCase):
    def test_angle_v2(self):
        import dataproc
        A=dataproc.ExampleData('test.xlsx',Dir="./")
        print("test xls 읽기테스트. row 개수:", A.df.shape[0])
        self.assertEqual(A.df.shape[0], 1)


if __name__ == '__main__':
    unittest.main()
