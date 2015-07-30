from django.test import TestCase
from apps.core.models import Candidate

class CandidateTestCase(TestCase):
    def setUp(self):
        Candidate.objects.create(name="joao", email="teste@teste.com", html=1, css=10, javascript=1, python=10,
                                 django=1, ios=10, android=1)
        Candidate.objects.create(name="maria", email="exemplo@teste.com", html=10, css=10, javascript=10, python=10,
                                 django=10, ios=10, android=10)

    def test_candidate_front(self):
        joao = Candidate.objects.get(name="joao")
        maria = Candidate.objects.get(name="maria")
        self.assertEqual(joao.is_front(), False)
        self.assertEqual(joao.is_back(), False)
        self.assertEqual(joao.is_mobile(), False)
        self.assertEqual(maria.is_front(), True)
        self.assertEqual(maria.is_back(), True)
        self.assertEqual(maria.is_mobile(), True)