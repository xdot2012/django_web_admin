from django.test import TestCase
from legacy.models import Sale
from legacy.tasks import task_read

# Create your tests here.
class SalesTestCase(TestCase):
    def setUp(self):
        df = task_read(10)
        Sale.create_from_dataframe(df)
        
    def test_task(self):
        pass