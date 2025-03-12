import random
import os
import time
import sys
import yaml
from collections import Counter
from datetime import datetime

# Use a more secure random number generator
system_random = random.SystemRandom()

# Unicode symbols for card suits
SUIT_SYMBOLS = {
    "Clubs": "♣",
    "Hearts": "♥",
    "Spades": "♠",
    "Diamonds": "♦"
}

# Unicode colors (ANSI escape codes)
RED = "\033[91m"
BLACK = "\033[30m"
RESET = "\033[0m"

# Add YAML file path
RESULTS_FILE = "poker_results.yaml"

def pick_a_card(system_random):
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
    suits = ["Clubs", "Hearts", "Spades", "Diamonds"]
    
    # Use system_random for better randomness
    rank = system_random.choice(ranks)
    suit = system_random.choice(suits)
    return f"{rank} of {suit}"

def format_card(card):
    """Format a card with Unicode symbols"""
    parts = card.split(" of ")
    rank = parts[0]
    suit = parts[1]
    
    # Abbreviate face cards
    if rank == "Jack":
        rank = "J"
    elif rank == "Queen":
        rank = "Q"
    elif rank == "King":
        rank = "K"
    elif rank == "Ace":
        rank = "A"
    
    # Add color based on suit
    symbol = SUIT_SYMBOLS[suit]
    color = RED if suit in ["Hearts", "Diamonds"] else BLACK
    
    # Return formatted card
    return f"{rank}{color}{symbol}{RESET}"

def deal_hand(system_random):
    return [pick_a_card(system_random), pick_a_card(system_random)]

def deal_flop(system_random):
    return [pick_a_card(system_random) for _ in range(3)]

def deal_turn_or_river(system_random):
    return pick_a_card(system_random)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_for_confirmation(message="Press Enter when ready to proceed...", clear=True):
    input(message)
    if clear:
        clear_screen()

def get_card_value(card):
    # Extract rank from card string
    rank = card.split(" of ")[0]
    # Convert rank to numeric value
    rank_values = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, 
                  "9": 9, "10": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
    return rank_values.get(rank, 0)

def get_card_suit(card):
    return card.split(" of ")[1]

