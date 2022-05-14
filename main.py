# Author: Akhilesh Bandaru
# Date: July 20th 2021
# File Name: Bandaru_CPT.py
# Description: This program will run the game FIGHT CLUB! The program will involve user to pick a fighter and use it to win a best out of 5 series.

# import statments here
import random

# global variables here
flag = True  # loop control
secondflag = True
thirdflag = True
fourthflag = True

userChoice = ''  # var that holds the RETURNED choice from getChoice()
fightertype = ['Wrestler', 'Balanced', 'Striker']
fightertypehealth = [250, 200, 150]

strikermoves = ['Punch', 'Kick']
strikermovespower = [40, 60]

balancedmoves = ['Clinch', 'Punch']
balancedmovespower = [20, 30]

wrestlermoves = ['Choke', 'Submission']
wrestlermovespower = [80, 100]

probabilityforhit = [3, 7, 6]

fighter = ''
health = 0
move1hitpower = 0
move2hitpower = 0
fightermove1 = ''
fightermove2 = ''
numberoftrainingsessions = 0
computerhealth = 0
computermove1power = 0
computermove2power = 0
computermove1 = ''
computermove2 = ''
wins = 0
losses = 0
hitprobability = 0
numberoftrainingsessions = 0
playerwins = 0
computerwins = 0

# List player stats: health, fighter type, probability ratio, 1hitpower, 2hitpower, move1, move2
selectedplayervar = [0, '', 0, 0, 0, 0, 0]

# computer player stats:  health, fight type, move1, move2, move1power, move2power
computerplayerstats = [0, '', '', '', 0, 0]


def showMenu():  # Display menu options
    print('   MENU')
    print('==========')
    print('P to Play Game')
    print('H for Help')
    print('Q to Quit')
    print('S for Starter Fighter Stats')
    print('==========')
    print(' ')


def getChoice():  # get user's choice
    choice = input('Option?: ')
    choice = choice.capitalize()
    return choice


def showHelp():
    print('')
    print('Please provide the fighter choice and play game.')
    print('')
    print('You can quit this program from the main menu by pressing Q')


def showPlayerstats():
    print('Striker:(Hit/Miss ratio: 40/60), (Health: 150 HP)')
    print('Balanced: (Hit/Miss ratio: 50/50), (Health: 200 HP)')
    print('Wrestler: (Hit/Miss ratio: 30/70), (Health: 250 HP)')


def selectedplayerfunction(userselection):
    indexflightertype = int(fightertype.index(userselection))

    print('Health available for chosen player ' + userselection + ' is: ' + str(fightertypehealth[indexflightertype]))
    selectedplayervar[0] = fightertypehealth[indexflightertype]
    selectedplayervar[1] = userfighterpick
    selectedplayervar[2] = probabilityforhit[indexflightertype]
    print('Selected player available moves:')
    if userfighterpick == 'Wrestler':
        selectedplayervar[3] = wrestlermovespower[0]
        selectedplayervar[4] = wrestlermovespower[1]
        selectedplayervar[5] = wrestlermoves[0]
        selectedplayervar[6] = wrestlermoves[1]
        for counter in wrestlermoves:
            print('  ' + counter)

    elif userfighterpick == 'Balanced':
        selectedplayervar[3] = balancedmovespower[0]
        selectedplayervar[4] = balancedmovespower[1]
        selectedplayervar[5] = balancedmoves[0]
        selectedplayervar[6] = balancedmoves[1]
        for counter in balancedmoves:
            print('  ' + counter)

    elif userfighterpick == 'Striker':
        selectedplayervar[3] = strikermovespower[0]
        selectedplayervar[4] = strikermovespower[1]
        selectedplayervar[5] = strikermoves[0]
        selectedplayervar[6] = strikermoves[1]
        for counter in strikermoves:
            print('  ' + counter)
    else:
        print('Invalid command! Please pick wrestler, striker, or balanced')
    return selectedplayervar


