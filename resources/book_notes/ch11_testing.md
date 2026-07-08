# Chapter 11: Testing Your Code

## Key Concepts

### Testing Functions
Python provides the `unittest` module in the standard library to help you write tests for your code. A **unit test** verifies that one specific aspect of a function's behavior is correct. A **test case** is a collection of unit tests that together prove a function behaves as expected.

Let's assume we have a function in `name_function.py`:
```python
def get_formatted_name(first, last):
    full_name = f"{first} {last}"
    return full_name.title()
```

Here is a test case in `test_name_function.py`:
```python
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    
    def test_first_last_name(self):
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

if __name__ == '__main__':
    unittest.main()
```

- **Inheriting `unittest.TestCase`**: The test case class must inherit from `unittest.TestCase`.
- **Method Names**: Any method that starts with `test_` will be run automatically by the test runner.
- **`self.assertEqual()`**: An assertion method to check if the result matches the expected value.

### Common Assertion Methods
`unittest` provides many assertion methods to verify conditions:
- `assertEqual(a, b)` — Check if `a == b`
- `assertNotEqual(a, b)` — Check if `a != b`
- `assertTrue(x)` — Check if `x` is True
- `assertFalse(x)` — Check if `x` is False
- `assertIn(item, list)` — Check if `item` is in `list`
- `assertNotIn(item, list)` — Check if `item` is not in `list`
- `assertRaises(Error)` — Verify that a block raises a specific exception

### Testing Classes
Testing classes is similar to testing functions — you write test cases to verify the behavior of class methods.

Assume we have a class `AnonymousSurvey` in `survey.py`:
```python
class AnonymousSurvey:
    def __init__(self, question):
        self.question = question
        self.responses = []
        
    def show_question(self):
        print(self.question)
        
    def store_response(self, new_response):
        self.responses.append(new_response)
```

Here is the test case:
```python
import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""
    
    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        my_survey.store_response('English')
        self.assertIn('English', my_survey.responses)
```

### The `setUp()` Method
If you create the same objects inside every test method, you can use the `setUp()` method. Python runs `setUp()` before running each test method. Objects created in `setUp()` are stored as instance attributes, making them available in all test methods.

```python
class TestAnonymousSurvey(unittest.TestCase):
    def setUp(self):
        """Create a survey and a set of responses for use in all test methods."""
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
        
    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
        
    def test_store_three_responses(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)
```

## Common Pitfalls
- **Forgetting `test_` Prefix**: Test methods that do not start with `test_` will not be executed.
- **Leaking State**: Forgetting that test methods should run independently. Avoid using global variables or persistent file modifications across tests without proper cleanup.
- **Overcomplicating Unit Tests**: Writing unit tests that check too many things at once. Keep tests focused and simple.

## Try It Yourself
1. Write a function that accepts a city and country and returns a single formatted string like `Santiago, Chile`. Write a test case class with a method `test_city_country()` to verify it works.
2. Add a third optional parameter to your function (e.g. population) and write a second test `test_city_country_population()` to verify it.
3. Write a test class for an `Employee` class that initializes with first name, last name, and annual salary. Include a method `give_raise()` and verify both default raises ($5000) and custom raises.