def evaluate_hand(player_hand, community_cards):
    # Combine player's hand with community cards
    all_cards = player_hand + community_cards
    
    # Extract ranks and suits
    ranks = [get_card_value(card) for card in all_cards]
    suits = [get_card_suit(card) for card in all_cards]
    
    # Count occurrences of each rank and suit
    rank_counts = Counter(ranks)
    suit_counts = Counter(suits)
    
    # Sort ranks in descending order for high card and straight detection
    sorted_ranks = sorted(ranks, reverse=True)
    
    # Check for flush (5 or more cards of the same suit)
    flush = any(count >= 5 for count in suit_counts.values())
    
    # Check for straight (5 consecutive ranks)
    # First, remove duplicates and sort
    unique_ranks = sorted(set(ranks), reverse=True)
    straight = False
    
    # Check for regular straights (including Broadway A-K-Q-J-10)
    for i in range(len(unique_ranks) - 4):
        if unique_ranks[i] - unique_ranks[i+4] == 4:
            straight = True
            break
    
    # Special case for A-5 straight (Ace can be low)
    if set([14, 2, 3, 4, 5]).issubset(set(ranks)):
        straight = True
    
    # Count pairs, three of a kind, four of a kind
    pairs = sum(1 for count in rank_counts.values() if count == 2)
    three_of_a_kind = any(count == 3 for count in rank_counts.values())
    four_of_a_kind = any(count == 4 for count in rank_counts.values())
    
    # Check for two pair flush - both pairs have the same suit
    two_pair_flush = False
    if pairs >= 2:
        # Group cards by rank and suit
        rank_suit_counts = Counter([(get_card_value(card), get_card_suit(card)) for card in all_cards])
        # Find pairs
        pair_ranks = [rank for rank, count in rank_counts.items() if count >= 2]
        if len(pair_ranks) >= 2:
            # Check if the top two pairs have the same suit
            pair_suits = {}
            for rank in sorted(pair_ranks, reverse=True)[:2]:
                for card in all_cards:
                    if get_card_value(card) == rank:
                        suit = get_card_suit(card)
                        if rank not in pair_suits:
                            pair_suits[rank] = suit
                        elif pair_suits[rank] != suit:
                            # Found a card of this rank with a different suit
                            pair_suits[rank] = None
            
            # Check if both pairs have the same non-None suit
            suits_list = [suit for suit in pair_suits.values() if suit is not None]
            if len(suits_list) == 2 and suits_list[0] == suits_list[1]:
                two_pair_flush = True
    
    # Check for flushed threes - three of a kind with the same suit
    flushed_threes = False
    if three_of_a_kind:
        # Find ranks with at least 3 cards
        three_ranks = [rank for rank, count in rank_counts.items() if count >= 3]
        for rank in three_ranks:
            # Count suits for this rank
            rank_suits = [get_card_suit(card) for card in all_cards if get_card_value(card) == rank]
            suit_counter = Counter(rank_suits)
            # If any suit appears 3 or more times, we have flushed threes
            if any(count >= 3 for count in suit_counter.values()):
                flushed_threes = True
                break
    
    # Check for flush with pair - a flush where at least one rank appears twice
    flush_with_pair = False
    if flush:
        # Find the most common suit
        most_common_suit = max(suit_counts.items(), key=lambda x: x[1])[0]
        # Get all cards of that suit
        flush_cards = [card for card in all_cards if get_card_suit(card) == most_common_suit]
        # Count ranks within the flush
        flush_ranks = [get_card_value(card) for card in flush_cards]
        flush_rank_counts = Counter(flush_ranks)
        # Check if any rank appears at least twice
        if any(count >= 2 for count in flush_rank_counts.values()):
            flush_with_pair = True
    
    # Determine hand type and score based on the probability results
    # Hand types (higher is better):
    # 12: Straight Flush (0.1870%)
    # 11: Two Pair Flush (0.4360%)
    # 10: Flushed Threes (0.9740%)
    # 9: Four of a Kind (1.2930%)
    # 8: Full House (5.4000%)
    # 7: Flush with Pair (2.2340%)
    # 6: Flush (1.9660%)
    # 5: Straight (3.6270%)
    # 4: Three of a Kind (7.8590%)
    # 3: Two Pair (27.0240%)
    # 2: One Pair (37.4730%)
    # 1: High Card (11.5270%)
    
    if straight and flush:
        hand_type = 12  # Straight Flush
    elif two_pair_flush:
        hand_type = 11  # Two Pair Flush
    elif flushed_threes:
        hand_type = 10  # Flushed Threes
    elif four_of_a_kind:
        hand_type = 9   # Four of a Kind
    elif three_of_a_kind and pairs >= 1:
        hand_type = 8   # Full House
    elif flush_with_pair:
        hand_type = 7   # Flush with Pair
    elif flush:
        hand_type = 6   # Flush
    elif straight:
        hand_type = 5   # Straight
    elif three_of_a_kind:
        hand_type = 4   # Three of a Kind
    elif pairs >= 2:
        hand_type = 3   # Two Pair
    elif pairs == 1:
        hand_type = 2   # One Pair
    else:
        hand_type = 1   # High Card
    
    # For tiebreakers, use the highest cards involved in the hand
    return (hand_type, sorted_ranks[:5])

def get_hand_name(hand_value):
    hand_types = {
        12: "Straight Flush",
        11: "Two Pair Flush",
        10: "Flushed Threes",
        9: "Four of a Kind",
        8: "Full House",
        7: "Flush with Pair",
        6: "Flush",
        5: "Straight",
        4: "Three of a Kind",
        3: "Two Pair",
        2: "One Pair",
        1: "High Card"
    }
    return hand_types.get(hand_value[0], "Unknown Hand")

