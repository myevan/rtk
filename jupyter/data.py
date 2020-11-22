import inspect

class PrimitiveError(Exception):
    def __init__(self, name, value, memo):
        Exception.__init__(self, name)
        self.__name = name
        self.__value = value
        self.__memo = memo

    def __str__(self):
        return f"{self.__name}({self.__memo})"

    @property
    def value(self):
        return self.__value

    @property
    def memo(self):
        return self.__memo

class Primitive:
    __seq = 0

    @classmethod
    def alloc_sequence(cls):
        cls.__seq += 1
        return cls.__seq

    def __init__(self, builtin_code=None, builtin_value=None, count=None, pk=False, fk=None, default=None, name=None, code=None):
        self.__seq = Primitive.alloc_sequence() if builtin_code else 0
        self.__count = count
        self.__pk = pk
        self.__fk = fk
        self.__code = code
        self.__code = builtin_code if code is None else code
        self.__value = builtin_value if default is None else default
        self.__name = name
        self.__model_cls = None

    def __repr__(self):
        def gen_attrs():
            if self.__count:
                yield str(self.__count)
            if self.__pk:
                yield 'pk=True'

        attrs = ', '.join(gen_attrs())
        if self.__model_cls:
            return f"{self.__class__.__name__}<{self.__model_cls.__name__}.{self.__name}>({attrs})"
        else:
            return f"{self.__class__.__name__}({attrs})"

    def bind(self, model_cls, name):
        self.__model_cls = model_cls
        self.__name = name

    def convert(self, value):
        return value

    @property
    def seq(self):
        return self.__seq

    @property
    def name(self):
        return self.__name

    @property
    def count(self):
        return self.__count

    @property
    def code(self):
        return self.__code

    @property
    def default_value(self):
        return self.__value

    @property
    def key_name(self):
        assert(self.__model_cls)
        return f"({self.__model_cls.__name__}.{self.__name})"

    @property
    def binding(self):
        return self.__model_cls

    @property
    def foreign_key(self):
        return self.__fk

    @property
    def is_primary_key(self):
        return self.__pk

class DeclMeta(type):
    def __new__(meta, name, bases, attrs):
        new_cls = type.__new__(meta, name, bases, attrs)

        field_pairs = inspect.getmembers(new_cls, lambda m:isinstance(m, Primitive))
        for field_name, field_type in field_pairs:
            field_type.bind(new_cls, field_name)

        if field_pairs:
            field_pairs.sort(key=lambda x: x[1].seq)
            new_cls._field_names, new_cls._field_types = list(zip(*field_pairs))
        else:
            new_cls._field_names = []
            new_cls._field_types = []

        new_cls._pk_names = [field_type.name for field_type in new_cls._field_types if field_type.is_primary_key]

        return new_cls

class Model(metaclass=DeclMeta):
    _records = None
    _pk_records = None
    __default_record = None
    __repr_limit = 3

    @classmethod
    def get_field_names(cls):
        return cls._field_names

    @classmethod
    def get_field_types(cls):
        return cls._field_types

    @classmethod
    def get_primary_key_names(cls):
        return cls._pk_names

    @classmethod
    def load_datas(cls, datas):
        cls.__records = [cls(*data) for data in datas]
        if cls.get_primary_key_names():
            cls._pk_records = dict((record.get_primary_key_values(), record) for record in cls._records)

    @classmethod
    def get(cls, pk, default=None):
        assert(cls._pk_records)
        return cls._pk_records.get(pk, default if default else cls.__default_record)
    
    @classmethod
    def put(cls, record):
        pk = record.get_primary_key_values()

        if not cls._pk_records:
            cls._pk_records = dict()

        cls._pk_records[pk] = record

        if not pk in cls._pk_records:
            if not cls._records:
                cls._records = list()

            cls._records.append(record)

    @classmethod
    def set_default(cls, record):
        cls.__default_record = record

    def __init__(self, *args, **kwargs):
        for name, value in zip(self.get_field_names(), args):
            setattr(self, name, value)

        for field_type in self.get_field_types()[len(args):]:
            setattr(self, field_type.name, kwargs.get(field_type.name, field_type.default_value))

    def __repr__(self):
        info = ' '.join(f'{key}={value}' for key, value in self.gen_field_pairs(limit=self.__repr_limit))
        return f"{self.__class__.__name__}({info})"

    def gen_field_pairs(self, limit=None):
        names = self.get_field_names() if limit is None else self.get_field_names()[:limit]
        for name in names:
            value = getattr(self, name)
            if type(value) is str:
                yield (name, f'"{value}"')
            else:
                yield (name, value)

    def get_primary_key_values(self):
        pk_names = self.get_primary_key_names()
        assert(pk_names)
        if len(pk_names) == 1:
            return getattr(self, pk_names[0])
        else:
            return tuple(getattr(self, name) for name in pk_names)

class Integer(Primitive):
    def __init__(self, *args, **kwargs):
        Primitive.__init__(self, 'i', 0, *args, **kwargs)
        self.min = -0x800000000000000
        self.max = +0x7FFFFFFFFFFFFFF

    def convert(self, value):
        ret_value = int(value)
        if ret_value < self.min: raise PrimitiveError('UNDERFLOW', ret_value, f"{ret_value} < {self.min}")
        if ret_value > self.max: raise PrimitiveError('OVERFLOW', ret_value, f"{ret_value} > {self.max}")
        return ret_value

class Int8(Integer):
    def __init__(self, *args, **kwargs):
        Primitive.__init__(self, 'i', 0, *args, **kwargs)
        self.min = -0x80
        self.max = +0x7F

class Float(Primitive):
    def __init__(self, *args, **kwargs):
        Primitive.__init__(self, 'f', 0.0, *args, **kwargs)

    def convert(self, value):
        return float(value)
    
class String(Primitive):
    def __init__(self, *args, **kwargs):
        Primitive.__init__(self, 's', "", *args, **kwargs)

    def convert(self, value):
        return str(value)

class Position(Primitive):
    def __init__(self, *args, **kwargs):
        Primitive.__init__(self, 'p', (0, 0, 0), *args, **kwargs)

class Rotation(Primitive):
    def __init__(self, *args, **kwargs):
        Primitive.__init__(self, 'd', 0, *args, **kwargs) # 0: x+

class Text:
    def __init__(self, value):
        self.__value = value

    def __str__(self):
        return self.__value

class Table:
    def __init__(self, field_names, records):
        self.field_names = field_names
        self.records = records

if __name__ == '__main__':
    class User(Model):
        id = Integer(pk=True)
        name = String()
        lv = Int8()

    class Profile(Model):
        id = Integer(pk=True)
        user_id = Integer(fk=User.id)

    print(User.id)
    user = User(id=1, name="a")
    print(user)
    print(Profile.user_id.foreign_key)
    User.lv.convert(300)
