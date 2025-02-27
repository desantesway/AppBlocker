from cryptography.fernet import Fernet
import base64

def get_code():
    cipher_suite = Fernet(base64.urlsafe_b64encode(b"qqvAnMd45bfMf1MOtetQvdAdzrgO1efG"))
    return cipher_suite.decrypt(b'gAAAAABnnNKeOBR_lFoE5RVK90T07CLkbsk1VCxGV6mcOoyo9THlUqAbvowIj1rwjXG2cV4lGIvAGNEZWnHYATedfZfbL_kgS0ZcmTuqsPXOMlWkL4EFEDly1Pk49UGVADhY6zeHvxFc').decode()