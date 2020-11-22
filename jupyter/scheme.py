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
    hrs = Integer()
    loy = Integer()
    lnd = Integer()
    fld = Integer()
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
        yield f"Men: {self.men:>7}  Food: {self.food:>6}  Land: {self.lnd:>4}"
        yield f"Generals: {self.generals:>2}  Rate: {self.rate:>6}  Flood: {self.fld:>3}"
        yield f"FreeGens: {self.free_gens:>2}  Horses: {self.hrs:>4}  Forts: {self.forts:>3}"

if __name__ == "__main__":
    Hero.set_default(Hero(id=0, name=T("무명")))   
    Hero.put(Hero(id=6,  inte=95, wara=91, chrm=95, birth=189-35, trust=50, arm=10, trn=10, men=10000, name=T("조조")))
    Province.put(Province(id=9, pop=350000,  gold=1000, food=40000, rate=41, hrs=20, loy=60, lnd=60, fld=30, forts=2, ruler_id=6,  governor_id=0, name=T("연주")))
    print(Province.get(9).head)
    print(Province.get(9).body)
