# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class Taiki(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.head = self._root.Head(self._io, self, self._root)
        self.generals = []
        i = 0
        while not self._io.is_eof():
            self.generals.append(self._root.General(self._io, self, self._root))
            i += 1


    class Head(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.num_generals = self._io.read_bytes(6)


    class General(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.debut = self._io.read_u1()
            self.auto_join = self._io.read_u1()
            self.home = self._io.read_u1()
            self.unknown1 = self._io.read_bytes(4)
            self.intelligence = self._io.read_u1()
            self.war_ability = self._io.read_u1()
            self.charm = self._io.read_u1()
            self.lawfulness = self._io.read_u1()
            self.virtue = self._io.read_u1()
            self.ambition = self._io.read_u1()
            self.belong = self._io.read_u1()
            self.loyalty = self._io.read_u1()
            self.service = self._io.read_u1()
            self.hidden = self._io.read_bytes(1)
            self.unknown2 = self._io.read_bytes(1)
            self.alignment = self._io.read_u1()
            self.lineage = self._io.read_u2le()
            self.men = self._io.read_u2le()
            self.weapon = self._io.read_u2le()
            self.training = self._io.read_u1()
            self.pos_in_war = self._io.read_u2le()
            self.birth = self._io.read_u1()
            self.portrait1 = self._io.read_u1()
            self.portrait2 = self._io.read_u1()
            self.name = (self._io.read_bytes(15)).decode(u"ascii")



