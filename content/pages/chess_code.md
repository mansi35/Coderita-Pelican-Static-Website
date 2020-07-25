Title: Coding The PGN Parser Chess
Date: 2020-12-05 10:18
Modified: 2020-12-05 19:22
Category: Python
Tags: programming
Slug: pgn-parser-chess-code
Author: Mansi Sharma
Summary: Let's try to parse a pgn file to determine final positions of pieces on Chess Board.

##Setup and Pre-processing##

The first step to code this problem is to know the setup of the game. So first of all we must set up the game by keeping all the white and black pieces on their respective starting positions. We would create a board view which will show that at a particular position which piece is present. Also we would create a piece view which would specify the position of each piece.

    1 def setup():
    2     """ create a board view and a piece view of the starting position"""
    3
    4     squares = [y+x for x in "12345678" for y in "ABCDEFGH"]
    5     start = "RNBQKBNR" + "P" * 8 + " " * 32 + "p" * 8 + "rnbqkbnr"
    6     board_view = dict(zip(squares, start))
    7
    8     piece_view = {_:[] for _ in "BKNPQRbknpqr"}
    9     for sq in board_view:
    10        piece = board_view[sq]
    11        if piece != " ":
    12            piece_view[piece].append(sq)
    13    return board_view, piece_view

This would create the initial board setup.

The second thing we need to do now is pre-process the pgn file, that is remove all the comments and Seven Tag Roasters (STR) from the pgn file. We can do this using using pattern matching available in python Regex and return a list of all moves.

This list will be now devoid of any comments and only consists of moves. Also we would remove all the attonations and clean up the moves. Since as we have already read in the prerequisites of this problem that in the pgn file a pawn may or may not be represented by a letter so we must also keep that in mind and fix up the pawn move by attaching the "P" or "p" letter with the moves if not present.

We must also process the last move seperately since there could be two cases:

1. The White wins

2. The Black wins

If the white wins there would be no black move in the pgn file so we should handle this last move seperately.

##Moving Pieces##

Now, since the initial setup and the pre-processing is done, we can now move to understand the moves different pieces will make.

We can observe now that almost all the pieces will behave similar to each other except the pawn. Since the moves the pawn will make will also have some other properties other than capture. The pawn also exhibits the properties of en-passant and promotion and hence it must be handeled seperately.

Talking about all the other pieces, the main thing we have to do is:

1. Remove the piece that is moving from the board view of previous position.

2. Add the piece that is moving to the board view of the final position.

3. Add the final position to the piece view of the piece.

4. Remove the previous position from the piece view of the piece.

5. If a enemy piece is captured, then remove the final position of our piece from the piece view of captured piece.

We can implement it in code in the following way:

    1 def move_piece(move, board_view, piece_view):
    2     piece, to_square = move[0], move[-2:]
    3
    4     capture = (move[-3] == "x")
    5     if capture:
    6         move = move[:-3] + move[-2:]
    7         captured_piece = board_view[to_square]
    8
    9     if len(move) == 5:
    10         from_square = move[1:3]
    11     elif len(piece_view[piece]) == 1:
    12         from_square = piece_view[piece][0]
    13     else:
    14         from_square = get_from_square(move, board_view, piece_view[piece])
    15
    16     board_view[from_square] = SPACE
    17     board_view[to_square] = piece
    18
    19     piece_view[piece].append(to_square)
    20     piece_view[piece].remove(from_square)
    21     if capture:
    22         piece_view[captured_piece].remove(to_square)
    23
    24     return board_view, piece_view


Also, there is one more thing, there are two rooks, two knights and two bishops in the same time. So how do we know which piece we have to move exactly?

Thatswhy we need to know what are the possible positions a particular piece could move or being more specific we should check whether the position we want to move a piece to, is in the possible positions it can move or not.

This is the reason we learnt how the pieces move in the prerequisite for this problem. So let's apply our learning to this.
     
     1     moved_by = move_sep(fp, tp)
     2
     3     def can_rook_move():
     4         return moved_by[0] == 0 or moved_by[1] == 0
     5
     6     def can_knight_move():
     7         return moved_by in [(1, 2), (2, 1)]
     8
     9     def can_bishop_move():
     10         return moved_by[0] == moved_by[1]
     11
     12     def can_queen_move():
     13         return can_rook_move() or can_bishop_move()
     14
     15     def can_king_move():
     15         return moved_by in [(0, 1), (1, 0), (1, 1)]
     17
     18     return {"R": can_rook_move, "N": can_knight_move,  "B": can_bishop_move, \
     19             "Q": can_queen_move, "K": can_king_move}[piece]()