def computerplayerstatsselection():
    computerpicknumber = random.randint(0, 2)
    computerplayerstats[0] = fightertypehealth[computerpicknumber]
    computerplayerstats[1] = fightertype[computerpicknumber]
    print('Computer picks ' + fightertype[computerpicknumber])
    if computerpicknumber == 0:
        computerplayerstats[2] = wrestlermoves[0]
        computerplayerstats[3] = wrestlermoves[1]
        computerplayerstats[4] = wrestlermovespower[0]
        computerplayerstats[5] = wrestlermovespower[1]
    elif computerpicknumber == 1:
        computerplayerstats[2] = balancedmoves[0]
        computerplayerstats[3] = balancedmoves[1]
        computerplayerstats[4] = balancedmovespower[0]
        computerplayerstats[5] = balancedmovespower[1]
    elif computerpicknumber == 2:
        computerplayerstats[2] = strikermoves[0]
        computerplayerstats[3] = strikermoves[1]
        computerplayerstats[4] = strikermovespower[0]
        computerplayerstats[5] = strikermovespower[1]
    return computerplayerstats


print('Welcome to FIGHTER CLUB to play. This program will let you select a player and play game.')
while flag == True:
    showMenu()
    userChoice = getChoice()

    if userChoice == 'H':
        showHelp()
    elif userChoice == 'Q':  # control the loop with the variable flag
        flag = False
    elif userChoice == 'P':
        userfighterpick = input('Select your fighter (Having trouble picking a fighter press 0): ')
        userfighterpick = userfighterpick.capitalize()
        if fightertype.count(userfighterpick) != 0:
            selectedplayervar = selectedplayerfunction(userfighterpick)
            health = selectedplayervar[0]
            hitprobability = selectedplayervar[2]
            move1hitpower = selectedplayervar[3]
            move2hitpower = selectedplayervar[4]
            fightermove1 = selectedplayervar[5]
            fightermove2 = selectedplayervar[6]

            thirdflag = True
            fourthflag = True
            secondflag = True
            wins = 0
            computerwins = 0
            playerwins = 0
            totalgames = 0
            losses = 0
            while thirdflag == True:
                userpickaction = input('Choose to fight or train: ')
                userpickaction = userpickaction.capitalize()
                if userpickaction == 'Train':
                    if numberoftrainingsessions <= 3:
                        for trainingsessions in range(1, 4):
                            numberoftrainingsessions = numberoftrainingsessions + 1
                            usertrainingitem = input(
                                'Do you want to work on ' + fightermove1 + ' or ' + fightermove2 + ': ')
                            usertrainingitem = usertrainingitem.capitalize()
                            if usertrainingitem == fightermove1:
                                move1hitpower = move1hitpower + random.randint(1, 5)
                                print('Your hitpower for ' + fightermove1 + ' increased to: ' + str(move1hitpower))
                            elif usertrainingitem == fightermove2:
                                move2hitpower = move2hitpower + random.randint(1, 5)
                                print('Your hitpower for ' + fightermove2 + ' increased to: ' + str(move2hitpower))
                            print('Number of Training Sessions: ' + str(trainingsessions))

                    else:
                        print('No more training sessions available')
                elif userpickaction == 'Fight':
                    print('THIS IS FIGHT CLUB!')
                    computerplayerstats = computerplayerstatsselection()

                    computerhealth = computerplayerstats[0]
                    computerpickfighter = computerplayerstats[1]
                    computermove1 = computerplayerstats[2]
                    computermove2 = computerplayerstats[3]
                    computermove1power = computerplayerstats[4]
                    computermove2power = computerplayerstats[5]

                    while secondflag == True:

                        while fourthflag == True:

                            print('**** TIME to FIGHT!!****')

                            useraction = input('Choose ' + fightermove1 + ' or ' + fightermove2 + ' : ')
                            useraction = useraction.capitalize()

                            if useraction == fightermove1:
                                print('You have chose to ' + fightermove1)
                            elif useraction == fightermove2:
                                print('You have chose to ' + fightermove2)

                            hitmissratio = random.randint(1, 10)

                            if hitmissratio <= hitprobability:

                                if useraction == fightermove1:
                                    computerhealth = computerhealth - move1hitpower
                                    computerhealth = str(computerhealth)
                                    print('Computer Health: ' + computerhealth)
                                    computerhealth = int(computerhealth)

                                elif useraction == fightermove2:
                                    computerhealth = computerhealth - move2hitpower
                                    computerhealth = str(computerhealth)
                                    print('Computer Health: ' + computerhealth)
                                    computerhealth = int(computerhealth)

                            elif hitmissratio > hitprobability:
                                print('COMPUTER TURN TO CHOSE')

                                if useraction == fightermove1:
                                    computerhealth = computerhealth
                                    computerhealth = str(computerhealth)
                                    print('Computer Health: ' + computerhealth)
                                    print('****Nothing happened!!!!!****')
                                    computerhealth = int(computerhealth)

                                elif useraction == fightermove2:
                                    computerhealth = computerhealth
                                    computerhealth = str(computerhealth)
                                    print('Computer Health: ' + computerhealth)
                                    print('****Nothing happened!!!!!****')
                                    computerhealth = int(computerhealth)

                            # print('COMPUTER TURN TO CHOSE')

                            computernumber = random.randint(1, 2)

                            if computernumber == 1:
                                print('Computer chose: ' + computermove1)
                                computermove = computermove1
                            elif computernumber == 2:
                                print('Computer chose: ' + computermove2)
                                computermove = computermove2

                            computerhitmissratio = random.randint(1, 10)

                            if computerhitmissratio <= hitprobability:

                                if computermove == computermove1:
                                    health = health - computermove1power
                                    health = str(health)
                                    print('Player Health: ' + health)
                                    health = int(health)

                                elif computermove == computermove2:
                                    health = health - computermove2power
                                    health = str(health)
                                    print('Player Health: ' + health)
                                    health = int(health)

                            elif computerhitmissratio > hitprobability:

                                if computermove == computermove1:
                                    health = health
                                    health = str(health)
                                    print('Player Health: ' + health)
                                    print('****Nothing happened!!!!!****')
                                    health = int(health)

                                elif computermove == computermove2:
                                    health = health
                                    health = str(health)
                                    print('Player Health: ' + health)
                                    print('****Nothing happened!!!!!****')
                                    health = int(health)

                            if computerhealth <= 0:
                                # print('Player has won! game')
                                wins = wins + 1
                                totalgames = wins + losses
                                print('Player has won! game:' + str(totalgames))
                                playerwins = playerwins + 1
                                print('You have won so far ' + str(playerwins) + ' games.')
                                wins = int(wins)
                                fourthflag = False
                            elif health <= 0:
                                # print('Computer has won!')
                                losses = losses + 1
                                totalgames = wins + losses
                                print('Computer has won! game:' + str(totalgames))
                                computerwins = computerwins + 1
                                print('Computer have won so far ' + str(computerwins) + ' games.')
                                computerwins = int(computerwins)
                                fourthflag = False
                            elif health <= 0 and computerhealth <= 0:
                                print('It is a tie')
                                fourthflag = False

                        computerpickindex = fightertype.index(computerpickfighter)
                        computerfullhealth = fightertypehealth[computerpickindex]
                        computerhealth = computerfullhealth

                        playerpickindex = fightertype.index(selectedplayervar[1])
                        playerfullhealth = fightertypehealth[playerpickindex]
                        health = playerfullhealth

                        # totalgames = wins + losses

                        if totalgames == 3 or computerwins == 2 or playerwins == 2:
                            if playerwins >= 2:
                                print('****Congratulations! Your going to the Hall of Fame.****')
                                secondflag = False
                                thirdflag = False
                            else:
                                print('****Do not giveup! Try again. Better Luck next time****')
                                fourthflag = False
                                secondflag = False
                                thirdflag = False
                        else:
                            print('More Fight!!!!. Get Ready for Game:' + str(totalgames + 1))
                            fourthflag = True

                else:
                    print('Invalid Command! Fight or Train option!')

    elif userChoice == 'S':
        showPlayerstats()
    else:
        print('Not a valid choice. Only S, Q, H, or P are valid choices')  # error message

print('Thank you for Playing!')