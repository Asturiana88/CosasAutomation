import unittest
import requests


class ApiTest(unittest.TestCase):
    def test_verificar_mail_post(self):
        req = requests.get('https://jsonplaceholder.typicode.com/comments?postId=1')
        resultado = req.json()
        self.assertEqual('Eliseo@gardner.biz',resultado[0]['email'])
        #print(req.content.decode('utf-8'))
        #print(req.text)

if __name__ == "__main__":
    unittest.main()