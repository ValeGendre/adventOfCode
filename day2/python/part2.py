
class Move:
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

class OpponentMove:
    ROCK = 'A'
    PAPER = 'B'
    SCISSOR = 'C'

class YourMove:
    LOSE = 'X'
    NULL = 'Y'
    WIN = 'Z'

class Result:
    LOSE = 0
    NULL = 3
    WIN = 6

def score(moves):
    move1, move2 = moves
    if move1 == OpponentMove.ROCK and move2 == YourMove.LOSE: return Result.LOSE + Move.SCISSOR
    if move1 == OpponentMove.PAPER and move2 == YourMove.LOSE: return Result.LOSE + Move.ROCK
    if move1 == OpponentMove.SCISSOR and move2 == YourMove.LOSE: return Result.LOSE + Move.PAPER

    
    if move1 == OpponentMove.ROCK and move2 == YourMove.NULL: return Result.NULL + Move.ROCK
    if move1 == OpponentMove.PAPER and move2 == YourMove.NULL: return Result.NULL + Move.PAPER
    if move1 == OpponentMove.SCISSOR and move2 == YourMove.NULL: return Result.NULL + Move.SCISSOR

    
    if move1 == OpponentMove.ROCK and move2 == YourMove.WIN: return Result.WIN + Move.PAPER
    if move1 == OpponentMove.PAPER and move2 == YourMove.WIN: return Result.WIN + Move.SCISSOR
    if move1 == OpponentMove.SCISSOR and move2 == YourMove.WIN: return Result.WIN + Move.ROCK

with open('ressources/input.txt', encoding='utf-8') as f:
    lines = [line.split(' ') for line in ''.join(f.readlines()).split('\n')]

score_list = sum(map(score, lines))

print(score_list)