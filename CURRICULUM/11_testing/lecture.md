# Lecture 11: Testing

Testing is the process of verifying that your code performs as expected under different conditions. Python's standard library includes the `unittest` module to facilitate unit testing.

---

## 1. Why Test Code?
- **Prevents regressions**: Ensures new changes don't break existing functionality.
- **Validates assumptions**: Confirms the code handles edge cases, bad inputs, and normal cases correctly.
- **Improves design**: Writing tests forces you to design modular, clean functions.

---

## 2. Writing a Simple Unit Test
A unit test verifies that a single, specific aspect of a function's behavior is correct.

Let's say you have a function in `name_formatter.py`:
```python
# name_formatter.py
def get_formatted_name(first, last):
    return f"{first} {last}".title()
```

You can write a test case for this function by inheriting from `unittest.TestCase`:
```python
# test_name_formatter.py
import unittest
from name_formatter import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_formatter.py'."""
    
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()
```

- **Running the Test**: Run the test script directly: `python test_name_formatter.py`.
- **Test Methods**: All methods in a test case starting with `test_` will be run automatically.

---

## 3. Common Assertion Methods
Assertions verify that a condition evaluates to the expected result.

| Assertion Method | Checks |
|------------------|--------|
| `self.assertEqual(a, b)` | `a == b` |
| `self.assertNotEqual(a, b)` | `a != b` |
| `self.assertTrue(x)` | `x is True` |
| `self.assertFalse(x)` | `x is False` |
| `self.assertIn(item, list)` | `item in list` |
| `self.assertNotIn(item, list)` | `item not in list` |
| `self.assertRaises(Error)` | Code raises `Error` |

---

## 4. The `setUp()` Method
When testing a class, you often create the same instances and resources in every test. The `setUp()` method runs **before each test method**, allowing you to create resources once and access them as instance variables.

```python
class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        """Create survey and responses once for all tests."""
        self.survey = AnonymousSurvey("What is your favorite language?")
        self.responses = ['Python', 'Go', 'JS']

    def test_single_response(self):
        self.survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.survey.responses)
```

---

## 🧠 Try It Yourself
1. Write a function that accepts city and country, returning a formatted string. Write a test case using `unittest` to test it.
2. Introduce a bug deliberately in the function (e.g., skip capitalizing the name) and run the test suite to observe the failure.
