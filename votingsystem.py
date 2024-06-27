nominee1 = input("Enter the Name of 1st Nominee : ")
nominee2 = input("Enter the Name of 2nd Nominee : ") 




nm1_votes = 0
nm2_votes = 0

voter_id = [1,2,3,4,5,6,7,8,9,10]

no_of_voter = len(voter_id)


while True:
    if voter_id == []:
        print("Voting Session is Over !!!")
        if nm1_votes > nm2_votes:
            percent = (nm1_votes/no_of_voter)* 100
            print(nominee1,"has Won the Election with ",percent,"% of Votes")
            break
        elif nm2_votes> nm1_votes:
            percent = (nm2_votes/no_of_voter)* 100
            print(nominee2,"has Won the Election with ",percent," % of votes")
            break
        else:
            print("Both have Equal no of Votes !!!! Government will decide who will Rule")
            break
    
    
    
    
    voter = int(input("Enter Your Voter ID :"))
    if voter in voter_id:
        print("You are a Voter")
        voter_id.remove(voter)
        print("----------------------------------")
        print("To Give Vote to",nominee1,"Press 1")
        print("To Give Vote to",nominee2,"Press 2")
        print("----------------------------------")
        vote = int(input("Enter your Precious Vote :"))
        if vote == 1:
            nm1_votes ==1
            print(nominee1,"Thanks You to give your Important Vote to them !!")
        elif vote == 2:
            nm2_votes ==1
            print(nominee2,"Thanks You to give your Important Vote to them !!")
        elif vote > 2:
            print("Check your Pressed Key")
        else:
            print("You are Not Eligible for the Voting")