import random
import math

def pri(*args):
    output = ' '.join(map(str, args))
    print(output)
    input()

#lv=레벨, sd=min damage, bd=max damage, cri_my= 크리티컬 확률, mhp=max bp
#hr_my= 명중률, avoid_my= 회피율
    
lv=100
sd=int(((((lv*5)**2/1000)+lv*5)/30 + (lv*5/200))+1)
bd=int((((lv*5)**2/1000)+lv*5))
cri_my=50
hr_my=10
avoid_my=60
mhp=int(math.log(lv)*(30+lv*6))+50
hp=mhp
life=True

#mb=momster_data_base
#0=체력, 1=공격력, 2=회피율, 3=명중률

mb={'타우로':(10000,10,5,70),'콜드아이':(50,5,10,10)}



def defense(monster_name,mond):
    global hp
    hit_me=random.randint(1,100)
    accuracy_mon=mb[monster_name][3]
    final_avoid=max(1,avoid_my-accuracy_mon)
    if hit_me >=final_avoid:
        mond=mond+random.randint(-5,5)
        pri('\033[35m'+str(mond)+'의 피해를 입었다.' + '\033[0m')
        hp=hp-mond
        if hp>=0:
            pri('hp:', hp)
        else:
            hp<=0
            pri('hp:',str(0))
            pri('사망')
    else:
        pri('피했다.')
        pri('hp:', hp)
    return hp

def att(monster_name,mon):
    critical=False
    avoid_mon=mb[monster_name][2]
    final_accuracy=max(1,hr_my-avoid_mon)
    hit_mon=random.randint(1,100)

    if hit_mon <= final_accuracy:
        damage = random.randint(sd, bd)
        cri=random.randint(1,100)
        if  cri_my > cri :
            critical==True
            print('\033[31m'+'크리티컬!'+'\033[0m')
            damage=damage*2
            dm='\033[31m' + str(damage) + '의 피해를 입혔습니다.' + '\033[0m'
        if damage == 0 and not critical:
            dm = '\033[33m' + 'Miss' + '\033[0m'
            pri('몬스터 체력:', mon)
        else:
            critical==False
            dm='\033[33m' + str(damage) + '의 피해를 입혔습니다.' + '\033[0m'
        
        mon=mon-damage
        pri(dm)
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


#drop_ls=몬스터별 드랍 테이블

drop_ls = {
    '타우드랍': {
        '뇌전 수리검': 0.1,
        '황갑충':0.01,
        '고깔모자':1,
        '타우로마시스의 뿔':98.89
    },
    '콜드드랍': {
        '하얀포션': 50,
        '콜드아이의 꼬리':50
    }
}


def random_item(monster):
    items = drop_ls.get(monster, {})
    
    if items:
        item_drop = random.choices(list(items.keys()), weights=list(items.values()), k=1)[0]
        return item_drop
    else:
        return None

print(sd,bd,mhp,hr_my)

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
        if dd1 == 'to':
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
        mon_life = True
        monster_name='타우로'
        mon=mb[monster_name][0]
        mond=mb[monster_name][1]
        while mon_life == True and life == True:
            if  mon <= 0:
                mon_life=False
                monster_drop='콜드드랍'
                item=random_item(monster_drop)
                pri('획득:',item)
            elif hp<=0:
                life=False
            else:
                mon=att(monster_name,mon)
                if mon >=0:
                    defense(monster_name,mond)    
        sc=5
    elif sc==5:
        pri('dd')
        sd= sd+3
        목표달성=True


        
        