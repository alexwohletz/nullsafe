"""Tests for the nullsafe package."""

import unittest
from nullsafe import ns, NullSafe

class TestNullSafe(unittest.TestCase):
    def test_basic_value_access(self):
        # Test direct value access
        self.assertEqual(ns(42)(), 42)
        self.assertIsNone(ns(None)())

    def test_attribute_access(self):
        # Test attribute access on objects
        class Person:
            def __init__(self):
                self.name = "John"
                self.age = 30

        person = Person()
        self.assertEqual(ns(person).name(), "John")
        self.assertEqual(ns(person).age(), 30)
        self.assertIsNone(ns(person).unknown_attr())
        self.assertIsNone(ns(None).any_attr())

    def test_item_access(self):
        # Test dictionary access
        data = {"name": "John", "age": 30}
        self.assertEqual(ns(data)["name"](), "John")
        self.assertEqual(ns(data)["age"](), 30)
        self.assertIsNone(ns(data)["unknown_key"]())
        self.assertIsNone(ns(None)["any_key"]())

        # Test list access
        lst = [1, 2, 3]
        self.assertEqual(ns(lst)[0](), 1)
        self.assertIsNone(ns(lst)[10]())
        self.assertIsNone(ns(None)[0]())

    def test_chaining(self):
        # Test chaining of attribute and item access
        data = {
            "user": {
                "profile": {
                    "address": {
                        "city": "New York"
                    }
                }
            }
        }
        self.assertEqual(
            ns(data)["user"]["profile"]["address"]["city"](),
            "New York"
        )
        self.assertIsNone(
            ns(data)["user"]["profile"]["nonexistent"]["field"]()
        )

    def test_nested_none(self):
        # Test handling of None in nested structures
        data = {
            "user": None
        }
        self.assertIsNone(ns(data)["user"]["any"]["path"]())

    def test_immutability(self):
        # Test that NullSafe objects are immutable
        wrapper = ns(42)
        with self.assertRaises(AttributeError):
            wrapper.new_attr = "value"

    def test_repr(self):
        # Test string representation
        self.assertEqual(repr(ns(42)), "NullSafe(42)")
        self.assertEqual(repr(ns(None)), "NullSafe(None)")
        self.assertEqual(repr(ns("test")), "NullSafe('test')")

if __name__ == '__main__':
    unittest.main()
