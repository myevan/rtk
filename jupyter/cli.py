import click

@click.group()
def cli():
    pass

@cli.command()
def show_rtk2_scenario_dat():
    import env
    from scenario import Scenario
    s = Scenario.from_file(env.get_work_path('tmp', 'SCENARIO.DAT'))
    for c in s.chapters:
        print(f"start year={c.head.year}, mon={c.head.mon}")
        print(f"rulers num={c.head.num_rulers} colors={','.join(f'{color}' for color in c.head.ruler_colors)}")
        for g in c.generals:
            if g.birth > 0:
                name = ''.join(c for c in g.name if c.isalpha() or c.isspace())
                print(f'birth={g.birth}, inte={g.intelligence}, wara={g.war_ability}, chrm={g.charm}, name="{name}", id={g.gnid}')
        break

@cli.command()
def show_rtk2_taiki_dat():
    import env
    from taiki import Taiki
    taiki = Taiki.from_file(env.get_work_path('tmp', 'TAIKI.DAT'))
    for g in taiki.generals:
        print(f'birth={g.birth}, debut={g.debut}, home={g.home}, inte={g.intelligence}, wara={g.war_ability}, chrm={g.charm}, name="{g.name}"')

cli()

