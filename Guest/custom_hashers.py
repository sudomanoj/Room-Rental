import hashlib
from django.contrib.auth.hashers import BasePasswordHasher, mask_hash

class SHA256PasswordHasher(BasePasswordHasher):
    """
    A password hashing class that uses SHA-256 algorithm.
    """

    algorithm = 'sha256'

    def encode(self, password, salt):
        assert password is not None
        assert salt and '$' not in salt
        hash_pw = hashlib.sha256((salt + password).encode('utf-8')).hexdigest()
        return '%s$%s' % (self.algorithm, hash_pw)

    def verify(self, password, encoded):
        algorithm, hash_pw = encoded.split('$', 1)
        encoded_2 = self.encode(password, '')
        return hashlib.sha256((password).encode('utf-8')).hexdigest() == hash_pw

    def safe_summary(self, encoded):
        algorithm, hash_pw = encoded.split('$', 1)
        assert algorithm == self.algorithm
        return {
            'algorithm': algorithm,
            'hash': mask_hash(hash_pw),
        }