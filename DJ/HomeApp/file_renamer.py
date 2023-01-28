import os
from uuid import uuid4
from django.utils.deconstruct import deconstructible

@deconstructible
class PathAndRename(object):
    def  __init__(self,sub_path):
        self.path = sub_path

    def __call__(self, instance,filename):
        ext = filename.split(".")[-1]
        filename = f"file_{instance}_{str(uuid4().hex)[:4]}.{ext}"
        return os.path.join(self.path,filename)


#https://www.youtube.com/watch?v=lR-OKnX7uOw
