# writing a list of line to file
lines=['first line \n','Second line \n','third line \n']
with open ('example.txt','a') as file:
    file.writelines(lines)