# Open a new text file (w mode) - called teams.txt - add the names of 5 sports teams.
sports_team_list = ["Chelsea F.C", "Manchester United F.C", "Team GB", "Arsenal F.C", "Liverpool F.C"]

teams_file = open("teams.txt", "w")

for team in sports_team_list:
    teams_file.write(team + "\n")

teams_file.close()

# read and display the names of the 1st and 4th team. (.strip())

teams_file = open("teams.txt", "r")
sports_teams = teams_file.readlines()

print(sports_teams[0].strip())
print(sports_teams[3].strip())

teams_file.close()

# edit the file so that the top line is replaced with "this is a new line"

teams_file = open("teams.txt", "r")

sports_team_list = teams_file.readlines()

teams_file.close()

teams_file = open("teams.txt", "w")

sports_team_list[0] = "This is a new line \n"

for team in sports_team_list:
    teams_file.write(team)

teams_file.close()

# Print out the edited file lien by line.

teams_file = open("teams.txt", "r")

sports_team_list = teams_file.readlines()

for team in sports_team_list:
   print(team)

teams_file.close()
