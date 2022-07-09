from Deck import Deck

class BlackJack:

    def __init__(self):
        self.deck = Deck()
        self.scores = {"Ace":1, "2":2, "3":3, "4":4, "5":5, "6":6,"7":7,"8":8,"9":9,"10":10, "Jack":10, "Queen":10, "King":10}

    def deal(self,players=2):

        # for p in range is 0 .. 1 not 0 .. 2
        hands =[[] for p in range(players)]

        #hands[0] = Player 1 hand
        #hands[1] = Player 2 hand

        for cards in range(0,2):
            for h in hands:
                h.append(self.deck.draw())
        return hands
   
    def calculate_values(self,hand):
        hand_value = 0
        ace = False
        for card in hand:

            # If we have an Ace in our hand its value is either 1 or 11.
            # We need to check to see what value it is, based upon if we are
            #  above or below total value of 21.
            if str(card.get_value()) =='Ace':
                ace = True
            hand_value += self.scores[card.get_value()]

        # Here we check to see if our Ace is 1 or 11.
        # If we would be above the value of 21 the value of Ace is 1, otherwise
        #  its value is 11.
        #
        # Handle value already has Ace value in it, that's why we only do a +10
        #  check here.
        if ace and ((hand_value +10) <22):
            hand_value+=10
        return hand_value

    def play(self,players):
        hands = self.deal(players)
        i=1
        for hand in hands:
            h_value = self.calculate_values(hand)
            print("Player " +str(i) +": "+ str(h_value))
            i+=1

