import pytest
from milestone2 import CryptSecure

@pytest.fixture
def crypt_secure_instance():
    return CryptSecure()

def test_register_user(crypt_secure_instance):
    # Successful registration
    crypt_secure_instance.register_user("user1", "password1")
    
    # Verify that the password can be successfully verified
    assert crypt_secure_instance.verify_password("password1", crypt_secure_instance.user_database["user1"])