def get_best_hand_cards(player_hand, community_cards):
    """Return the 5 cards that form the best hand for a player"""
    all_cards = player_hand + community_cards
    
    # Extract ranks and suits
    card_info = [(card, get_card_value(card), get_card_suit(card)) for card in all_cards]
    
    # Count occurrences of each rank and suit
    rank_counts = Counter([info[1] for info in card_info])
    suit_counts = Counter([info[2] for info in card_info])
    
    # Group cards by rank for easier access
    cards_by_rank = {}
    for card, rank_val, _ in card_info:
        if rank_val not in cards_by_rank:
            cards_by_rank[rank_val] = []
        cards_by_rank[rank_val].append(card)
    
    # Group cards by suit for flush detection
    cards_by_suit = {}
    for card, _, suit in card_info:
        if suit not in cards_by_suit:
            cards_by_suit[suit] = []
        cards_by_suit[suit].append(card)
    
    # Check for flush with pair
    flush_with_pair_cards = None
    for suit, cards in cards_by_suit.items():
        if len(cards) >= 5:
            # We have a flush, now check for pairs within the flush
            flush_ranks = [get_card_value(card) for card in cards]
            flush_rank_counts = Counter(flush_ranks)
            pair_ranks = [rank for rank, count in flush_rank_counts.items() if count >= 2]
            
            if pair_ranks:
                # We have at least one pair in the flush
                # Sort pair ranks by value (highest first)
                pair_ranks.sort(reverse=True)
                # Get the highest pair
                pair_rank = pair_ranks[0]
                
                # Get the pair cards
                pair_cards = [card for card in cards if get_card_value(card) == pair_rank][:2]
                
                # Get the remaining highest cards from the flush
                remaining_cards = [card for card in cards if get_card_value(card) != pair_rank]
                remaining_cards.sort(key=get_card_value, reverse=True)
                
                # Combine to form the 5-card hand
                flush_with_pair_cards = pair_cards + remaining_cards[:3]
                break
    
    # Check for flush
    flush_cards = None
    for suit, cards in cards_by_suit.items():
        if len(cards) >= 5:
            # Sort flush cards by rank (highest first)
            flush_cards = sorted(cards, key=get_card_value, reverse=True)[:5]
            break
    
    # Check for straight
    straight_cards = None
    ranks = sorted(set(rank_counts.keys()), reverse=True)
    for i in range(len(ranks) - 4):
        if ranks[i] - ranks[i+4] == 4:
            straight_ranks = ranks[i:i+5]
            straight_cards = []
            for rank in straight_ranks:
                straight_cards.append(cards_by_rank[rank][0])
            break
    
    # Check for A-5 straight
    if not straight_cards and 14 in ranks and all(r in ranks for r in [2, 3, 4, 5]):
        straight_ranks = [5, 4, 3, 2, 14]  # 5-high straight with Ace low
        straight_cards = []
        for rank in straight_ranks:
            straight_cards.append(cards_by_rank[rank][0])
    
    # Check for straight flush
    straight_flush_cards = None
    if flush_cards and straight_cards:
        # Check if the flush cards form a straight
        flush_ranks = sorted(set(get_card_value(card) for card in flush_cards), reverse=True)
        for i in range(len(flush_ranks) - 4):
            if flush_ranks[i] - flush_ranks[i+4] == 4:
                straight_flush_ranks = flush_ranks[i:i+5]
                straight_flush_cards = []
                for rank in straight_flush_ranks:
                    for card in flush_cards:
                        if get_card_value(card) == rank:
                            straight_flush_cards.append(card)
                            break
                break
    
    # Four of a kind
    four_of_a_kind = None
    for rank, count in rank_counts.items():
        if count >= 4:
            four_cards = cards_by_rank[rank][:4]
            # Add highest kicker
            kickers = [card for card, r, _ in card_info if r != rank]
            kickers.sort(key=get_card_value, reverse=True)
            four_of_a_kind = four_cards + kickers[:1]
            break
    
    # Full house
    full_house = None
    three_rank = None
    pair_rank = None
    
    # Find highest three of a kind
    for rank, count in sorted(rank_counts.items(), reverse=True):
        if count >= 3:
            three_rank = rank
            break
    
    # Find highest pair different from three of a kind
    if three_rank is not None:
        for rank, count in sorted(rank_counts.items(), reverse=True):
            if count >= 2 and rank != three_rank:
                pair_rank = rank
                break
    
    if three_rank is not None and pair_rank is not None:
        three_cards = cards_by_rank[three_rank][:3]
        pair_cards = cards_by_rank[pair_rank][:2]
        full_house = three_cards + pair_cards
    
    # Three of a kind
    three_of_a_kind = None
    three_ranks = [rank for rank, count in rank_counts.items() if count >= 3]
    if three_ranks:
        # Take the highest three of a kind
        three_rank = max(three_ranks)
        three_cards = cards_by_rank[three_rank][:3]
        # Add two highest kickers
        kickers = [card for card, r, _ in card_info if r != three_rank]
        kickers.sort(key=get_card_value, reverse=True)
        three_of_a_kind = three_cards + kickers[:2]
    
    # Two pair
    two_pair = None
    pair_ranks = [rank for rank, count in sorted(rank_counts.items(), reverse=True) if count >= 2]
    if len(pair_ranks) >= 2:
        # Take the two highest pairs
        pair1_cards = cards_by_rank[pair_ranks[0]][:2]
        pair2_cards = cards_by_rank[pair_ranks[1]][:2]
        # Add highest kicker
        kickers = [card for card, r, _ in card_info 
                  if r != pair_ranks[0] and r != pair_ranks[1]]
        kickers.sort(key=get_card_value, reverse=True)
        two_pair = pair1_cards + pair2_cards
        if kickers:
            two_pair.append(kickers[0])
    
    # One pair
    one_pair = None
    if pair_ranks and two_pair is None:
        pair_cards = cards_by_rank[pair_ranks[0]][:2]
        # Add three highest kickers
        kickers = [card for card, r, _ in card_info if r != pair_ranks[0]]
        kickers.sort(key=get_card_value, reverse=True)
        one_pair = pair_cards + kickers[:3]
    
    # High card - take the 5 highest cards
    high_card = sorted([card for card, _, _ in card_info], key=get_card_value, reverse=True)[:5]
    
    # Return the best hand (always 5 cards)
    if straight_flush_cards:
        return straight_flush_cards
    elif four_of_a_kind:
        return four_of_a_kind
    elif full_house:
        return full_house
    elif flush_with_pair_cards:
        return flush_with_pair_cards
    elif flush_cards:
        return flush_cards
    elif straight_cards:
        return straight_cards
    elif three_of_a_kind:
        return three_of_a_kind
    elif two_pair:
        return two_pair
    elif one_pair:
        return one_pair
    else:
        return high_card

