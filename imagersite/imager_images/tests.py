"""Tests for imager_images app."""

from django.test import TestCase
from django.db import models
from django.test import SimpleTestCase
from django.test.utils import isolate_apps


# Create your tests here.
#  -- example test ---
@isolate_apps('app_label', attr_name='apps')
class TestModelDefinition(SimpleTestCase):
    """."""

    def test_model_definition(self):
        """."""
        class TestModel(models.Model):
            pass
        self.assertIs(self.apps.get_model('app_label', 'TestModel'), TestModel)
