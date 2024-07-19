# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[], play_order=[]):
    if not prev_play:
        prev_play = 'R'
    opponent_history.append(prev_play)

    if len(opponent_history) > 5:
        last_four = "".join(opponent_history[-4:])
        play_order.append(last_four)
        # print(play_order)
        
        potential_plays = [
            play_order[-1][-3:] + "R",
            play_order[-1][-3:] + "P",
            play_order[-1][-3:] + "S",
        ]

        # print("potential_plays: ", potential_plays)

        sub_order = {
            k: play_order.count(k) 
            for k in potential_plays
        }

        # print(sub_order)

        prediction = max(sub_order, key=sub_order.get)[-1:]

        # print("prediction: ", prediction)


        ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
        return ideal_response[prediction]

    # guess = "R"
    # if len(opponent_history) > 2:
    #     guess = opponent_history[-2]

    # return guess