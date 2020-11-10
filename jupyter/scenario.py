# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class Scenario(KaitaiStruct):
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.chapters = []
        i = 0
        while not self._io.is_eof():
            self.chapters.append(self._root.Chapter(self._io, self, self._root))
            i += 1


    class Head(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.zero = self._io.read_u2le()
            self.year = self._io.read_u2le()
            self.mon = self._io.read_u1()
            self.num_rulers = self._io.read_u1()
            self.ruler_colors = self._io.read_bytes(16)


    class Chapter(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.head = self._root.Head(self._io, self, self._root)
            self.generals = [None] * (255)
            for i in range(255):
                self.generals[i] = self._root.General(self._io, self, self._root)

            self.special = self._root.Special(self._io, self, self._root)
            self.rulers = [None] * (16)
            for i in range(16):
                self.rulers[i] = self._root.Ruler(self._io, self, self._root)

            self.provinces = [None] * (41)
            for i in range(41):
                self.provinces[i] = self._root.Province(self._io, self, self._root)

            self.tail = self._io.read_bytes(146)


    class Ruler(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.general = self._io.read_u2le()
            self.capital = self._io.read_u2le()
            self.advisor = self._io.read_u2le()
            self.trust = self._io.read_u2le()
            self.unknown1 = self._io.read_u1()
            self.unknown2 = self._io.read_u1()
            self.ally = self._io.read_u2le()
            self.unknown4 = self._io.read_u2le()
            self.hostilities = self._io.read_bytes(16)
            self.joint_invasion_ally = self._io.read_u1()
            self.join_invasion_target = self._io.read_u1()
            self.target_province_faction_owner = self._io.read_u1()
            self.marriage = self._io.read_u1()
            self.exile = self._io.read_u1()
            self.unknown5 = self._io.read_bytes(6)


    class General(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.gnid = self._io.read_u2le()
            self.unknown1 = self._io.read_u2le()
            self.intelligence = self._io.read_u1()
            self.war_ability = self._io.read_u1()
            self.charm = self._io.read_u1()
            self.lawfulness = self._io.read_u1()
            self.virtue = self._io.read_u1()
            self.ambition = self._io.read_u1()
            self.faction = self._io.read_u1()
            self.loyalty = self._io.read_u1()
            self.service = self._io.read_u1()
            self.hidden = self._io.read_u1()
            self.unknown2 = self._io.read_u1()
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


    class Province(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.next = self._io.read_u2le()
            self.governor = self._io.read_u2le()
            self.unknown1 = self._io.read_u2le()
            self.freegen1 = self._io.read_u2le()
            self.gold = self._io.read_u2le()
            self.food = self._io.read_u4le()
            self.pop = self._io.read_u2le()
            self.faction = self._io.read_u1()
            self.unknown2 = self._io.read_bytes(5)
            self.land_dev = self._io.read_u1()
            self.pop_loyalty = self._io.read_u1()
            self.flood_dev = self._io.read_u1()
            self.num_horses = self._io.read_u1()
            self.num_forts = self._io.read_u1()
            self.unknown3 = self._io.read_bytes(4)
            self.region1 = self._io.read_u1()
            self.region2 = self._io.read_u1()
            self.region3 = self._io.read_u1()
            self.region4 = self._io.read_u1()


    class Special(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            self.unknown1 = self._io.read_u1()
            self.empty_slot = self._io.read_u2le()
            self.sima_hui = self._io.read_u1()
            self.xu_zijiang = self._io.read_u1()
            self.hua_tuo = self._io.read_u1()
            self.unknown2 = self._io.read_u1()



