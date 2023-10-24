from django.test import TestCase

# Create your tests here.

from django.core.exceptions import ValidationError
from .models import Thing

class ThingModelTest(TestCase):
    def test_name_max_length(self):
        # Test that the name field has a maximum length of 20 characters.
        thing = Thing(name="A" * 21, description="Valid description", quantity=50)
        with self.assertRaises(ValidationError):
            thing.full_clean()

    def test_name_unique(self):
        # Test that the name field is unique.
        thing1 = Thing(name="DuplicateName", description="Valid description", quantity=50)
        thing1.save()
        thing2 = Thing(name="DuplicateName", description="Another description", quantity=75)
        with self.assertRaises(ValidationError):
            thing2.full_clean()

    def test_description_max_length(self):
        # Test that the description field has a maximum length of 120 characters.
        thing = Thing(name="ValidName", description="B" * 121, quantity=50)
        with self.assertRaises(ValidationError):
            thing.full_clean()

    def test_quantity_min_max_values(self):
        # Test that the quantity field has minimum and maximum value constraints.
        # Valid value: 50
        valid_thing = Thing(name="ValidName", description="Valid description", quantity=50)
        valid_thing.full_clean()  # Should not raise an exception

        # Invalid values: less than 0, more than 100
        invalid_thing1 = Thing(name="InvalidName1", description="Invalid description", quantity=-1)
        invalid_thing2 = Thing(name="InvalidName2", description="Invalid description", quantity=101)
        with self.assertRaises(ValidationError):
            invalid_thing1.full_clean()
            invalid_thing2.full_clean()
            
    
