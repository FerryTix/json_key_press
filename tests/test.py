from json_key_press import CompressibleObject, JSONKeyPress
import json


class OrderCategory(CompressibleObject):
    def compress(self, o):
        return {
            'apple': 'a',
            'peach': 'p',
            'cherry': 'c',
        }[o]

    def decompress(self, o):
        return {
            'a': 'apple',
            'p': 'peach',
            'c': 'cherry',
        }[o]


order = {
    "order_uuid": int,
    "category": OrderCategory,
    "amount": int,
}

test_schema = {
    "order": order,
    "amount": int,
    "customer_name": str,
}

test_long = {
    "order": {
        "order_uuid": "7234723467",
        "amount": 50,
        "category": "apple"
    },
    "amount": 10,
    "customer_name": "Harald",

}

if __name__ == '__main__':
    t = JSONKeyPress(schema=test_schema)
    sk = t._short_keyed
    lk = t._long_keyed
    assert "A" in sk
    assert "order" in lk
    compr = t.compress(test_long)
    decompr = t.decompress(compr)
    assert decompr == test_long
    la, lb = len(json.dumps(compr)), len(json.dumps(decompr))
    print(la, lb)
    print("Compression rate for example:", la / lb)
    print(json.dumps(compr, indent=4))
    print(json.dumps(decompr, indent=4))

    o = t(decompressed=test_long)
    assert o.get_compressed()["B"] == 10 == o.get_decompressed()["amount"]
