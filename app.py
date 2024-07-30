import modules.polling as polling, modules.voting as voting

def app():    
    # get registered voters
    getRegisteredVoters = int(input("Enter number of registered voters: "))

    # count votes
    vote_count = 0 #initialise vote_count variable to track votes
    while vote_count < getRegisteredVoters:
        # call get_votes method from voting module and update count variable
        voting.get_votes()
        vote_count = vote_count + 1
        result = polling.poll
        
        try:
            # winner = max(result.items(), key=lambda x: x[1])
            winner = max(result.values(), key=lambda x: list(x.values())[0])

            # party = max(result, key=lambda k: list(result[k].values()[0]))

        except Exception as e:
            print(f"{e}")
        else:
            # candidate = winner[0]
            # no_of_votes = winner[1]
            # print(f"The winner of the election is {candidate} with {no_of_votes} votes.")
            # print("no bug here")
            # print(f"{party} has the highest votes")
            print(winner)
        # finally:
        #     print("program ended")
app()