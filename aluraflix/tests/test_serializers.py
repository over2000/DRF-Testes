from django.test import TestCase
from aluraflix.models import Programa
from aluraflix.serializers import ProgramaSerializer

class ProgramaSerializerTestCase(TestCase):

    def setUp(self):
        self.programa = Programa(
            titulo = 'Teste Filme',
            data_lancamento = '2003-06-04',
            tipo='F',
            likes=3333,
            dislikes=33
        )
        self.serializer = ProgramaSerializer(instance=self.programa)

    def test_verify_serializer_fields(self):
        """testando campos do serializer"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['titulo', 'tipo', 'data_lancamento', 'likes'] ))

    def test_verify_serializer_content_fields(self):
        """testando conteúdo dos campos do serializer"""
        data = self.serializer.data
        self.assertEqual(data['titulo'], self.programa.titulo)
        self.assertEqual(data['tipo'], self.programa.tipo)
        self.assertEqual(data['data_lancamento'], self.programa.data_lancamento)
        self.assertEqual(data['likes'], self.programa.likes)
    