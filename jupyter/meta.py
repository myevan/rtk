class SingletonMeta(type):
    def __new__(meta, cls_name, bases, attrs):
        new_cls = type.__new__(meta, cls_name, bases, attrs)
        new_cls._inst = new_cls()
        return new_cls

class Singleton(metaclass=SingletonMeta):
    @classmethod
    def get(cls):
        return cls._inst
