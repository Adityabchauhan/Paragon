import math
def power():
    D = int(input("Enter degree of paragon:"))
    if D==1:
        P=0
    elif 2<=D<=99:
        P=(50*int(math.pow(D,3)) + 5025*int(math.pow(D,2)) + 168324*D + 843000)/600
    elif D==100:
        P=200000
    print("Required power for degree",D,"paragon is:",P)
    
def curr_power():
    T5=int(input("Enter the no of tier 5 monkeys(Excluding first three tier-5 towers):"))*10000
    NT5=int(input("Enter the no of non tier 5 monkeys:"))*100
    M=int(input("Enter amount of total money spent(Excluding first three tier-5 towers):"))/25
    P=int(input("Enter total amount of pops(Including first three tier-5 towers):"))/180
    PPT=int(input("Enter amount of paragon power totems:"))*2000
    total_pow=T5+NT5+M+P+PPT
    print(total_pow)
    for i in range(0,101):
        if (i+1)==1:
            P=0
        elif 2<=(i+1)<=99:
            P=(50*int(math.pow((i+1),3)) + 5025*int(math.pow((i+1),2)) + 168324*(i+1) + 843000)/600
        elif (i+1)==100:
            P=200000

        if P>=total_pow:
            print("You will generate a degree",i,"paragon")
            break

while True:
    print('''
1. To Find out Required Power for Paragon
2. Calculate your total power
3. Tips
4. Credits
5. Exit
''')
    ch=int(input("Enter your choice:"))
    if ch==1:
        power()
    elif ch==2:
        curr_power()
    elif ch==3:
        print('''

Degree 1:
0 Power Needed.
Purchase the first three tier-5 upgrades.

Degree 20:
11,219 Power Needed.
Purchase the first three tier-5 upgrades.
Have at least 17 tier 4 towers with maxed cross pathing (i.e. 2-4-0 as opposed to 0-4-0)
Have $125,000 invested in the non-tier 5 sacrifices.

Degree 40:
31,891 Power Needed.
Purchase the first three tier-5 upgrades.
Have at least 17 tier 4 towers with maxed cross pathing (i.e. 2-4-0 as opposed to 0-4-0)
Have $250,000 invested in the non-tier 5 sacrifices.
Have 2,040,000 pops (or $510,000 cash generated) achieved across sacrificial towers.

Degree 60:
67,512 Power Needed.
Purchase the first three tier-5 upgrades.
Have at least 17 tier 4 towers with maxed cross pathing (i.e. 2-4-0 as opposed to 0-4-0)
Have $250,000 invested in the non-tier 5 sacrifices.
Have 8,350,000 pops (or $2,087,500 cash generated) achieved across sacrificial towers.

Degree 76 (Max without Power Totems):
Purchase the first three Tier 5 upgrades.
Have 100 tier-4 or below upgrades distributed among the other sacrificial monkeys, excluding the first three tier 5 towers.
Invest at least $250,000 on the sacrificed towers, excluding the first three tier 5 towers.
Accumulate 16,200,000 pops (or $4,050,000 cash generated or round 132) across all sacrificed towers.

Degree 100 (Max):
200,000 Power Needed
Buy the first three Tier 5 upgrades.
Have 100 Tier 4 or below upgrades distributed among the other sacrificial monkeys, excluding the first
three tier 5 towers. (Note: 4-0-2 counts as 6 Tiers)
Have $250,000 spent on the sacrificed towers, excluding the first three tier 5 towers.
Accumulate 16,200,000 pops (or $4,050,000 cash generated) across all sacrificed towers.
If in single player, Purchase 45 Paragon Power Totems (40 if the player can purchase a second Crossbow
Master for Apex Plasma Master).
If in co-op, have 3 Additional Co-Op players (or 2 extra players if all have the MasterDoubleCrossIcon.
png Master Double Cross MK) with 9 additional Tier 5 towers.
''')
    elif ch==4:
        print('''Made by u/Adityabchauhan
Bibilography: https://bloons.fandom.com/wiki
''')
    elif ch==5:
              break
            

