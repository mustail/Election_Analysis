# python practice continued
print("Hello world.")

print("Arapahoe and Denver are not in the list of counties.")


# printing with f string


my_votes = int(input("How many votes did you get in the election?"))
total_votes = int(input("What is the total number of votes in the election?"))
percentage_votes = (my_votes/total_votes) * 100
#print("I received " + str(percentage_votes)+ "% of total votes.")

message_to_candidate = (
    f"You received {my_votes:,} number of votes. "
    f"The total number of votes cast was {total_votes:,}. "
    f"You received {my_votes/total_votes*100:.2f}% of the total votes."
)
print(message_to_candidate)

print(f"I received {my_votes/total_votes*100}% of the total votes.")
print(f"I received {percentage_votes}% of the total election.")

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}

for county, voters in counties_dict.items():
    #print(county + " county has " + str(voters) + " registered voters.")
    print(f"{county} county has {voters:,} number of registered voters.")

# skill drill
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}
                ]

for county_dict in voting_data:
    print(f"{county_dict['county']} county has {county_dict['registered_voters']:,} number of registered voters.")
# very important here: If you use double quotation marks for the f-strings containing the keys,
# then be sure to use single quotation marks for the keys and values of the dictionary.
# I tried the above (for ex. county, registered_voters) with double quotes, but it did not work.
