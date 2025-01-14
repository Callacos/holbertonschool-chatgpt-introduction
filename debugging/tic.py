def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Vérifier les lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Vérifier les colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Vérifier la diagonale principale
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    # Vérifier la diagonale secondaire
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_full(board):
    """
    Vérifie si le plateau est plein.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)

        # Gestion des entrées
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
            if row not in range(3) or col not in range(3):
                print("Invalid input! Please enter a number between 0 and 2.")
                continue
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        # Vérifier si la case est vide
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Faire le mouvement
        board[row][col] = player

        # Vérifier si le joueur actuel gagne
        if check_winner(board):
            print_board(board)
            print(f"Player {player} wins!")
            break

        # Vérifier s'il y a un match nul
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Changer de joueur
        player = "O" if player == "X" else "X"

if __name__ == "__main__":
    while True:
        tic_tac_toe()
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay != "yes":
            print("Thanks for playing!")
            break
