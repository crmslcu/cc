import random

def pri(*args):
    for arg in args:
        print(arg)
    input()

sd=1
bd=10
cri_my=50
hp=100
mhp=100
life=True
mb={'타우로':(30,100)}


def att(mon,mond):
    critical=False
    mon_life=True
    global hp
    while mon_life == True:
        damage = random.randint(sd, bd)
        cri=random.randint(1,100)
        if cri_my > cri :
            critical==True
            print('크리티컬!')
            damage=damage*2
        else:
            critical==False
        pri(damage,'의 피해를 주었습니다.')
        mon=mon-damage
        if mon <= 0:
            mon_life=False
        else:
            mond = mond + random.randint(-5, 5)
            print(f"{mond} suffered damage.")
            hp = hp - mond
            if hp <= 0:
                life = False
                mon_life = False 
    return damage


pri('어느날 대머리 도적이 살았습니다.')

pri('대머리 도적은 오늘 어디서 사냥을 할지 고민을 하고 있었습니다.')

pri('한 시청자는 황갑충이나 캐라며 타우를 잡으러 가라 권했고 다른 시청자는 파티사냥을 통해 레벨업이나 하라고 말했습니다.')

pri('대머리 도적은 ')

pri('그래 결정했어')

sc='st'

목표달성=False
while 목표달성 != True:
    if sc=='st':
        dd1=input('황갑충을 캐러 타우로 가야겠어:타우, 파티원과 레벨업을 하러 가야겠어:요람')
        if dd1 == '타우':
            print('좋아 타우를 잡으러 가야겠어!')
            sc='jj1' 
        elif dd1 == '요람':
            print('dyf')   
        else:
            sc='st'
    elif life == False:
        pri('Game Over')
    elif sc=='jj1':
        pri('그렇게 대머리 도적은 저주받은 신전2에 도착했습니다.')
        pri('여기가 저주받은 신전이구나.')
        pri('대머리 도적은 자신의 황갑충을 매만지며 창을들고 설쳐대는 타우로마시스의 대가리에 뇌전수리검을 던졌다.')
        att(*mb['타우로'])
        pri('전투 종료. 남은',hp)
        sc=5
        

    elif sc==5:
        print("일비 표창을 획득했다",'공격력이 3증가했다')
        sd= sd+3
        목표달성=True



     
     def defense():
    
       
        elif hp<=0:
            life == False
            pri('사망')
            break
        else:
            mond=mond+random.randint(-5,5)
            pri(mond,'의 피해를 입었다.')
            hp=hp-mond
        


        



        def luk(monster_name,mon): #럭키세븐
    critical=False
    avoid_mon=mb[monster_name][2]
    final_accuracy=max(1,hr_my-avoid_mon) #최소 명중률 = 1
    hit_mon=random.randint(1,100)
    one_damage=0
    two_damage=0

    for _ in range(2):
        hit_mon<= final_accuracy   #fanal_accuracy=최종 명중률
        damage=random.randint(sd+10,sd+10)
        cri=random.randint(1,100)
        total_damage=0

        if cri_my > cri:
            critical==True
            damage=damage*2
            dm=damage

        if damage == 0:
            dm='miss'
            pri('몬스터 체력:', mon)
        else:
            dm=str(damage)
        mon=mon-damage
        pri(dm)
        if mon>=0:
            pri('몬스터 체력',mon)
        else:
            mon<=0
            pri('몬스터 체력:',str(0)) #체력이 0이하로 내려가면 0으로 표기후 사망표시
            pri('적 처치')
        
    else:
        pri('Miss')
        pri('몬스터 체력:', mon)
    return mon



    for _ in range(2):  # Perform the attack twice
        hit_mon = random.randint(1, 100)

        if hit_mon <= final_accuracy:  # final_accuracy=Final hit rate
            damage = random.randint(sd + 10, sd + 10)
            cri = random.randint(1, 100)

            if cri_my > cri:
                damage *= 2

            dm = str(damage)
            
            if damage == 0:
                dm = 'miss'

            damages.append(damage)

    for dmg in damages:
         print(str(dmg))       

    total_damage = sum(damages)
    mon -= total_damage
    pri('몬스터 체력:', mon)

    return mon



if item == '황갑충':
                        pri('황갑충을 착용해 공격력이 +3되었다.')
                        sd=sd+3
                        bd=bd+3
                        pri(sd,bd)

