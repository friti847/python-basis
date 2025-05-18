import chess
import random

def print_board(board):
    print(board)

def player_move(board):
    while True:
        move = input("Введите ваш ход (вот пример, e2e4): ")
        try:
            chess_move = chess.Move.from_uci(move)
            if chess_move in board.legal_moves:
                board.push(chess_move)
                break
            else:
                print("Нелегальный ход. Попробуйте снова.")
        except:
            print("Неверный формат хода. Попробуйте снова.")

def computer_move(board):
    legal_moves = list(board.legal_moves)
    move = random.choice(legal_moves)
    board.push(move)
    print(f"Ход компьютера: {move}")

def main():
    board = chess.Board()
    print("Добро пожаловать в шахматы!")
    print_board(board)

    while not board.is_game_over():
        print("\nВаш ход:")
        player_move(board)
        print_board(board)

        if board.is_game_over():
            break

        print("\nХод компьютера:")
        computer_move(board)
        print_board(board)

    if board.is_checkmate():
        print("Мат!")
    elif board.is_stalemate():
        print("Пат!")
    elif board.is_insufficient_material():
        print("С твоими фигурами не победить!")
    else:
        print("Игра окончена.")

if __name__ == "__main__":
    main()