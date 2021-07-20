"""
一回合制游戏
每个角色有 hp 和 Power  代表血量和攻击力
定义fight 方法
血量剩余多的人获胜
"""


def game():
    my_hp = 1000
    my_power = 200
    your_hp = 1000
    your_power = 199

    while True:
        my_hp = my_hp - your_power
        your_hp = your_hp - my_power
        if my_hp <= 0:
            print("我输了~~")
            break
        elif your_hp <= 0:
            print("你输了~~")
            break

    # if my_final_hp > your_final_hp:
    #     print("我赢了！")
    # else:
    #     print("你赢了！")
    # 三目运算
    # print("我赢了！") if my_final_hp > your_final_hp else print("你赢了！")


game()
