# Action Hero

from .list_hero import *

count_round = 0 
def round():   
    global count_round

    count_round += 1
    print(f"\nRound {count_round}")

    return count_round

def match(no_match,hero1,hero2):

    def match_start():
        print("\n" + "="*30)
        print(f"\nMatch {no_match} Start!")
        print(f"{hero1.name} VS {hero2.name}")
        print("\n"+"="*30)

    match_start()

    while(True):

        round()

        hero1.menyerang(hero2)
        hero2.menyerang(hero1)

        if hero1.health <= 0:
                print("\n"+"="*30)
                print(f"\n{hero1.name} lose, {hero2.name} win!")
                break
        elif hero2.health <= 0:
                print("\n"+"="*30)
                print(f"\n{hero1.name} lose, {hero2.name} win!")
                break
        
        print("\n" + "-"*30)
    
    def match_over():
        print(f"Match {no_match} Over!")
        print("\n" + "="*30)
    
    match_over()