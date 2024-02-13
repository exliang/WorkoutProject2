
# Emily Liang
# exliang@uci.edu
# 79453973

# key validation using private funcs
class InvalidKeyException(Exception):
    pass


class Key:
    def __key(self, key):  # return True if key is valid, else return false
        try:
            if type(int(key)) == int and int(key) > 0:
                return True
        except ValueError:
            raise InvalidKeyException("Invalid key.")
