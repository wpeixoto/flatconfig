import flatten_dict
# from typing import Any, _VT, _KT


class FlatConfig(dict):

    @staticmethod
    def dot_reducer(k1, k2):
        if k1 is None:
            return k2
        else:
            return k1 + "." + k2

    def __init__(self, dict_like: dict = None) -> None:
        dd = {}
        if dict_like is not None:
            dd = flatten_dict.flatten(dict_like, reducer=FlatConfig.dot_reducer)
        super().__init__(dd)

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

