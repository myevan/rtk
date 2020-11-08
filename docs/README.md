# Diary

# Day-1

## UI

### Province

```
Jan 189 AD (Spring)
                               1   | 9. Yong 
                             /     | Ruler: Cao Cao
  15                4 - 3 - 2      | Trust: 50
    \               | \ |          | Governor: Cao Cao
    14              5 - 7 - 6      | Advisor: Chen Gong
      \            / \ / \ / \     |---------------------------------------
       13 - 12 - 11 - 10 - 9 -- 8  | Pop   350000  Gold    1000  Loy    60
      / \  /  \  / \  / \ /  \ /   | Men    20000  Food   40000  Land   60
    30 - 29 - 20 - 19 - 17 - 16    | Generals   9  Rate      46  Flood  30
    /  \ / \ /  \ /  \ / \  /  \   | FreeGens   0  Horses    20  Forts   2
  33 - 32 - 31 - 21 - 28 - 18 - 24 |---------------------------------------
  / \ /  \  / \ /  \  / \  / \ /   | Cao Cao, your orders for
35 - 34 - 40 - 23 - 22 - 27 - 25   | Province 9 (0-19)?
  \  / \ /  \ / \  /  \ / \  /     |
   36 - 41 - 39  38 - 37 - 26      |
```

### General

```
Guan Yu

(Liu Bei's cohort)  Loy 100
Arm    10  Rnk Act  Int  83
Trn    10  Ser   1  War  99
Men  1000  Age  28  Chr  91
```

## Model

### Province

* Number: 번호
* Ruler: 군주
* Governor: 태수
* Advisor: 군사
* Pop: 인구
* Men: 병사
* Gold: 자금
* Food: 식량
* Rate: 물가
* Loy: 민충성도
* Land: 토지가치
* Flood: 치수도
* Generals: 현역장수
* FreeGens: 재야장수
* Horses: 명마
* Forts: 성채
* Name: 이름

### General

* Debut: 등장년도
* Birth: 출생년도
* Trust: 신뢰도
* Home: 출신
* Int: 지력
* War: 무력
* Chr: 매력
* Loy: 충성
* Rnk: 지위
* Ser: 연차
* Men: 병사
* Trn: 사기
* Weap: 무장
* RelShip: 관계
* RelGen: 관계 장수
* Name: 이름
* 야망
* 의리
* 인덕
* 상성

## Day-2

### Provinces

* 유주: 1, 2, 3
* 병주: 4, 5
* 기주: 6, 7
* 청주: 8
* 연주: 9
* 사주: 10, 11
* 옹주: 12, 13
* 량주: 14, 15
* 서주: 16
* 예주: 17, 18
* 형주: 19, 20, 21, 22, 23
* 양주: 24, 25, 26, 27, 28
* 익주: 29, 30, 31, 32, 33, 34, 35, 36
* 교주: 37, 38, 39, 40, 41

### Functions

* Rest: 대기(휴식)
* Move: 이동
* Send: 수송
* War: 전쟁
* Milit: 군사
    * Hire: 징병
    * Reassign: 재편성
    * Train: 훈련
* Person: 인사
    * Recruit: 등용
        * SpecialVisit: 삼고의예
        * Horse: 명마
        * Gold: 돈
        * Letter: 편지
    * Search: 수색
    * Appoint: 임명
        * Governor: 태수
        * Advisor: 군사
    * Dismiss: 해임
        * General: 장수
        * Advisor: 군사
* Diplom: 외교
    * Alliance: 동맹
    * JointInvasion: 공동작전
    * Marriage: 혼인
    * Gift: 선물
    * CancelAlliance: 동맹파기
    * Threaten: 항복권고
* Spy: 계략
    * Infiltrate: 매복의독
        * Hide: 매복
        * Verify: 확인
        * Withdraw: 철수
    * RivalTrigers: 이호경식
    * TrigerAndWolf: 구호탄랑
    * Betrayal: 적중작적
    * ForgedLetter: 위서의심
* View: 정보
    * Other provinces: 타국정보
    * Generals: 장수정보
    * Summary1: 장수요약1
    * Summary2: 장수요약2
    * Territory: 속령목록
    * DataOrder: 정렬순서
        * Intellect 지력
        * WarAbility 무력
        * Charm 매력
        * Men 병사수
        * Loyalty 충성도
* Cultiv: 개발
* Flood: 치수
* Reward: 포상
    * Gold: 돈
    * Horse: 명마
    * Wrtings: 서적
* Give: 선정
* Merch: 매매
    * SellFood: 식량 판매
    * BuyFood: 식량 구매
    * BuyHorses: 명마 구매
    * BuyWeapons: 무기 구매
* Map: 지도
* Delegate: 위임
* Exile: 방랑
* Advice: 특별 
    * Advice: 군사조언
    * Rumors: 소문
    * Healing: 치료
* Other: 기타
    * Wait: 대기
        * MessageWait: 서신속도
        * MessengerSpeed: 사신속도
    * Graphics: 도
    * Music: 배경음
    * SoundEffects: 효과음
    * Save: 저장
    * HEXWar: 전쟁
    * QuitPlayer: 플레이 종료
    * QuitGame: 게임 종료

## Analysis

<https://rotk2.fandom.com/wiki/Scenario_Initialization>

### SCENARIO.DAT 

<https://github.com/myevan/rtk/blob/main/jupyter/scenario.ks>

```bash
$ ./jupyter/cli.sh show-rtk2-scenario-dat
```

### TAIKI.DAT

<https://github.com/myevan/rtk/blob/main/jupyter/taiki.ks>

```bash
$ ./jupyter/cli.sh show-rtk2-taiki-dat
```