# 이 밑으로 기존 아이템 드랍 함수
def random_item(monster_name):
    items = drop_ls.get(monster_name, {})
    
    if items:
        item_drop = random.choices(list(items.keys()), weights=list(items.values()), k=1)[0]
        return item_drop
    else:
        return None


#이 밑으로 기존 공격 함수 

def att(monster_name,mon): #뇌전 던지기, 기본 공격
    critical=False
    avoid_mon = mb[monster_name][2]
    final_accuracy = max(1,hr_my-avoid_mon) #최소 명중률 1
    hit_mon = random.randint(1,100)

    if hit_mon <= final_accuracy: #최종 명중률
        damage = random.randint(sd, bd)
        cri=random.randint(1,100)
        if  cri_my > cri :
            critical==True
            damage=damage*2
            pri('\033[31m' + str(damage)+'의 피해를 입혔습니다.' +'\033[0m')
        elif damage == 0 and not critical:
            pri('\033[33m' + 'Miss' + '\033[0m')
            pri('몬스터 체력:', mon)
        else:
            critical==False
            pri('\033[33m' + str(damage) + '의 피해를 입혔습니다.' + '\033[0m')
        
        mon=mon-damage
        if mon>=0:
            pri('몬스터 체력:', mon)
        else:
            mon<=0
            pri('몬스터 체력:',str(0))
            pri('적 처치')

    else:
        pri('\033[33m' + 'Miss' + '\033[0m')
        pri('몬스터 체력:', mon)
    return mon

def luk(monster_name, mon):  #럭키 세븐
    avoid_mon = mb[monster_name][2]
    final_accuracy = max(1, hr_my - avoid_mon)  
    damages = []

    for _ in range(2): 
        hit_mon = random.randint(1, 100)

        if hit_mon <= final_accuracy:  # final_accuracy=Final hit rate
            damage = int(1.2*random.randint(sd,bd))
            cri = random.randint(1, 100)

            if cri_my > cri:
                damage *= 2
                print('\033[31m' + str(damage)+'의 피해를 입혔습니다.' + ' ' + '\033[0m')
            else:
                print('\033[33m' + str(damage)+'의 피해를 입혔습니다.' + ' ' + '\033[0m')

            if damage == 0:
                print('\033[33m' + 'miss ' + '\033[0m')
            else: 
                damages.append(damage)

        else:
            print('\033[31m' + 'miss ' + '\033[0m')
        print()

    total_damage = sum(damages)
    mon -= total_damage

    mon = max(0, mon)

    print('몬스터 체력: ' + str(mon))

    return mon

# 이 밑으로 기존 전투 과정

        while mon_life == True and life == True:
            bt1=input('뇌전투척 - 1\n럭키세븐 - 2\n어벤져 - 3')
            if bt1=='1':
                pri('뇌전투척!')
                skill_name='bsc'
                mon=att(skill_name,monster_name,mon)
                if  mon <= 0:
                    mon_life=False
                    get_item(monster_name)
                elif mon_life==True:
                    pri('적의 공격')
                    defense(monster_name,mond)
                    if hp<=0:
                        life=False
                else:
                    pri('오류')
            
            elif bt1=='2':
                pri('럭키세븐!')
                skill_name='luk'
                mon=att(skill_name,monster_name,mon)
                if  mon <= 0:
                    mon_life=False
                    get_item(monster_name)
                elif mon_life==True:
                    pri('적의 공격')
                    defense(monster_name,mond)
                    if hp<=0:
                        life=False
                else:
                    pri('오류')


            elif bt1=='3':
                pri('어벤져!')
                skill_name='ave'
                mon=att(skill_name,monster_name,mon)
                if  mon<=0:
                    mon_life=False 
                    get_item(monster_name)
                elif mon_life == True:
                    pri('적의 공격')
                    defense(monster_name,mond)
                    if hp<=0:
                        life=False
                else:
                    pri('오류')               
            else:
                sc='jj1'   
        sc=5





 skills = {'1': ('bsc', 'Thunder Battle Chuck'), '2': ('luk', 'Lucky Seven'), '3': ('ave', 'Avenger')}

    while mon_life and life:
        bt1 = input('Thunder Battle Chuck - 1\nLucky Seven - 2\nAvenger - 3')
        
        if bt1 in skills:
            skill_code, skill_display = skills[bt1]
            pri(f'{skill_display}!')
            mon = att(skill_code, monster_name, mon)