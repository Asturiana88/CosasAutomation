import unittest
import requests

req = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print("Status: ")
print(req.status_code)
print(req.content)

req = requests.post(url='https://jsonplaceholder.typicode.com/posts', json={'title':'prueba', 'body':'lorem ipsum', 'userId': 1})
print("Status: ")
print(req.text)
print(req.status_code)
# te crea un file con el error
#with open("asd.html", 'w') as file:
#    file.write(req.text)   

req = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print("Status: ")
print(req.status_code)

class ApiTest(unittest.TestCase):

    def test_put_OK(self):
        req = requests.put('https://jsonplaceholder.typicode.com/posts/1', {'title':'prueba New', 'body':'lorem ipsum New', 'userId': 1})
        print(req.status_code)
        self.assertEqual(req.status_code,201)
        

    def test_patch_OK_modif_title(self): 
        req = requests.patch('https://jsonplaceholder.typicode.com/posts/1', {'title':'pruebaaaaaaaa'})
        print(req.status_code)
        self.assertEqual(req.status_code,201)

if __name__ == "__main__":
    unittest.main()



 