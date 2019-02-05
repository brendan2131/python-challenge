import os
import csv

# Path to CSV
csv_path = os.path.join("..","Resources","election_data.csv")

# Create list for votes
votes=[]


# Open CSV
with open(csv_path, newline="", encoding = "utf-8") as csvfile:
    election = csv.reader(csvfile, delimiter=",")

    # Skip Headers
    csv_header = next(election)

    # Collect all votes
    for i in election:
        votes.append(i[2])

    TotalVotes = len(votes)

    # Find unique candidate values
    candidates = set(votes)

    # Use Lists to find total votes for each candidate
    KhanList=[]
    OTooleyList=[]
    CorreyList=[]
    LiList=[]

    for v in votes:
        if v == "Khan":
            KhanList.append(v)
        elif v == "O'Tooley":
            OTooleyList.append(v)
        elif v == "Correy":
            CorreyList.append(v)
        else:
            LiList.append(v)


    # Total Votes per Candidate
    KhanVotes = len(KhanList)
    OTooleyVotes = len(OTooleyList)
    CorreyVotes = len(CorreyList)
    LiVotes = len(LiList)

    # Percent Votes per Candidate
    KhanPercent = (KhanVotes / TotalVotes) * 100
    OTooleyPercent = (OTooleyVotes / TotalVotes) * 100
    CorreyPercent = (CorreyVotes / TotalVotes) * 100
    LiPercent = (LiVotes / TotalVotes) * 100

    # Find Winner
    ResultsList=[KhanVotes,OTooleyVotes,CorreyVotes,LiVotes]
    CandidateList=["Khan","O'Tooley","Correy","Li"]

    greatist_ammount = max(ResultsList)
    max_index = ResultsList.index(greatist_ammount)
    Winner = CandidateList[max_index]

    # Print
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {TotalVotes}")
    print("-------------------------")
    print(f"Khan: {KhanPercent}% ({KhanVotes})")
    print(f"Correy: {CorreyPercent}% ({CorreyVotes})")
    print(f"Li: {LiPercent}% ({LiVotes})")
    print(f"O'Tooley: {OTooleyPercent}% ({OTooleyVotes})")
    print("-------------------------")
    print(f"Winner: {Winner}")
    print("-------------------------")

    # Export text file
    output_path = os.path.join("..", "PyPoll", "ElectionResults.txt")

    text_file = open(output_path, "w")

    text_file.write("Election Results\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Total Votes: {TotalVotes}\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Khan: {KhanPercent}% ({KhanVotes})\n")
    text_file.write(f"Correy: {CorreyPercent}% ({CorreyVotes})\n")
    text_file.write(f"Li: {LiPercent}% ({LiVotes})\n")
    text_file.write(f"O'Tooley: {OTooleyPercent}% ({OTooleyVotes})\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Winner: {Winner}\n")
    text_file.write("-------------------------")

    text_file.close()



    

