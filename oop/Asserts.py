import unittest

class PruebasStandars(unittest.TestCase):
    def test_suma(self):
        a = 2+2
        b = 3+1
        self.assertEqual(a,b)

    def test_otra_suma(self):
        a = 5+1
        b = 8+20
        self.assertNotEqual(a,b)

    def test_algo_verdadero(self):
        a = 2+2
        b = 3+1
        self.assertTrue(a==b, "a y b deberian ser iguales")

    def test_algo_mas_verdadero(self):
        self.assertTrue(True)

    def test_algo_falso(self):
        self.assertFalse(2+1 == 3+4, "Esto deberia ser falso")

    def test_algo_mayor(self):
        a = 2
        b = 6
        # self.assertTrue(a>b)
        self.assertGreater(b,a)

    def test_algo_mayor_Igual(self):
       a = 2
       b = 6
       # self.assertTrue(a>=b)
       self.assertGreaterEqual(b,a)
    
    def test_algo_menor(self):
      a = 2
      b = 6
      # self.assertTrue(a<b)
      self.assertLess(a,b)

    def test_algo_menor_igual(self):
      a = 2
      b = 6
      # self.assertTrue(a<=b)
      self.assertLessEqual(a,b)

    def test_listar(self):
        a=[1,2,"fruta"]
        b=[1,2,"fruta"]
        self.assertListEqual(a,b)
    
    def test_comparar_tuplas(self):
        a=(1,2,3)
        b=(1,2,3)
        self.assertTupleEqual(a,b)

    def test_comparar_diccionarios(self):
        a = {"id":2, "nombre":"pepe", "apellido": "suarez"}
        b = {"id":2, "nombre":"pepe", "apellido": "suarez"}
        self.assertDictEqual(a,b)

if __name__ == "__main__":
    unittest.main()