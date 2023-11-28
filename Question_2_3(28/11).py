seq_one = ":-)"
seq_two = ":-("
total=0


votes = int(input("please enter the total number of votes"))
votes_distribution = input("please enter a sequence of a and b")
    if votes>15:
        raise Exception("the function has to have no more than 15 votes")
