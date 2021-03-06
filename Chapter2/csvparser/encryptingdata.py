import hashlib


password = "Devilkillsyou"

bytesecret = password.encode('utf8')

m = hashlib.md5()

m.update(bytesecret)

m.digest()
