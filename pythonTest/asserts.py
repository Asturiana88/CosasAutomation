import unittest
import platform

class PruebasStandars(unittest.TestCase):

    @classmethod
    def setUpClass(cls): # Esto es como un Before
        print("Esto se va a ejecutar 1 vez, al inicio, antes que los test cases")


    def setUp(self): # Es como un beforeEach, se corre al inicio x cada testCase
        print("Hago algo antes de cada testCase")


    @unittest.skip("No se ejecuta ya que hay cambios en curso") # Caso skippado, no se ejecuta
    def test_suma(self):
        a = 2+2
        b = 3+1
        self.assertEqual(a,b)
    @unittest.skipIf(platform.system() == 'Windows', 'No se ejecuta en windows')
    def test_otra_suma(self):
        a = 5+1
        b = 8+20
        self.assertNotEqual(a,b)

    @unittest.skipUnless(platform.system() == 'Windows', 'Solo se ejecuta en windows')
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
    
    def test_algo_es_none(self):
       a = 2
       b = 6
       # self.assertTrue(a>b)
       self.assertIsNone(a+b)

    def test_algo_no_es_none(self):
       a = 2
       b = 6
       # self.assertTrue(a>=b)
       self.assertIsNotNone(a+b)

    def test_algo_es(self):
       a = 2
       b = 6
       # self.assertTrue(a>=b)
       self.assertIs(a,b)

    def test_algo_no_es(self):
       a = 2
       b = 6
       # self.assertTrue(a>=b)
       self.assertIsNot(a,b)    

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

    def test_algo_en(self):
      a = "Hola mundo"
      b = "Hola"
      # self.assertTrue(a<b)
      self.assertIn(a,b, "El texto no esta incluido")

    def test_algo_no_en(self):
      a = "Hola mundo"
      b = "Hola"
      # self.assertTrue(a<=b)
      self.assertNotIn(a,b, "El texto esta incluido")

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

    def tearDown(self): # Es como un afterEach, se ejecuta al finalizar cada TestCase
        print("Cosas que se van a hacer al final de cada testCase")

    @classmethod
    def tearDownClass(cls):
        print("Esto se ejecuta 1 vez, al final de todos los Test Cases")

# if __name__ == "__main__":
#     unittest.main()

# Se corre en consola (parado en el path del archivo) con:
# python -m unittest asserts.py
# Para mas informacion de cada test:
# python -m unittest asserts.py --verbose  or python -m unittest asserts.py -v
# modo silencioso, sin info de mas:
# python -m unittest asserts.py --quiet  or -q