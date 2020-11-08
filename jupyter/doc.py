from data import Model, Integer, String
from data import Text as T

class Hero(Model):
    id = Integer(pk=True)
    trust = Integer()
    men = Integer()
    name = String()
    province_id = Integer(fk=lambda: Province.id)

class Province(Model):
    id = Integer(pk=True)
    pop = Integer()
    gold = Integer()
    food = Integer()
    rate = Integer()
    horses = Integer()
    loy = Integer()
    land = Integer()
    flood = Integer()
    forts = Integer()
    ruler_id = Integer(fk=lambda: Hero.id)
    governor_id = Integer(fk=lambda: Hero.id)
    advisor_id = Integer(fk=lambda: Hero.id)
    name = String()

    @property
    def men(self):
        return 0

    @property
    def generals(self):
        return 0

    @property
    def free_gens(self):
        return 0

    @property
    def ruler(self):
        return Hero.get(self.ruler_id)
    
    @property
    def governor(self):
        return Hero.get(self.governor_id)
    
    @property
    def advisor(self):
        return Hero.get(self.advisor_id)

    @property
    def head(self):
        return "\n".join(self.gen_head_lines())

    @property
    def body(self):
        return "\n".join(self.gen_body_lines())
    
    def gen_head_lines(self):
        yield f"{self.id}. {self.name}"
        yield f"Ruler: {self.ruler.name}"
        yield f"Trust: {self.ruler.trust}"
        if self.governor_id:
            yield f"Governor: {self.governor.name}"
        if self.advisor_id:
            yield f"Advisor: {self.advisor.name}"

    def gen_body_lines(self):
        yield f"Pop: {self.pop} Gold: {self.gold} Loy: {self.loy}"
        yield f"Men: {self.men} Food: {self.gold} Land: {self.land}"
        yield f"Generals: {self.generals} Rate: {self.rate} Flood: {self.flood}"
        yield f"FreeGens: {self.free_gens} Horses: {self.horses} Forts: {self.forts}"