But there may be a case where both the pieces are able to come to the specified situation. In such a case, we must resolve this ambiguity by checking if there is a piece of the same team in between the path to that position. If that is the case, that piece can't move to the specified position and the other piece will acquire that position. So we need to resolve this ambiguity too. It is not that difficult, we just have to check for the ranks and files being empty between those positions and can be handled easily.

##Pawn Moves##

Now comes the pawn moves. We can divide the pawn moves into four categories:

1. Regular pawn move.

2. Capturing.

3. Promotion.

4. Enpassant.

We can identify them easily using Regex since we know the pattern they will follow (from the prerequisites).

Keeping in mind, data is code, we can use this data given below for our code, processing it beforehand. 

      1 SPACE =" "
      2 WHITE, BLACK ="P", "p"
      3 can_move_from = {WHITE: {"3": ["2"], "4": ["3", "2"], "5": ["4"], "6":["5"], "7":["6"]},\
      4                 BLACK: {"6": ["7"], "5": ["6", "7"], "4": ["5"], "3": ["4"], "2": ["3"]} }
      5
      6 can_capture_from = {WHITE: {"3": "2", "4": "3", "5": "4", "6": "5", "7": "6", "8": "7"},\
      7                     BLACK: {"6": "7", "5": "6", "4": "5", "3": "4", "2": "3", "1": "2"} }
      8 enpassant_captured = {WHITE: "5", BLACK: "4"}
      9 promoted_from = {WHITE: "7", BLACK: "2"}


Talking about a regular pawn move or a capturing move, it is similar to a regular piece move and a regular capturing move we discussed before. We just have to update the board view and the piece view.

When we talk about promotion, there are two cases:

1. Promotion with capturing

2. Promotion without capturing

If it is a promotion with capturing, it would be a move like gxf8=Q or gxf8Q. So what we have to do is:

1. Remove the position the pawn is promoted to from the piece view of the captured piece.

2. Add the piece the pawn is promoted to, to the board view of the position now.

3. Add the position the pawn is promoted at to the piece view of the piece it is promoted to.

4. Remove the previous position of pawn from the piece view of pawn.

Else, if the pawn promotes without capture, it would be a move like f8=Q or f8Q:
So we can follow the same steps just skipping step 1.

     1 def promote(move, board_view, piece_view):
     2     if "x" in move:
     3         # Move like gxf8=Q or gxf8Q
     4         pawn, from_file, promoted_at, promoted_to = move[0], move[1], move[3:5], move[-1]
     5         captured_piece = board_view[promoted_at]
     6         piece_view[captured_piece].remove(promoted_at)
     7     else:
     8         # Move like f8=Q or f8Q
     9         pawn, from_file, promoted_at, promoted_to = move[0], move[1], move[1:3], move[-1]
     10
     11     board_view[promoted_at] = promoted_to
     12     piece_view[promoted_to].append(promoted_at)
     13
     14     from_square = from_file + promoted_from[pawn]
     15     piece_view[pawn].remove(from_square)
     16
     17     return board_view, piece_view

Now, if the move is an enpassant, we can use the data we have processed beforehand to identify the position the pawn comes from and easily update the board view and piece view by removing the pawn of enemy team from the board and acquiring the position it may have moved. This is depicted in the code below:

     69 def make_enpassant(move, board_view, piece_view):
     70      move = move.replace("x", "")
     71      pawn, from_file, to_square = move[0], move[1], move[2:4]
     72      to_file = to_square[0]
     73
     74      from_square = from_file + enpassant_captured[pawn]
     75      captured_pawn_square = to_file + enpassant_captured[pawn]
     76
     77      board_view[to_square] = pawn
     78      board_view[from_square] = SPACE
     79      board_view[captured_pawn_square] = SPACE
     80
     81      piece_view[pawn].remove(from_square)
     82      piece_view[pawn].append(to_square)
     83      piece_view[pawn.swapcase()].remove(captured_pawn_square)
     84
     85      return board_view, piece_view

Now, since all the movements of the pieces has been discussed, we can easily find out the final position of all the pieces after the game ends.

And this has been our mission all along.

<div id="disqus_thread"></div>
<script>

/**
*  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
*  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables*/
/*
var disqus_config = function () {
this.page.url = PAGE_URL;  // Replace PAGE_URL with your page's canonical URL variable
this.page.identifier = PAGE_IDENTIFIER; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
};
*/
(function() { // DON'T EDIT BELOW THIS LINE
var d = document, s = d.createElement('script');
s.src = 'https://coderita.disqus.com/embed.js';
s.setAttribute('data-timestamp', +new Date());
(d.head || d.body).appendChild(s);
})();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
                            
