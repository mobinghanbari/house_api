from passlib.context import CryptContext

pwd_ctx = CryptContext(schemes="bcrypt")

class Hash:
    @staticmethod
    def bcrypt(password):
        return pwd_ctx.hash(password)

    @staticmethod
    def verify(password, plain_password):
        return pwd_ctx.verify(plain_password, password)
