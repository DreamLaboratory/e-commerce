import os
from django.utils.deconstruct import deconstructible
from uuid import uuid4


@deconstructible
def PathAndRename(object):
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filname):
        ext = filname.split(".")[-1]
        filname = f"file_{instance.pk}_{str(uuid4().hex)[:4]}.{ext}"
        return os.path.join(self.path, filname)
