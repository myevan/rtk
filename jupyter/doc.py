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
        yield f"Pop: {self.pop:>7}  Gold: {self.gold:>6}  Loy: {self.loy:>5}"
        yield f"Men: {self.men:>7}  Food: {self.food:>6}  Land: {self.land:>4}"
        yield f"Generals: {self.generals:>2}  Rate: {self.rate:>6}  Flood: {self.flood:>3}"
        yield f"FreeGens: {self.free_gens:>2}  Horses: {self.horses:>4}  Forts: {self.forts:>3}"

if __name__ == "__main__":
    Hero.set_default(Hero(id=0, name=T("무명")))   
    Hero.put(Hero(id=1,  inte=70, wara=75, chrm=72, birth=189-37, trust=50, arm=10, trn=10, men=10000, name=T("공손찬")))
    Hero.put(Hero(id=2,  inte=85, wara=70, chrm=99, birth=189-29, trust=50, arm=10, trn=10, men=10000, name=T("유비")))
    Hero.put(Hero(id=3,  inte=70, wara=81, chrm=70, birth=189-45, trust=50, arm=10, trn=10, men=10000, name=T("원소")))
    Hero.put(Hero(id=4,  inte=53, wara=51, chrm=50, birth=189-41, trust=50, arm=10, trn=10, men=10000, name=T("한복")))
    Hero.put(Hero(id=5,  inte=82, wara=35, chrm=87, birth=189-37, trust=50, arm=10, trn=10, men=10000, name=T("공융")))
    Hero.put(Hero(id=6,  inte=95, wara=91, chrm=95, birth=189-35, trust=50, arm=10, trn=10, men=10000, name=T("조조")))
    Hero.put(Hero(id=7,  inte=55, wara=90, chrm=44, birth=189-35, trust=50, arm=10, trn=10, men=10000, name=T("동탁")))
    Hero.put(Hero(id=8,  inte=54, wara=95, chrm=87, birth=189-34, trust=50, arm=10, trn=10, men=10000, name=T("마등")))
    Hero.put(Hero(id=9,  inte=62, wara=51, chrm=78, birth=189-58, trust=50, arm=10, trn=10, men=10000, name=T("도겸")))
    Hero.put(Hero(id=10, inte=69, wara=80, chrm=50, birth=189-36, trust=50, arm=10, trn=10, men=10000, name=T("원술")))
    Hero.put(Hero(id=11, inte=74, wara=73, chrm=68, birth=189-48, trust=50, arm=10, trn=10, men=10000, name=T("유표")))
    Hero.put(Hero(id=12, inte=87, wara=90, chrm=89, birth=189-34, trust=50, arm=10, trn=10, men=10000, name=T("손견")))
    Hero.put(Hero(id=13, inte=60, wara=48, chrm=48, birth=189-38, trust=50, arm=10, trn=10, men=10000, name=T("왕랑")))
    Hero.put(Hero(id=14, inte=56, wara=18, chrm=23, birth=189-39, trust=50, arm=10, trn=10, men=10000, name=T("유엽")))
    Hero.put(Hero(id=15, inte=85, wara=45, chrm=90, birth=189-53, trust=50, arm=10, trn=10, men=10000, name=T("유언")))
    Province.put(Province(id=1, pop=65000,   gold=100,  food=2000,  rate=50, horses=5,  loy=5, land=10,  flood=5,  forts=1, ruler_id=0,  governor_id=0, name=T("유주")))
    Province.put(Province(id=2, pop=70000,   gold=100,  food=2000,  rate=50, horses=5,  loy=5, land=10,  flood=5,  forts=2, ruler_id=0,  governor_id=0, name=T("유주")))
    Province.put(Province(id=3, pop=100000,  gold=1000, food=25000, rate=58, horses=10, loy=35, land=55, flood=30, forts=4, ruler_id=1,  governor_id=0, name=T("유주")))
    Province.put(Province(id=4, pop=100000,  gold=1000, food=25000, rate=34, horses=10, loy=55, land=50, flood=30, forts=0, ruler_id=2,  governor_id=0, name=T("병주")))
    Province.put(Province(id=5, pop=70000,   gold=100,  food=2000,  rate=50, horses=5,  loy=15, land=25, flood=0,  forts=1, ruler_id=0,  governor_id=0, name=T("유주")))
    Province.put(Province(id=6, pop=500000,  gold=1000, food=50000, rate=44, horses=15, loy=50, land=50, flood=50, forts=3, ruler_id=3,  governor_id=0, name=T("기주")))
    Province.put(Province(id=7, pop=120000,  gold=1000, food=30000, rate=57, horses=15, loy=55, land=65, flood=50, forts=3, ruler_id=4,  governor_id=0, name=T("기주")))
    Province.put(Province(id=8, pop=80000,   gold=1000, food=25000, rate=50, horses=10, loy=65, land=65, flood=50, forts=2, ruler_id=5,  governor_id=0, name=T("청주")))
    Province.put(Province(id=9, pop=350000,  gold=1000, food=40000, rate=41, horses=20, loy=60, land=60, flood=30, forts=2, ruler_id=6,  governor_id=0, name=T("연주")))
    Province.put(Province(id=10, pop=800000, gold=1000, food=50000, rate=58, horses=30, loy=45, land=65, flood=50, forts=6, ruler_id=7,  governor_id=0, name=T("사주")))
    Province.put(Province(id=11, pop=450000, gold=500,  food=25000, rate=70, horses=15, loy=35, land=45, flood=35, forts=3, ruler_id=7,  governor_id=0, name=T("사주")))
    Province.put(Province(id=12, pop=250000, gold=500,  food=25000, rate=57, horses=20, loy=40, land=45, flood=30, forts=4, ruler_id=7,  governor_id=0, name=T("사주")))
    Province.put(Province(id=13, pop=240000, gold=100,  food=2000,  rate=50, horses=5,  loy=25, land=20, flood=20, forts=3, ruler_id=0,  governor_id=0, name=T("옹주")))
    Province.put(Province(id=14, pop=230000, gold=1000, food=25000, rate=44, horses=30, loy=40, land=45, flood=40, forts=1, ruler_id=8,  governor_id=0, name=T("량주")))
    Province.put(Province(id=15, pop=80000,  gold=100,  food=2000,  rate=50, horses=20, loy=5,  land=10, flood=5,  forts=1, ruler_id=0,  governor_id=0, name=T("량주")))
    Province.put(Province(id=16, pop=150000, gold=1000, food=35000, rate=49, horses=15, loy=55, land=50, flood=25, forts=2, ruler_id=9,  governor_id=0, name=T("서주")))
    Province.put(Province(id=17, pop=200000, gold=100,  food=2000,  rate=50, horses=10, loy=45, land=50, flood=20, forts=4, ruler_id=0,  governor_id=0, name=T("예주")))
    Province.put(Province(id=18, pop=250000, gold=100,  food=2000,  rate=50, horses=10, loy=40, land=50, flood=10, forts=3, ruler_id=0,  governor_id=0, name=T("예주")))
    Province.put(Province(id=19, pop=900000, gold=1000, food=40000, rate=52, horses=20, loy=50, land=50, flood=40, forts=4, ruler_id=10, governor_id=0, name=T("형주")))
    Province.put(Province(id=20, pop=800000, gold=1000, food=45000, rate=56, horses=30, loy=65, land=65, flood=40, forts=3, ruler_id=11, governor_id=0, name=T("형주")))
    Province.put(Province(id=21, pop=600000, gold=1000, food=50000, rate=47, horses=20, loy=55, land=65, flood=40, forts=4, ruler_id=12, governor_id=0, name=T("형주")))
    Province.put(Province(id=22, pop=500000, gold=100,  food=2000,  rate=50, horses=15, loy=40, land=55, flood=10, forts=3, ruler_id=0,  governor_id=0, name=T("형주")))
    Province.put(Province(id=23, pop=650000, gold=100,  food=2000,  rate=50, horses=10, loy=40, land=50, flood=5,  forts=1, ruler_id=0,  governor_id=0, name=T("형주")))
    Province.put(Province(id=24, pop=350000, gold=1000, food=30000, rate=31, horses=10, loy=50, land=55, flood=30, forts=3, ruler_id=13, governor_id=0, name=T("양주")))
    Province.put(Province(id=25, pop=150000, gold=100,  food=2000,  rate=50, horses=5,  loy=30, land=40, flood=10, forts=1, ruler_id=0,  governor_id=0, name=T("양주")))
    Province.put(Province(id=26, pop=70000,  gold=100,  food=2000,  rate=50, horses=5,  loy=25, land=15, flood=5,  forts=0, ruler_id=0,  governor_id=0, name=T("양주")))
    Province.put(Province(id=27, pop=80000,  gold=100,  food=2000,  rate=50, horses=5,  loy=25, land=15, flood=5,  forts=4, ruler_id=0,  governor_id=0, name=T("양주")))
    Province.put(Province(id=28, pop=150000, gold=1000, food=30000, rate=51, horses=10, loy=50, land=50, flood=20, forts=0, ruler_id=14, governor_id=0, name=T("양주")))
    Province.put(Province(id=29, pop=300000, gold=100,  food=2000,  rate=50, horses=5,  loy=35, land=35, flood=5,  forts=3, ruler_id=0,  governor_id=0, name=T("익주")))
    Province.put(Province(id=30, pop=300000, gold=500,  food=25000, rate=61, horses=15, loy=60, land=65, flood=30, forts=0, ruler_id=15, governor_id=0, name=T("익주")))
    Province.put(Province(id=31, pop=300000, gold=100,  food=2000,  rate=50, horses=5,  loy=35, land=35, flood=5,  forts=1, ruler_id=0,  governor_id=0, name=T("익주")))
    Province.put(Province(id=32, pop=250000, gold=500,  food=25000, rate=44, horses=15, loy=55, land=55, flood=30, forts=0, ruler_id=15, governor_id=0, name=T("익주")))
    Province.put(Province(id=33, pop=348500, gold=1000, food=35000, rate=51, horses=20, loy=60, land=65, flood=30, forts=4, ruler_id=15, governor_id=0, name=T("익주")))
    Province.put(Province(id=34, pop=150000, gold=100,  food=2000,  rate=50, horses=5,  loy=40, land=30, flood=5,  forts=3, ruler_id=0,  governor_id=0, name=T("익주")))
    Province.put(Province(id=35, pop=80000,  gold=100,  food=2000,  rate=50, horses=5,  loy=35, land=25, flood=5,  forts=1, ruler_id=0,  governor_id=0, name=T("익주")))
    Province.put(Province(id=36, pop=85000,  gold=100,  food=2000,  rate=50, horses=5,  loy=35, land=35, flood=5,  forts=2, ruler_id=0,  governor_id=0, name=T("익주")))
    Province.put(Province(id=37, pop=60000,  gold=100,  food=2000,  rate=50, horses=0,   loy=5, land=10, flood=5,  forts=1, ruler_id=0,  governor_id=0, name=T("교주")))
    Province.put(Province(id=38, pop=55000,  gold=100,  food=2000,  rate=50, horses=0,   loy=5, land=10, flood=0,  forts=0, ruler_id=0,  governor_id=0, name=T("교주")))
    Province.put(Province(id=39, pop=60000,  gold=100,  food=2000,  rate=50, horses=0,   loy=5, land=10, flood=0,  forts=0, ruler_id=0,  governor_id=0, name=T("교주")))
    Province.put(Province(id=40, pop=65000,  gold=100,  food=2000,  rate=50, horses=5,   loy=5, land=15, flood=5,  forts=0, ruler_id=0,  governor_id=0, name=T("교주")))
    Province.put(Province(id=41, pop=80000,  gold=100,  food=2000,  rate=50, horses=0,   loy=5, land=15, flood=5,  forts=1, ruler_id=0,  governor_id=0, name=T("교주")))
    print(Province.get(9).head)
    print(Province.get(9).body)