def load_previous_players():
    """Load previous player names from the results file"""
    if not os.path.exists(RESULTS_FILE):
        return ["Silas", "Aria", "Asher"]  # Default if no file exists
    
    try:
        with open(RESULTS_FILE, 'r') as file:
            data = yaml.safe_load(file)
            if data and 'games' in data and data['games']:
                # Get the most recent game
                latest_game = data['games'][-1]
                if 'players' in latest_game:
                    return latest_game['players']
    except Exception as e:
        print(f"Error loading previous players: {e}")
    
    # Return defaults if anything goes wrong
    return ["Silas", "Aria", "Asher"]

def get_unicode_card(card):
    """Convert a card string to its Unicode representation"""
    # Extract rank and suit
    parts = card.split(" of ")
    if len(parts) != 2:
        return card  # Return original if format is unexpected
    
    rank, suit = parts
    
    # Map ranks to Unicode symbols
    rank_map = {
        "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", "10": "10",
        "Jack": "J", "Queen": "Q", "King": "K", "Ace": "A"
    }
    
    # Map suits to Unicode symbols
    suit_map = {
        "Clubs": "♣", "Hearts": "♥", "Spades": "♠", "Diamonds": "♦"
    }
    
    # Get Unicode representations
    unicode_rank = rank_map.get(rank, rank)
    unicode_suit = suit_map.get(suit, suit)
    
    # Combine into Unicode card
    return f"{unicode_rank}{unicode_suit}"

