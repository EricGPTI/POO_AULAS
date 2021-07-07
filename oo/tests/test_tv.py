from unittest import TestCase
from oo.tv import TV
from oo.controle import Controle

class TesteTv(TestCase):
    def test_status_inicial_tv_0(self):
        controle = Controle()
        tv = TV(controle)
        self.assertEqual(tv.status, 0)

    def test_status_tv_ligada_1(self):
        controle = Controle()
        tv = TV(controle)
        tv.ligar()
        status = tv.proximo_canal()
        self.assertEqual(status, 1)