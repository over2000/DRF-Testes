from django.test import TestCase
from aluraflix.models import Programa

class ProgramaModelTestCase(TestCase):

    def setUp(self):
        self.programa = Programa(
            titulo = 'Teste Filme',
            data_lancamento = '2003-06-04'
        )
        
    def test_verify_model_fields(self):
        self.assertEqual(self.programa.titulo, 'Teste Filme')
        self.assertEqual(self.programa.tipo, 'F')
        self.assertEqual(self.programa.data_lancamento, '2003-06-04')
        self.assertEqual(self.programa.likes, 0)
        self.assertEqual(self.programa.dislikes, 0)