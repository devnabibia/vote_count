import modules.polling as polling

def get_votes():
    # Display Party to voters
    parties = polling.poll.keys()
    print("Vote a running party\n")
    for party in parties:
        print(party)

    # Get vote choice from voters
    vote = input("Choose your party: ")
    print("Thank you for voting")

    # update polls
    # polls = polling.poll
    if vote in polling.poll:
        print("vote added")
        if vote.upper() == "LP": 
            polling.poll[vote]['Peter Obi'] += 1
        elif vote.upper() == "PDP":
            polling.poll[vote]['Lionel Messi'] += 1
        elif vote.upper() == "APGA":
            polling.poll[vote]['Ben White'] += 1
        elif vote.upper() == "AD":
            polling.poll[vote]['John Doe'] += 1
        elif vote.upper() == "APC":
            polling.poll[vote]['Karen Joy'] += 1
        return polling.poll

        # try:
        #     updatePollVote = updatePollVote + 1
        # except Exception as e:
        #     print(f"{e}")
        # else:
        #     print(polling.poll)