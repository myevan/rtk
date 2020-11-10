meta:
  id: scenario
  file-extension: dat
  endian: le
seq:
  - id: chapters
    type: chapter
    repeat: eos
types:
  chapter:
    seq:
      - id: head
        type: head
      - id: generals
        type: general
        repeat: expr
        repeat-expr: 255
      - id: special
        type: special
      - id: rulers
        type: ruler
        repeat: expr
        repeat-expr: 16
      - id: provinces
        type: province
        repeat: expr
        repeat-expr: 41
      - id: tail
        size: 146  
  head:
    seq:
      - id: zero
        type: u2
      - id: year
        type: u2
      - id: mon
        type: u1
      - id: num_rulers
        type: u1
      - id: ruler_colors
        size: 16
  general:
    seq:
      - id: gnid
        type: u2
      - id: unknown1
        type: u2
      - id: intelligence
        type: u1
      - id: war_ability
        type: u1
      - id: charm
        type: u1
      - id: lawfulness
        type: u1
      - id: virtue
        type: u1
      - id: ambition
        type: u1
      - id: faction
        type: u1
      - id: loyalty
        type: u1
      - id: service
        type: u1
      - id: hidden
        type: u1
      - id: unknown2
        type: u1
      - id: alignment
        type: u1
      - id: lineage
        type: u2
      - id: men
        type: u2
      - id: weapon
        type: u2
      - id: training
        type: u1
      - id: pos_in_war
        type: u2
      - id: birth
        type: u1
      - id: portrait1
        type: u1
      - id: portrait2
        type: u1
      - id: name
        type: str
        size: 15
        encoding: ascii    
  special:
    seq:
      - id: unknown1
        type: u1
      - id: empty_slot
        type: u2
      - id: sima_hui
        type: u1
      - id: xu_zijiang
        type: u1        
      - id: hua_tuo
        type: u1        
      - id: unknown2
        type: u1
  ruler:
    seq:
      - id: general
        type: u2
      - id: capital
        type: u2
      - id: advisor
        type: u2
      - id: trust
        type: u2
      - id: unknown1
        type: u1
      - id: unknown2
        type: u1
      - id: ally
        type: u2
      - id: unknown4
        type: u2
      - id: hostilities
        size: 16
      - id: joint_invasion_ally
        type: u1
      - id: join_invasion_target
        type: u1
      - id: target_province_faction_owner
        type: u1
      - id: marriage
        type: u1
      - id: exile
        type: u1
      - id: unknown5
        size: 6
  province:
    seq:
      - id: next
        type: u2
      - id: governor
        type: u2
      - id: unknown1
        type: u2
      - id: freegen1
        type: u2
      - id: gold
        type: u2
      - id: food
        type: u4
      - id: pop
        type: u2
      - id: faction
        type: u1
      - id: unknown2
        size: 5
      - id: land_dev
        type: u1
      - id: pop_loyalty
        type: u1
      - id: flood_dev
        type: u1
      - id: num_horses
        type: u1
      - id: num_forts
        type: u1
      - id: unknown3
        size: 4
      - id: region1
        type: u1
      - id: region2
        type: u1
      - id: region3
        type: u1
      - id: region4 
        type: u1