if __name__ == "__main__":
    Hero.set_default(Hero(id=0, name=T("무명")))   
    Hero.put(Hero(id=1, trust=50, name=T("공손찬")))
    Hero.put(Hero(id=2, trust=50, name=T("유비")))
    Hero.put(Hero(id=3, trust=50, name=T("원소")))
    Hero.put(Hero(id=4, trust=50, name=T("한복")))
    Hero.put(Hero(id=5, trust=50, name=T("공융")))
    Hero.put(Hero(id=6, trust=50, name=T("조조")))
    Hero.put(Hero(id=7, trust=50, name=T("동탁")))
    Hero.put(Hero(id=8, trust=50, name=T("마등")))
    Hero.put(Hero(id=9, trust=50, name=T("도겸")))
    Hero.put(Hero(id=10, trust=50, name=T("원술")))
    Hero.put(Hero(id=11, trust=50, name=T("유표")))
    Hero.put(Hero(id=12, trust=50, name=T("손견")))
    Hero.put(Hero(id=13, trust=50, name=T("왕랑")))
    Hero.put(Hero(id=14, trust=50, name=T("유엽")))
    Hero.put(Hero(id=15, trust=50, name=T("유언")))
    Province.put(Province(id=1, pop=65000, gold=100, food=2000, rate=50, horses=5, loy=5, lnad=10, flood=5, forts=1, ruler_id=0, governor_id=0, name=T("유주")))
    Province.put(Province(id=2, pop=70000, gold=100, food=2000, rate=50, horses=5, loy=5, lnad=10, flood=5, forts=2, ruler_id=0, governor_id=0, name=T("유주")))
    Province.put(Province(id=3, pop=100000, gold=672, food=41000, rate=58, horses=9, loy=35, lnad=58, flood=33, forts=2, ruler_id=1, governor_id=0, name=T("유주")))
    Province.put(Province(id=4, pop=100000, gold=2876, food=49275, rate=34, horses=10, loy=94, lnad=67, flood=82, forts=0, ruler_id=2, governor_id=0, name=T("병주")))
    Province.put(Province(id=5, pop=70000, gold=100, food=2000, rate=50, horses=5, loy=15, lnad=25, flood=0, forts=1, ruler_id=0, governor_id=0, name=T("유주")))
    Province.put(Province(id=6, pop=500000, gold=1000, food=70000, rate=44, horses=15, loy=50, lnad=50, flood=50, forts=3, ruler_id=3, governor_id=0, name=T("기주")))
    Province.put(Province(id=7, pop=120000, gold=438, food=44000, rate=57, horses=14, loy=92, lnad=67, flood=51, forts=3, ruler_id=4, governor_id=0, name=T("기주")))
    Province.put(Province(id=8, pop=80000, gold=634, food=34800, rate=50, horses=8, loy=99, lnad=70, flood=50, forts=2, ruler_id=5, governor_id=0, name=T("청주")))
    Province.put(Province(id=9, pop=333500, gold=835, food=55800, rate=41, horses=18, loy=95, lnad=77, flood=73, forts=2, ruler_id=6, governor_id=0, name=T("연주")))
    Province.put(Province(id=10, pop=800000, gold=533, food=74500, rate=58, horses=29, loy=45, lnad=68, flood=50, forts=6, ruler_id=7, governor_id=0, name=T("사주")))
    Province.put(Province(id=11, pop=450000, gold=237, food=19300, rate=70, horses=13, loy=55, lnad=45, flood=38, forts=3, ruler_id=7, governor_id=0, name=T("사주")))
    Province.put(Province(id=12, pop=250000, gold=265, food=30300, rate=57, horses=20, loy=47, lnad=45, flood=30, forts=4, ruler_id=7, governor_id=0, name=T("사주")))
    Province.put(Province(id=13, pop=240000, gold=100, food=2000, rate=50, horses=5, loy=25, lnad=20, flood=20, forts=3, ruler_id=0, governor_id=0, name=T("옹주")))
    Province.put(Province(id=14, pop=230000, gold=637, food=33300, rate=44, horses=29, loy=54, lnad=45, flood=40, forts=1, ruler_id=8, governor_id=0, name=T("량주")))
    Province.put(Province(id=15, pop=80000, gold=100, food=2000, rate=50, horses=20, loy=5, lnad=10, flood=5, forts=1, ruler_id=0, governor_id=0, name=T("량주")))
    Province.put(Province(id=16, pop=150000, gold=144, food=57400, rate=49, horses=12, loy=92, lnad=55, flood=32, forts=2, ruler_id=9, governor_id=0, name=T("서주")))
    Province.put(Province(id=17, pop=200000, gold=100, food=2000, rate=50, horses=10, loy=45, lnad=50, flood=20, forts=4, ruler_id=0, governor_id=0, name=T("예주")))
    Province.put(Province(id=18, pop=250000, gold=100, food=2000, rate=50, horses=10, loy=40, lnad=50, flood=10, forts=3, ruler_id=0, governor_id=0, name=T("예주")))
    Province.put(Province(id=19, pop=900000, gold=670, food=35800, rate=52, horses=17, loy=62, lnad=54, flood=42, forts=4, ruler_id=10, governor_id=0, name=T("형주")))
    Province.put(Province(id=20, pop=800000, gold=166, food=57100, rate=56, horses=26, loy=99, lnad=67, flood=48, forts=3, ruler_id=11, governor_id=0, name=T("형주")))
    Province.put(Province(id=21, pop=584500, gold=777, food=73700, rate=47, horses=18, loy=96, lnad=83, flood=82, forts=4, ruler_id=12, governor_id=0, name=T("형주")))
    Province.put(Province(id=22, pop=500000, gold=100, food=2000, rate=50, horses=15, loy=40, lnad=55, flood=10, forts=3, ruler_id=0, governor_id=0, name=T("형주")))
    Province.put(Province(id=23, pop=650000, gold=100, food=2000, rate=50, horses=10, loy=40, lnad=50, flood=5, forts=1, ruler_id=0, governor_id=0, name=T("형주")))
    Province.put(Province(id=24, pop=350000, gold=608, food=38000, rate=31, horses=10, loy=58, lnad=55, flood=30, forts=3, ruler_id=13, governor_id=0, name=T("양주")))
    Province.put(Province(id=25, pop=150000, gold=100, food=2000, rate=50, horses=5, loy=30, lnad=40, flood=10, forts=1, ruler_id=0, governor_id=0, name=T("양주")))
    Province.put(Province(id=26, pop=70000, gold=100, food=2000, rate=50, horses=5, loy=25, lnad=15, flood=5, forts=0, ruler_id=0, governor_id=0, name=T("양주")))
    Province.put(Province(id=27, pop=80000, gold=100, food=2000, rate=50, horses=5, loy=25, lnad=15, flood=5, forts=4, ruler_id=0, governor_id=0, name=T("양주")))
    Province.put(Province(id=28, pop=150000, gold=598, food=21400, rate=51, horses=10, loy=84, lnad=53, flood=23, forts=0, ruler_id=14, governor_id=0, name=T("양주")))
    Province.put(Province(id=29, pop=300000, gold=100, food=2000, rate=50, horses=5, loy=35, lnad=35, flood=5, forts=3, ruler_id=0, governor_id=0, name=T("익주")))
    Province.put(Province(id=30, pop=300000, gold=325, food=10590, rate=61, horses=15, loy=80, lnad=68, flood=35, forts=0, ruler_id=15, governor_id=0, name=T("익주")))
    Province.put(Province(id=31, pop=300000, gold=100, food=2000, rate=50, horses=5, loy=35, lnad=35, flood=5, forts=1, ruler_id=0, governor_id=0, name=T("익주")))
    Province.put(Province(id=32, pop=250000, gold=156, food=25950, rate=44, horses=15, loy=64, lnad=55, flood=32, forts=0, ruler_id=15, governor_id=0, name=T("익주")))
    Province.put(Province(id=33, pop=348500, gold=79, food=69360, rate=51, horses=15, loy=99, lnad=70, flood=33, forts=4, ruler_id=15, governor_id=0, name=T("익주")))
    Province.put(Province(id=34, pop=150000, gold=100, food=2000, rate=50, horses=5, loy=40, lnad=30, flood=5, forts=3, ruler_id=0, governor_id=0, name=T("익주")))
    Province.put(Province(id=35, pop=80000, gold=100, food=2000, rate=50, horses=5, loy=35, lnad=25, flood=5, forts=1, ruler_id=0, governor_id=0, name=T("익주")))
    Province.put(Province(id=36, pop=85000, gold=100, food=2000, rate=50, horses=5, loy=35, lnad=35, flood=5, forts=2, ruler_id=0, governor_id=0, name=T("익주")))
    Province.put(Province(id=37, pop=60000, gold=100, food=2000, rate=50, horses=0, loy=5, lnad=10, flood=5, forts=1, ruler_id=0, governor_id=0, name=T("교주")))
    Province.put(Province(id=38, pop=55000, gold=100, food=2000, rate=50, horses=0, loy=5, lnad=10, flood=0, forts=0, ruler_id=0, governor_id=0, name=T("교주")))
    Province.put(Province(id=39, pop=60000, gold=100, food=2000, rate=50, horses=0, loy=5, lnad=10, flood=0, forts=0, ruler_id=0, governor_id=0, name=T("교주")))
    Province.put(Province(id=40, pop=65000, gold=100, food=2000, rate=50, horses=5, loy=5, lnad=15, flood=5, forts=0, ruler_id=0, governor_id=0, name=T("교주")))
    Province.put(Province(id=41, pop=80000, gold=100, food=2000, rate=50, horses=0, loy=5, lnad=15, flood=5, forts=1, ruler_id=0, governor_id=0, name=T("교주")))
    print(Province.get(9).head)
    print(Province.get(9).body)
