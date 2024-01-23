import random
import math

def pri(*args):
    output = ' '.join(map(str, args))
    print(output)
    input()

#lv=레벨, sd=min damage, bd=max damage, cri_my= 크리티컬 확률, mhp=max hp
#hr_my= 명중률, avoid_my= 회피율
    
lv=100
sd=int(((((lv*5)**2/1000)+lv*5)/30 + (lv*5/200))+1)
bd=int((((lv*5)**2/1000)+lv*5))
cri_my=50
hr_my=100
avoid_my=100
mhp=int(math.log(lv)*(30+lv*6))+50
hp=mhp
life=True

#mb=momster_data_base
#0=체력, 1=공격력, 2=회피율, 3=명중률

mb={'타우로':(1000,1,10,70),'콜드아이':(50,10,10,10),'와일드카고':(500,10,5,50)}



def defense(monster_name,mond):
    global hp
    hit_me=random.randint(1,100)
    accuracy_mon=mb[monster_name][3]
    final_avoid=max(1,avoid_my-accuracy_mon) #최소 회피율 1
    if hit_me >=final_avoid:
        mond=mond+random.randint(-5,5)
        if mond>=0:
            print('\033[35m'+str(mond)+'의 피해를 입었다.' + '\033[0m')
            hp=hp-mond
        else:
            print('\033[35m'+'0의 피해를 입었다.' + '\033[0m')

        if hp>=0:
            pri('hp:', hp)
        else:
            hp<=0
            print('hp:',str(0))
            pri('사망')
    else:
        print('피했다.')
        pri('hp:', hp)
    return hp

def att(skill_name, monster_name, mon):         #att 함수로 모든 공격 실행
    avoid_mon = mb[monster_name][2]             #적의 회피율
    final_accuracy = max(1, hr_my - avoid_mon)  #최종 회피율 정의
    damages = []                                #총합 데미지
    dmp = 0                                     #데미지 배율 정의
    hit_nb = 0                                  #공격횟수 정의

    if skill_name == 'luk':                     #럭키 세븐
        hit_nb = 2
        dmp = 1.2
    elif skill_name == 'bsc':                   #기본 공격
        hit_nb = 1
        dmp = 1.0
    elif skill_name == 'ave':                   #어벤져
        hit_nb = 1                         
        dmp = 1.5
    elif skill_name == 'tri':                   #트리플 스로우
        hit_nb = 3
        dmp = 1.2
    elif skill_name == 'new':
        hit_nb = 10
        dmp = 0.5
    

    else:
        pri('스킬 타수, 퍼뎀 지정 오류')
            

    for _ in range(hit_nb):
        hit_mon = random.randint(1, 100)        #명중판정

        if hit_mon <= final_accuracy:
            damage = int(dmp * random.randint(sd, bd))
            cri = random.randint(1, 100)
            critical = cri_my > cri
            if critical:
                damage *= 2
                print('\033[31m' + f'{damage}의 피해를 입혔습니다.' + ' ' + '\033[0m')
            else:
                print('\033[33m' + f'{damage}의 피해를 입혔습니다.' + ' ' + '\033[0m')
            if damage == 0:
                print('\033[33m' + '0' + '\033[0m')
            else:
                damages.append(damage)

        else:
            print('\033[34m' + 'Miss ' + '\033[0m')

    total_damage = sum(damages)
    mon -= total_damage
    mon = max(0, mon)

    print('몬스터 체력: ' + str(mon))

    return mon


skills = {
    '1': ('bsc', '기본공격'),
    '2': ('luk', '럭키 세븐'),   
    '3': ('ave', '어벤져')
}

def skill_p(skill_code, skill_display):                    #skill_code= 스킬의 축약어, like=bsc
    new_index = len(skills) + 1                            #skill_display= 스킬의 이름, like=럭키세븐
    skills[str(new_index)] = (skill_code, skill_display)
    print(f'새로운 스킬 획득: {skill_display}!')

new_skills={
    'tri': '트리플 스로우',
    'new': '새 기술'
}

def remove_skill(skill_code):               #스킬 삭제
    for key, (code, _) in skills.items():
        if code == skill_code:
            del skills[key]
            print(f'Skill {skill_code} removed successfully from skills!')
            reorganize_skills()
            return

    print(f'Skill {skill_code} not found in skills.')

