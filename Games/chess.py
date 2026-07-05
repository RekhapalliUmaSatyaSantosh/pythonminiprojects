def king():
    print("""
          ♔ KING MOVEMENT:
  
    • Can move 1 square in ANY direction
    • All 8 surrounding squares
    • Cannot move into check
    • Captures enemy pieces on adjacent squares
  
  Example from e4:
    . . . . .
    . . ♔ . .
    . ♔ . ♔ .
    . . ♔ . .
    . . . . .""")
def queen():
    print("""
  ♕ QUEEN MOVEMENT:
  
    • Moves ANY distance in ANY direction
    • Combines Rook + Bishop powers
    • Cannot jump over pieces
    • Most powerful piece (value = 9 points)
  
  Example from e4:
    . . ♛ . .
    . ♛ ♛ ♛ .
    ♛ ♛ ♛ ♛ ♛
    . ♛ ♛ ♛ .
    . . ♛ . .
       """)
def rook():
    print(
        """ ♖ ROOK MOVEMENT:
  
    • Moves ANY distance horizontally or vertically
    • 4 directions: up, down, left, right
    • Cannot jump over pieces
    • Strong on open files/ranks (value = 5 points)
  
  Example from e4:
    . . ♜ . .
    . . ♜ . .
    ♜ ♜ ♜ ♜ ♜
    . . ♜ . .
    . . ♜ . .
    """)
def bishop():
    print(
        """♗ BISHOP MOVEMENT:
  
    • Moves ANY distance diagonally
    • 4 diagonal directions
    • Stays on same color squares forever!
    • Cannot jump over pieces (value = 3 points)
  
  Example from e4:
    ♝ . . . ♝
    . ♝ . ♝ .
    . . ♝ . .
    . ♝ . ♝ .
    ♝ . . . ♝
    """)
def knight():
    print("""
           ♘ KNIGHT MOVEMENT:
  
    • Moves in L-shape: 2+1 squares
    • 8 possible positions
    • CAN jump over other pieces (unique!)
    • Changes square color with every move (value = 3 points)
  
  Example from e4:
    . ♞ . ♞ .
    ♞ . . . ♞
    . . ♞ . .
    ♞ . . . ♞
    . ♞ . ♞ .
    """)
def pawn():
    print(
        """♙ PAWN MOVEMENT:
  
    • Moves FORWARD 1 square (toward opponent)
    • Can move 2 squares from starting position
    • Captures DIAGONALLY forward (1 square)
    • Promotes when reaching last rank
    • Special: En passant capture (value = 1 point)
  
  White pawn (moving up):
    . . . . .
    . ♟ . ♟ .   ← Capture diagonally
    . . ♙ . .
    . ♙ . . .
  
  Black pawn (moving down):
    . . . . .
    . ♙ . ♙ .   ← Capture diagonally
    . . ♟ . .
    . ♟ . . .""")

print('WELCOME HERE TO KNOW THE MOVEMENT OF CHESS PIECESES')

while True:
    print("""
    Select a piece:
        K - King     Q - Queen    R - Rook
        B - Bishop   N - Knight   P - Pawn
        """)
    choose=input('Choose an option= ').lower()
    if choose=='k' or choose=='king':
        king()
    elif choose=='q' or choose=='queen':
        queen()
    elif choose=='r' or choose=='rook':
        rook()
    elif choose=='b' or choose=='bishop':
        bishop()
    elif choose=='n' or choose=='knight':
        knight()
    elif choose=='p' or choose=='pawn':
        pawn()
    again=input('Do You want to see another piece? ').lower()
    if again!='y':
        print('Thank For Visiting!!')
        break
    
