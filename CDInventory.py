#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
#Brent Kieszling, 2020-August-10, Modified all sections
#Brent Kieszling, 2020-August-11, Fixed option [a] and added SOC formatting
#------------------------------------------#

#DATA--
strChoice = '' # User input
lstActiveTbl = []  # list of dictionaries to hold data
dicHeader ={'ID': 'ID', 'Title': 'Title', 'Artist': 'Artist'}
dicRow = {'ID': '', 'Title': '', 'Artist': ''}
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
haveLoaded = False # Load tracker
strMainMenu = 'Please select from the following options: \n \
            [l] load Inventory from file\n \
            [a] Add CD\n \
            [i] Display Current Inventory \n \
            [d] delete CD from Inventory\n \
            [s] Save Inventory to file\n \
            [x] exit \n'

strNotLoadedA = 'Adding a new entry before loading saved data may \
result in duplicate CD IDs. Would you like to return to the main menu? (y/n) \n'

strNotLoadedS = 'Saving before loading will overwrite saved data.\n\
Would you like to continue? (y/n) \n'
#PROCESSING--
#Check and see if the file is present, if not create the file
import os
if os.path.exists(strFileName):
    pass
else:
    objFile = open(strFileName, 'a')
    objFile.close()

# Get user Input
#PRESENTATION INPUT/OUTPUT--
print('Welcome to: The Magic CD Inventory!\n')
while True:
# 1. Display menu allowing the user to choose:
    # convert choice to lower case at time of input
    strChoice = str(input(strMainMenu)).lower()
    print()


#----------------Menu option [x]----------------------------------------- 
# Exit the program if the user chooses so
#PROCESSING--
    if strChoice == 'x':
        break


#----------------Menu option [l]----------------------------------------- 
# Load data from saved file
#PROCESSING--
    elif strChoice == 'l':
        haveLoaded = True
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstSavedCD = row.strip().split(',')
# All ID's are intergers except the header ID which is a string.
    # This try statement navigates the difference in type while adding saved data.
            try:
                lstSavedCD[0] = int(lstSavedCD[0])
            except:
                pass
            dicRow = {'ID' : lstSavedCD[0], 'Title': lstSavedCD[1], 'Artist': lstSavedCD[2]}
            if dicRow in lstActiveTbl:
                pass
            else:
                lstActiveTbl.append(dicRow)
        objFile.close()
        
#PRESENTATION OUTPUT--
        print('Saved data has been uploaded.')


#----------------Menu option [a]----------------------------------------- 
# Add data to the table (2d-list) each time the user wants to add data
#PROCESSING--
    elif strChoice == 'a': 
# Add header to active table if not already present
        if dicHeader in lstActiveTbl:
            pass
        else:
            lstActiveTbl.append(dicHeader)

# Check if saved data has been loaded this session
        while haveLoaded != True:
#PRESENTATION INPUT/OUTPUT--
            x = str(input(strNotLoadedA)).lower()
#PROCESSING--
            if x == 'y':
                break
            else:
#PRESENTATION INPUT/OUTPUT--
                strID = input('Enter a numerical ID: ')
                strTitle = input('Enter the CD\'s Title: ')
                strArtist = input('Enter the Artist\'s Name: ')
#PROCESSING--
                intID = int(strID)
                dicRow = {'ID': intID, 'Title': strTitle, 'Artist': strArtist}
                lstActiveTbl.append(dicRow)
                break

        while haveLoaded == True:
#PRESENTATION INPUT/OUTPUT--
            strID = input('Enter an ID: ')
            strTitle = input('Enter the CD\'s Title: ')
            strArtist = input('Enter the Artist\'s Name: ')
            intID = int(strID)
#PROCESSING--
            dicRow = {'ID': intID, 'Title': strTitle, 'Artist': strArtist}
            lstActiveTbl.append(dicRow)
            break


#----------------Menu option [i]-----------------------------------------  
# Display the current data to the user each time the user wants to display the data
#PROCESSING--
    elif strChoice == 'i':
# All of the dictionaries have the same key words 'ID', 'Title' and 'Artist'
    # Therefore we can print the value held at the key word as we go through each dictionary.
#PRESENTATION OUTPUT--
        for row in lstActiveTbl:
# Formats the display into an easily readable table. ID is padded with 6 available
    #characters while Artist and Title are padded with 22. Recommended by Mr Klos.
            print('{:6}{:22}{:22}'.format(str(row['ID']), row['Title'], row['Artist']))


#----------------Menu option [d]-----------------------------------------  
#Delete an entry
#PROCESSING--
    elif strChoice == 'd':
#PRESENTATION INPUT/OUTPUT--
        cdDelete = int(input('Please enter the ID of the CD you would like to remove. \n'))
#PROCESSING--
        for row in lstActiveTbl:
#checkID is set to the value held by ID in each dictionary and then checks
    #if it matches the users input.
            checkID = row.get('ID')
            if checkID == cdDelete:
                lstActiveTbl.remove(row)
#PRESENTATION INPUT/OUTPUT--
                print('The following CD has been removed: \n')
                print(row)
#PROCESSING--
            else:
                pass


#----------------Menu option [s]-----------------------------------------  
# Save the data to a text file CDInventory.txt if the user chooses so
#PROCESSING--
    elif strChoice == 's':
        while haveLoaded != True:
#PRESENTATION INPUT/OUTPUT--
            z = str(input(strNotLoadedS)).lower()
#PROCESSING--
            if z == 'y':
                objFile = open(strFileName, 'w')
                for row in lstActiveTbl:
                    strID = str(row['ID'])
                    strTitle = row['Title']
                    strArtist = row['Artist']
                    objFile.write(strID + ',' + strTitle + ',' + strArtist + '\n')
                objFile.close()
                print('Save succesful!')
                break
            else:
                print('Failed to save.')
                break

        while haveLoaded == True:
#PRESENTATION INPUT/OUTPUT--
            objFile = open(strFileName, 'w')
            for row in lstActiveTbl:
                strID = str(row['ID'])
                strTitle = row['Title']
                strArtist = row['Artist']
                objFile.write(strID + ',' + strTitle + ',' + strArtist + '\n')
            objFile.close()
            print('Save succesful!')
            break


# Handle unexpected menu input
#PRESENTATION OUTPUT--
    else:
        print('Please choose from the following letters: l, a, i, d, s or x')

