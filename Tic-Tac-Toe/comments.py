#             if available_square(clicked_row, clicked_col):
#                 if player == 1:
#                     mark_square(clicked_row, clicked_col, 1)
#                     if check_win(player):
#                         game_over = True
#                     player = 2

# # after click toggle player
#                 elif player == 2:
#                     mark_square(clicked_row, clicked_col, 2)
#                     if check_win(player):
#                         game_over = True
#                     player = 1
                
    ###---------- OPTIMIZED ----------###
            # if available_square(clicked_row, clicked_col):
            #     mark_square(clicked_row, clicked_col, player)
    
            #     if check_win(player):
            #         game_over = True




# def available_square(row, col):
#     return board[row][col] == 0       # [same as below comment]
# ''' if board[row][col]:
#         return True
#     else:
#         return False
# '''