def reorganize_skills():                    #삭제 이후 순서를 재설정
    global skills
    new_skills = {}
    index = 1

    for key in sorted(skills, key=lambda k: int(k)):
        new_skills[str(index)] = skills[key]
        index += 1

    skills = new_skills

#drop_ls=몬스터별 드랍 테이블

drop_ls = {
    '타우로': {
        '뇌전 수리검': 0.1,
        '황갑충': 0.01,
        '고깔모자': 1,
        '타우로마시스의 뿔': 98.89
    },
    '콜드아이': {
        '하얀포션': 50,
        '콜드아이의 꼬리':50
    },
    '와일드카고': {
        '와일드카고의 눈':99.89,
        '엘릭서':1.1,
        '블러드 기간틱':0.011
    }
}


def get_item(monster_name):         #한번더 갈아엎기? 고민좀 해봅시다.
    items = drop_ls.get(monster_name, {}) 
    if items:
        item = random.choices(list(items.keys()), weights=list(items.values()), k=1)[0]
        print(f"{item}을 얻었다.")

        if drop_ls[monster_name][item] == 0.1:
            pri('공격력이 5 증가했다.')
            sd+=5
            bd+=5
            pri(sd,bd)
        elif drop_ls[monster_name][item] == 0.01:
            pri('공격력이 30 증가했다.')
            sd+=30
            bd+=30
            pri(sd,bd)
        elif drop_ls[monster_name][item] == 1:
            pri('또 고깔이다. 고깔고깔')
        else:
            pri('잡템을 팔아 돈을 얻었다.')
    else:
        pri('오류임.')


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
        dd1=input('황갑충을 캐러 타우로 가야겠어 - 1\n파티원과 레벨업을 하러 가야겠어 - 2')
        if dd1 == '1':
            print('좋아 타우를 잡으러 가야겠어!')
            sc='jj1' 
        elif dd1 == '2':
            print('요람 파티사냥을 가야겠다.')
            sc='yo1'
        else:
            sc='st'
    elif life == False:
        pri('Game Over')
    elif sc=='jj1':
        pri('그렇게 대머리 도적은 저주받은 신전2에 도착했습니다.')
        pri('여기가 저주받은 신전이구나.')
        pri('대머리 도적은 자신의 황갑충을 매만지며 창을들고 설쳐대는 타우로마시스의 대가리에 뇌전수리검을 던졌다.')
        pri('전투 돌입')
        mon_life = True
        monster_name='타우로'
        mon=mb[monster_name][0]
        mond=mb[monster_name][1]

        while mon_life and life:
            bt1 = input('\n'.join([f'{skill_display} - {index + 1}' for index, (_, skill_display) in enumerate(skills.values())]) + '\n')
        
            if bt1 in skills:
                skill_code, skill_dp = skills[bt1]
                print()
                print(f'{skill_dp}!')
                mon = att(skill_code, monster_name, mon)

                if mon <= 0:
                    mon_life = False
                    get_item(monster_name)
                elif mon_life:
                    pri('적 공격')
                    defense(monster_name, mond)
                    if hp <= 0:
                        life = False
                else:
                    pri('error')
            else:
                sc = 'jj1'
        pri('타우로 마시스를 잡고 새로운 스킬을 습득했다.')
        skill_p('tri', new_skills['tri'])

        sc='yo1'

    elif sc=='yo1':
        pri('그렇게 5명의 파티원을 구한 대머리 도적은 차가운 요람에 도착했다.')
        pri('전투 돌입')
        
        mon_life = True
        monster_name='콜드아이'
        mon=mb[monster_name][0]
        mond=mb[monster_name][1]

        while mon_life and life:
            bt1 = input('\n'.join([f'{skill_display} - {index + 1}' for index, (_, skill_display) in enumerate(skills.values())]) + '\n')
        
            if bt1 in skills:
                skill_code, skill_dp = skills[bt1]
                print()
                print(f'{skill_dp}!')
                mon = att(skill_code, monster_name, mon)

                if mon <= 0:
                    mon_life = False
                    get_item(monster_name)
                elif mon_life:
                    pri('적 공격')
                    defense(monster_name, mond)
                    if hp <= 0:
                        life = False
                else:
                    pri('error')
            else:
                sc = 'yo1'   
        sc=5

    elif sc==5:
        pri(skills)

    

