class Card:

    def __init__(self,suit,rank):

        if rank in {"J","Q","K"}:
            self.rank = 10
        elif rank=="A":
            self.rank = 11
        else:
            self.rank = int(rank)

        self.suit = suit

        
        
