from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
suz = "sobir12423ri2j3r495jt3o4"
print(suz)

sss = urlsafe_base64_encode(force_bytes(suz))
# zzz = urlsafe_base64_encode(force_bytes(suz))
print(sss)


asli = urlsafe_base64_decode(sss).decode()

print(asli)

