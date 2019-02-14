import flatconfig

import unittest


class TestAccessFlatKeys(unittest.TestCase):

    def setUp(self):
        self.flat_1 = flatconfig.FlatConfig()
        self.flat_1["single"] = "single"
        self.flat_1["double.first"] = 0
        # self.flat_1["double"]["second"] = 1  # Not implemented yet

    def test_single_1(self):
        self.assertEqual(
            "single",
            self.flat_1["single"]
        )

    def test_double_1(self):
        self.assertEqual(
            0,
            self.flat_1["double.first"]
        )

    # def test_double_2(self):
    #     self.assertEqual(
    #         1,
    #         self.flat_1["double.second"]
    #     )


class TestConstruct(unittest.TestCase):

    def setUp(self):
        self.a_conf = flatconfig.FlatConfig(
            {
                "a": {
                    "b": {
                        "c": 1
                    }
                }
            }
        )

    def test_from_3dict(self):
        self.assertEqual(
            1,
            self.a_conf["a.b.c"]
        )
