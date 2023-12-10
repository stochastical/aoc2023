from collections import Counter

with open('input.txt') as f:
    hand_to_bids: dict[str, int] = dict((l.split()[0], int(l.split()[1])) for l in f)
hand_to_bids

## Part 1

# weakest first
CARD_STRENGTHS: list[str] = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

# weakest first
KIND_STRENGTHS: list[tuple[int]] = [
    (1, 1, 1, 1, 1),  # 'High card'
    (2, 1, 1, 1),  # 'One pair'
    (2, 2, 1),  # 'Two pair'
    (3, 1, 1),  # 'Three of a kind'
    (3, 2),  # 'Full house'
    (4, 1),  # 'Four of a kind'
    (5,),  # 'Five of a kind'
]


def hand_kind(card: str) -> int:
    return KIND_STRENGTHS.index(tuple(sorted(Counter(card).values(), reverse=True)))


def rank_cards(hand_bids: dict[str, int]) -> list[str]:
    return sorted(
        [card for card in hand_bids],
        key=lambda card: [hand_kind(card)] + [CARD_STRENGTHS.index(c) for c in card],
    )


def calculate_winnings(hand_bids: dict[str, int]) -> int:
    return sum(
        [
            rank * hand_bids[hand]
            for rank, hand in enumerate(rank_cards(hand_bids), start=1)
        ]
    )


calculate_winnings(hand_to_bids)

## Part 2

# redefine card strengths (weakest first)
CARD_STRENGTHS: list[str] = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

def hand_kind(card: str) -> int:
    '''Return the highest kind that is the result of replacing every 'J' with every possible card'''
    return max(
        KIND_STRENGTHS.index(
            tuple(sorted(Counter(card.replace('J', strength)).values(), reverse=True))
        )
        for strength in CARD_STRENGTHS
    )

calculate_winnings(hand_to_bids)
