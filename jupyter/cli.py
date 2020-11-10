import click

@click.group()
def cli():
    pass

@cli.command()
def export_rtk2_scenario_dat():
    import env
    from scenario import Scenario
    s = Scenario.from_file(env.get_work_path('tmp', 'SCENARIO.DAT'))

    import os
    base_dir_path = '..'
    csv_dir_path = os.path.join(base_dir_path, 'csvs')
    if not os.path.isdir(csv_dir_path):
        os.makedirs(csv_dir_path)

    import csv
    for ci, c in enumerate(s.chapters):
        print(f"start year={c.head.year}, mon={c.head.mon}")
        print(f"rulers num={c.head.num_rulers} colors={','.join(f'{color}' for color in c.head.ruler_colors)}")

        l_cols = ['birth', 'intelligence', 'war_ability', 'charm', 'lawfulness', 'virtue', 'ambition', 'faction', 'loyalty', 'service', 'alignment', 'lineage','men', 'weapon', 'training', 'name']
        s_cols = ['bir', 'int', 'war', 'chr', 'law', 'vir', 'amb', 'fct', 'loy', 'srv', 'ali', 'lin','men', 'wpn', 'trn', 'name']
        with open(os.path.join(csv_dir_path, f'{ci+1}_generals.csv'), 'w') as csvf:
            csvw = csv.writer(csvf)
            csvw.writerow(s_cols)
            for g in c.generals:
                if g.birth > 0:
                    name = ''.join(c for c in g.name if c.isalpha() or c.isspace())
                    values = [getattr(g, col) for col in l_cols[:-1]]
                    values.append(name)
                    csvw.writerow(values)

        l_cols = ['pop', 'gold', 'food', 'num_horses', 'pop_loyalty', 'land_dev', 'flood_dev', 'faction', 'governor', 'region1', 'region2', 'region3', 'region4']
        s_cols = ['idx', 'pop', 'gold', 'food', 'hrs', 'loy', 'lnd', 'fld', 'fct', 'gov', 'r1', 'r2', 'r3', 'rgn']
        with open(os.path.join(csv_dir_path, f'{ci+1}_provinces.csv'), 'w') as csvf:
            csvw = csv.writer(csvf)
            csvw.writerow(s_cols)
            for pi, p in enumerate(c.provinces):
                values = [pi + 1]
                values += [getattr(p, col) for col in l_cols]
                csvw.writerow(values)

        break

@cli.command()
def show_rtk2_taiki_dat():
    import env
    from taiki import Taiki
    taiki = Taiki.from_file(env.get_work_path('tmp', 'TAIKI.DAT'))
    for g in taiki.generals:
        print(f'birth={g.birth}, debut={g.debut}, home={g.home}, inte={g.intelligence}, wara={g.war_ability}, chrm={g.charm}, name="{g.name}"')

@cli.command()
def show_rtk2_hero_names():
    import env
    names = set()

    from scenario import Scenario
    s = Scenario.from_file(env.get_work_path('tmp', 'SCENARIO.DAT'))

    for c in s.chapters:
        for g in c.generals:
            if g.birth > 0:
                names.add(''.join(c for c in g.name if c.isalpha() or c.isspace()))

    from taiki import Taiki
    taiki = Taiki.from_file(env.get_work_path('tmp', 'TAIKI.DAT'))
    for g in taiki.generals:
        if g.birth > 0:
            names.add(''.join(c for c in g.name if c.isalpha() or c.isspace()))

    for name in sorted(names):
        print(name)

cli()

