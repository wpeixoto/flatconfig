import flatten_dict
import requests
import requests.exceptions
# from typing import Any, _VT, _KT
import ruamel.yaml as yaml


class FlatKeysDict(dict):

    @staticmethod
    def dot_reducer(k1, k2):
        if k1 is None:
            return k2
        else:
            return k1 + "." + k2

    def __init__(self, dict_like: dict = None) -> None:
        dd = {}
        if dict_like is not None:
            dd = flatten_dict.flatten(dict_like, reducer=FlatKeysDict.dot_reducer)
        super().__init__(dd)

    @classmethod
    def from_yaml(cls, yaml_string):
        return cls(yaml.safe_load(yaml_string))

    @classmethod
    def from_file(cls, filename, fmt='yaml'):
        with open(filename, 'r') as f:
            yml_str = f.read()
        if fmt == 'yaml':
            o = cls.from_yaml(yml_str)
        else:
            raise ValueError("Format '{}' not recognized".format(fmt))
        return o

    # def __getitem__(self, k: _KT) -> _VT:
    #     try:
    #         item = super().__getitem__(k)
    #     except KeyError:
    #         for kk in self.keys():
    #             if str(kk).startswith(k)
    #     return item


# def __setattr__(self, name: str, value: Any) -> None:
    #     try:
    #         super().__setattr__(name, value)
    #     except KeyError:
    #         path = name.split(".")
    #         try:
    #             super().__setattr__(name, value)
    #

class FlatConfig(FlatKeysDict):

    def __init__(self, filename=None, url=None) -> None:
        dict_like = {}
        if filename is not None:
            dict_like = FlatKeysDict.from_file(filename)
        else:
            if url is not None:
                try:
                    r = requests.get(url)
                except ValueError:
                    pass
                else:
                    dict_like = FlatKeysDict.from_yaml(r.text)
        super().__init__(dict_like)


if __name__ == '__main__':
    pass