def save_game_results(players, winner, hand_type, seed, community_cards, player_hands):
    """Save game results to YAML file"""
    # Create a timestamp for the game
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Format the game result
    game_result = {
        'timestamp': timestamp,
        'seed': seed,
        'players': players,
        'winner': winner,
        'winning_hand': hand_type,
        'community_cards': [card for card in community_cards],  # Store raw cards
        'player_hands': {player: [card for card in hand] for player, hand in zip(players, player_hands)}
    }
    
    # Load existing data or create new structure
    if os.path.exists(RESULTS_FILE):
        try:
            with open(RESULTS_FILE, 'r') as file:
                data = yaml.safe_load(file) or {'games': []}
        except Exception as e:
            print(f"Error loading results file: {e}")
            data = {'games': []}
    else:
        data = {'games': []}
    
    # Add the new game result
    data['games'].append(game_result)
    
    # Save the updated data
    try:
        with open(RESULTS_FILE, 'w') as file:
            yaml.dump(data, file, default_flow_style=False)
        print(f"Game results saved to {RESULTS_FILE}")
    except Exception as e:
        print(f"Error saving results: {e}")

def texas_holdem(seed=None):
    # Initialize random number generator with seed if provided
    if seed is None:
        # Generate a random seed if none provided
        seed = int(time.time() * 1000) & 0xFFFFFFFF
    
    # Set the seed for reproducibility
    random.seed(seed)
    system_random = random.Random(seed)
    
    print(f"Welcome to Texas Hold 'Em! (Seed: {seed})\n")
    
    # Load previous players as defaults
    default_players = load_previous_players()
    
    # Ask for player names in a single comma-separated input
    while True:
        # If we have previous players, offer them as defaults
        if os.path.exists(RESULTS_FILE):
            default_players_str = ", ".join(default_players)
            player_input = input(f"Enter player names (comma-separated) or press Enter for default players [{default_players_str}]: ").strip()
            
            # Use default names if input is empty
            if not player_input:
                player_names = default_players
                print(f"Using default players: {default_players_str}")
                break
        else:
            # No results file, so require player names
            player_input = input("Enter player names (comma-separated, e.g., 'Alice, Bob, Charlie'): ").strip()
            
            # Don't allow empty input when no defaults are available
            if not player_input:
                print("Please enter at least 2 player names.")
                continue
        
        player_names = [name.strip() for name in player_input.split(',') if name.strip()]
        
        if len(player_names) < 2:
            print("We need at least 2 players to start. Please enter at least 2 names.")
            continue
        elif len(player_names) > 10:
            print("Maximum 10 players allowed. Please enter 10 or fewer names.")
            continue
        else:
            break
    
    print(f"\nGreat! We have {len(player_names)} players: {', '.join(player_names)}")
    
    # Deal hands to all players
    hands = []
    for name in player_names:
        input(f"{name}, press Enter to receive your hand.")
        player_hand = deal_hand(system_random)
        hands.append(player_hand)
        clear_screen()
        print(f"{name}'s hand:")
        print("\n".join([format_card(card) for card in player_hand]))
        wait_for_confirmation()
    
    # Initialize community cards
    community_cards = []
    
    # Dealing the Flop
    wait_for_confirmation("Press Enter to deal the flop.")
    flop = deal_flop(system_random)
    community_cards.extend(flop)
    print("Community Cards:")
    print(" ".join([format_card(card) for card in community_cards]))

    # Dealing the Turn
    wait_for_confirmation("Press Enter to deal the turn.")
    turn = deal_turn_or_river(system_random)
    community_cards.append(turn)
    print("Community Cards:")
    print(" ".join([format_card(card) for card in community_cards]))

    # Dealing the River
    wait_for_confirmation("Press Enter to deal the river.")
    river = deal_turn_or_river(system_random)
    community_cards.append(river)
    print("Community Cards:")
    print(" ".join([format_card(card) for card in community_cards]))
    wait_for_confirmation()

    # Show final results
    print("GAME RESULTS\n")
    print("Community Cards:")
    formatted_community_cards = " ".join([format_card(card) for card in community_cards])
    print(formatted_community_cards)
    print("\nPlayer Hands:")
    
    # Evaluate each player's hand
    scores = []
    best_hands = []
    for i, (name, hand) in enumerate(zip(player_names, hands)):
        hand_value = evaluate_hand(hand, community_cards)
        hand_name = get_hand_name(hand_value)
        best_five_cards = get_best_hand_cards(hand, community_cards)
        
        # Ensure we have exactly 5 cards in the best hand
        if len(best_five_cards) < 5:
            # If we don't have 5 cards, add high cards from remaining cards
            all_cards = hand + community_cards
            remaining_cards = [card for card in all_cards if card not in best_five_cards]
            remaining_cards.sort(key=get_card_value, reverse=True)
            best_five_cards.extend(remaining_cards[:5-len(best_five_cards)])
        
        formatted_hand = f"{format_card(hand[0])} {format_card(hand[1])}"
        formatted_best_hand = " ".join([format_card(card) for card in best_five_cards[:5]])
        
        print(f"{name}: {formatted_hand}")
        print(f"Best hand: {hand_name}")
        print(f"Cards: {formatted_best_hand}")
        print()
        
        scores.append((name, hand_value, hand_name))
        best_hands.append(formatted_best_hand)
    
    # Determine winner based on highest hand value
    winner_name, winner_hand_value, winner_hand_name = max(scores, key=lambda x: x[1])
    print(f"\nAnd the winner is... {winner_name} with a {winner_hand_name}!")
    
    # Save game results
    save_game_results(
        player_names, 
        winner_name, 
        winner_hand_name, 
        seed,
        [card for card in community_cards],  # Store raw cards
        [[card for card in hand] for hand in hands]  # Store raw hands
    )
    
    print(f"\nGame Over! (Seed: {seed})")
    return seed

