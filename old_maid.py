"""
Old Maid Card Game
------------------
Description: A simple text-based Old Maid game for one player vs. computer.
"""

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    
    try:
        input("\nPress enter to continue. ")
        print()
    except SyntaxError:
        pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    
    deck = []
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663')  # remove a queen as the game requires
    return deck


def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck
    '''
    
    random.shuffle(deck)


def deal_cards(deck):
    '''(list of str)-> tuple of (list of str,list of str)

    Returns two lists representing two decks that are obtained
    after the dealer deals the cards from the given deck.
    The first list represents dealer's i.e. computer's deck
    and the second represents the other player's i.e user's list.
    '''
    
    dealer = []
    other = []

    for i in range(len(deck)):
        if i % 2 == 0:
            dealer.append(deck[i])
        else:
            other.append(deck[i])

    return (dealer, other)


def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled
    '''

    no_pairs = []

    copy_l = l[:]
    rank = []

    for c in copy_l:
        if len(c) == 3:
            rank.append(c[:2])
        else:
            rank.append(c[0])

    no_pairs = []
    already_kept = []

    for i in range(len(copy_l)):
        current_rank = rank[i]

        count = 0
        for j in range(len(rank)):
            if rank[j] == current_rank:
                count = count + 1

        if count % 2 == 1:
            if current_rank not in already_kept:
                no_pairs.append(copy_l[i])
                already_kept.append(current_rank)

    random.shuffle(no_pairs)
    return no_pairs


def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    for c in deck:
        print(c, end=' ')


def get_valid_input(n):
    '''
    (int)->int
    Returns an integer given by the user that is at least 1 and at most n.
    Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]

    Precondition: n>=1
    '''
    
    data = input(f"Give me an integer between 1 and {n}: ").strip()
    while True:
        try:
            data_int = int(data)
            if 1 <= data_int <= n:
                return data_int
            else:
                data = input(f"Invalid number. Give me an integer between 1 and {n}: ").strip()
        except ValueError:
            data = input(f"Invalid input. Give me an integer between 1 and {n}: ").strip()


def play_game():
    '''()->None
    This function plays the game'''

    deck = make_deck()
    shuffle_deck(deck)
    tmp = deal_cards(deck)

    dealer = tmp[0]
    human = tmp[1]

    print("Hello. My name is Robot and I am the dealer.")
    print("Welcome to my card game!")
    print("Your current deck of cards is:")
    print()
    print_deck(human)
    print()
    print()
    print("Do not worry. I cannot see the order of your cards")

    print("Now discard all the pairs from your deck. I will do the same.")
    wait_for_player()

    dealer = remove_pairs(dealer)
    human = remove_pairs(human)

    turn = 1  # human's turn
    while len(dealer) > 0 and len(human) > 0:
        if turn == 1:
            print("***********************************************************")
            print("Your turn.")
            print()
            print("Your current deck of cards is:")
            print()
            print_deck(human)
            print()
            print()
            print(
                f"I have {len(dealer)} cards. If 1 stands for my first card and\n{len(dealer)} for my last card, which of my cards would you like?")
            position = get_valid_input(len(dealer)) - 1
            print(f"You asked for my {position + 1}th card.")
            chosen_card = dealer.pop(position)
            print(f"Here it is. It is {chosen_card}")
            human.append(chosen_card)
            print()
            print(f"With {chosen_card} added, your current deck of cards is:")
            print()
            print_deck(human)
            human = remove_pairs(human)
            print()
            print()
            print("And after discarding pairs and shuffling, your deck is:")
            print()
            print_deck(human)
            print()
            wait_for_player()
            turn = 0  # robot's turn
            print()

        else:
            print("***********************************************************")
            print("My turn.")
            print()
            index = random.randint(1, len(human))
            english_number = ["st", "nd", "rd", "th"]
            if index > 3:
                ord_index = 3
            else:
                ord_index = index - 1
            print(f"I took your {index}{english_number[ord_index]} card.")
            chosen_card = human.pop(index - 1)
            dealer.append(chosen_card)
            dealer = remove_pairs(dealer)
            wait_for_player()
            turn = 1

    if len(dealer) == 0:
        print("Ups. I do not have any more cards\nYou lost! I, Robot, win")
    else:
        print("***********************************************************")
        print("Ups. You do not have any more cards\nCongratulations! You, Human, win")


play_game()
