
import math

batsmen = [
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    [],
    []
]

total_score = 0
total_wickets = 0

total_match_balls = 6 * 10
current_match_balls = 0
total_overs = 0
balls_in_over = 0
total_run_rate = 0

facing_batsman_index = 0
non_facing_batsman_index = 1

while current_match_balls < total_match_balls and total_wickets < 10:

    runs_scored = int(input("Runs scored off of delivery?: "))
    
    wicket_taken = False
    if (input("Wicket taken? (Y/N): ").upper() == "Y"):
        wicket_taken = True

    batsmen[facing_batsman_index].append(runs_scored)
    current_match_balls += 1
    
    total_score += runs_scored
    
    total_overs = math.floor(current_match_balls / 6)
    balls_in_over = current_match_balls % 6

    if total_overs == 0:
        total_run_rate = total_score
    else:
        total_run_rate = total_score / (current_match_balls / 6)

    if wicket_taken:
        total_wickets += 1
    
    if runs_scored % 2 != 0:
        temp_index = facing_batsman_index
        facing_batsman_index = non_facing_batsman_index
        non_facing_batsman_index = temp_index
    
    if balls_in_over == 0:
        temp_index = facing_batsman_index
        facing_batsman_index = non_facing_batsman_index
        non_facing_batsman_index = temp_index

    if wicket_taken:
        facing_batsman_index = max([facing_batsman_index, non_facing_batsman_index]) + 1

    print("------")
    print(f"{total_score} for {total_wickets} wickets")
    print(f"{current_match_balls} of {total_match_balls} bowled")
    print(f"Facing batsman: {sum(batsmen[facing_batsman_index])}")
    print(f"Non-facing batsman: {sum(batsmen[non_facing_batsman_index])}")
    print(f"Over: {total_overs}.{balls_in_over}")
    print(f"Runrate: {total_run_rate}")
    print("------")
    print(batsmen)

print(f"FINAL INNINGS SCORE {total_score} for {total_wickets} wickets")




