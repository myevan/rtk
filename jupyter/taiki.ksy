meta:
  id: taiki
  file-extension: dat
  endian: le
seq:
  - id: head
    type: head
  - id: generals
    type: general
    repeat: eos
types:
  head:
    seq:
      - id: num_generals
        size: 6
  general:
    seq:
      - id: debut
        type: u1
      - id: auto_join
        type: u1
      - id: home
        type: u1
      - id: unknown1
        size: 4
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
      - id: belong
        type: u1
      - id: loyalty
        type: u1
      - id: service
        type: u1
      - id: hidden
        size: 1
      - id: unknown2
        size: 1
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
