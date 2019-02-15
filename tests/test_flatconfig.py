import flatconfig
import unittest


class TestFlatConfig(unittest.TestCase):

    def setUp(self):
        # self.a_conf = flatconfig.FlatConfig(url="file://localhost/./config01.yaml")
        self.a_conf = flatconfig.FlatConfig(filename="config01.yaml")

    def test_flat_config_1(self):
        self.assertDictEqual(
            {
                "section.key1": "value1",
                "section.key2": True
            },
            self.a_conf
        )


if __name__ == '__main__':
    pass
