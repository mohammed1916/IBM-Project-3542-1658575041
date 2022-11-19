from locust import HttpUser, task, between
import os


def getImg(filePath):
      _fileName = os.path.basename(filePath)
      _fileContent = open(filePath,'rb')
      return _fileName, _fileContent, 'file'

_files= {
    "Images":getImg("../Test Images/2.jpeg"),
    "Images":getImg("../Test Images/3.jpeg"),
}
headers = {'content-type': 'multipart/form-data'}

class PerformanceTest(HttpUser):

    @task
    def home(self):
        r = self.client.post("", files=_files, headers = headers)
        print(r)