def calculate_hand_probabilities(num_simulations=100000, seed=None):
    """
    Calculate the probabilities of each hand type through simulation.
    
    Args:
        num_simulations: Number of hands to simulate
        seed: Random seed for reproducibility
        
    Returns:
        Dictionary with hand types and their probabilities
    """
    if seed is None:
        # Generate a random seed if none provided
        seed = int(time.time() * 1000) & 0xFFFFFFFF
    
    # Set the seed for reproducibility
    random.seed(seed)
    system_random = random.Random(seed)
    
    print(f"Calculating probabilities over {num_simulations} simulations (Seed: {seed})...")
    
    # Counter for each hand type
    hand_counts = Counter()
    
    for _ in range(num_simulations):
        # Deal a random hand and community cards
        player_hand = deal_hand(system_random)
        community_cards = deal_flop(system_random) + [deal_turn_or_river(system_random), deal_turn_or_river(system_random)]
        
        # Evaluate the hand
        hand_value = evaluate_hand(player_hand, community_cards)
        hand_type = hand_value[0]  # Just the hand type, not the tiebreaker
        
        # Count this hand type
        hand_counts[hand_type] += 1
    
    # Calculate probabilities
    probabilities = {}
    for hand_type, count in sorted(hand_counts.items(), reverse=True):
        hand_name = get_hand_name((hand_type, []))
        probability = count / num_simulations * 100
        probabilities[hand_name] = probability
    
    return probabilities, seed

def print_hand_probabilities(seed=None):
    """Print the probabilities of each hand type in a nice format."""
    probabilities, used_seed = calculate_hand_probabilities(seed=seed)
    
    print("\nPOKER HAND PROBABILITIES")
    print("========================")
    print(f"{'Hand Type':<20} {'Probability (%)':<15}")
    print("-" * 35)
    
    for hand_name, probability in probabilities.items():
        print(f"{hand_name:<20} {probability:.4f}%")
    
    print("\nNote: These probabilities are specific to this variant of poker where duplicates are allowed.")
    print(f"Seed used: {used_seed}")

if __name__ == "__main__":
    # Parse command line arguments
    seed = None
    calc_probabilities = False
    
    i = 1
    while i < len(sys.argv):
        if sys.argv[i] == "--calc-probabilities":
            calc_probabilities = True
        elif sys.argv[i] == "--seed" and i + 1 < len(sys.argv):
            try:
                seed = int(sys.argv[i + 1])
                i += 1  # Skip the next argument since we've processed it
            except ValueError:
                print(f"Error: Invalid seed value '{sys.argv[i + 1]}'. Using random seed.")
        i += 1
    
    if calc_probabilities:
        print_hand_probabilities(seed)
    else:
        texas_holdem(seed)
