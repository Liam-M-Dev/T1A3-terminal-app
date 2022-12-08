# Haiku Creator - WIP

## Liam Massey T1A3

***

### Repository Link

[Github repository](https://github.com/Liam-M-Dev/T1A3-terminal-app)  
***

### About the App

Haiku creator is a terminal app that you can use to create your own haiku poetry. The app it allows you to create a file to save your own haiku poems. You can create multiple files, access them to print out your poems to the terminal, edit poems and remove poems or the file itself.  
As an added extra there is a jumble mode that allows you to select a file with 2 or more poems and randomly mix/match the poems sentences to create new poems.  
Just remember to follow the basic rule, 5-7-5 rule (5 syllables first line, 7 second line and 5 for the third line).  
Please refer to the help documentation to get a better understanding to install the app and how to use it.  
***

### Code Style Guide

For this terminal application I will be following the pep8 style guide.  
[pep8 style guide](https://peps.python.org/pep-0008/#copyright)  
***

### List of Features and Description  

List of features associated with the app:

- A clean menu with clear inputs for the user.
- Create a haiku allowing to create a new haiku and save it in a new file or within an already available file.
- An easy to use file system allowing editing and removing of files and poems within the file.
- A jumbler that jumbles the poems within a file and returns a fun mismatch of poems.

#### **Menu Feature**

The menu is a clean feature that will keep the screen clear of clutter when accessing the different options. It displays 5 options which are an intro section, the create haiku section, access saved files for editing, the jumble feature and a quit program feature. The user then selects the option by typing in the input section with the corresponding number.  

#### **Create a Haiku**

The create haiku is the main feature of this program. For this feature the user is able to create their own haikus and save them within a new file or a previously saved file. This feature is able to check the user inputs to ensure no incorrect values are provided and that each line follows the syllable rule. Users are prompted at the start to create a new file or use a saved file.  

#### **File System**

The file system is a feature that allows the users to handle the files and poems saved within a file. There are 3 main areas of this feature, creating a new file when it is chosen with creating a new haiku. Allowing users to open files and read the poems within, users can also edit the poems within the files. Lastly users are able to delete files and to delete poems within files.

#### **Jumbler**

The jumbler is a fun little feature in which the user can jumble the sentences within a saved file and return new mismatched poems. The jumbler will only accept a file with at least 2 or more poems within its contents. Once an appropriate file is chosen, the feature will rearrange the lines of the poems by swapping line 1s with line 1s, line 2s with line 2s and line 3s with line 3s. Returning a new set of mismatched poems this then allows the user to save the new list or return to the original file. 

***

### Implementation Plan

The implementation plan for this project is as follows (work in progress)

I have created a Kaban workboard to track my progress with the use of Trello boards. [link to website](https://trello.com/b/jaVpKf8J/haiku-terminal-app)

- Initially set up venv and install needed external libraries
- add requirements.txt
- Set up main loop which is the menu feature, this will have the other functions/extensions added to it during programming of other features. Deadline Saturday 10th of December 4pm
- Create intro page as this is a short introduction spot it won't take too long and connect to the main menu. Deadline Thursday 8th of December 4pm
- set up a small bash executable script to track progress of program whilst working throughout. Deadline Saturday 10th of December 4pm
- Create haiku feature follow check list. Deadline Monday 12th of December 4pm
- Create file system follow check list. Deadline Tuesday 13th of December 4pm
- create jumbler follow check list. Deadline Wednesday 14th of December 4pm
- Implement tests of two features (Create haiku feature and file system)(These tests will be created during creation of the two features) Will have this completed with the associated deadlines.
- Write up help file that explains all system requirements, how to install various packages and os related information and a useful help file for how to run the program itself including script execution from bash. Deadline Thursday 15th of December
- Finalize documentation aka clean all this up and make it readable. Deadline Thursday 15th of December
- Create slide deck and film presentation. Deadline Friday 16th of December

Deadline for my project is to have all this finished by Friday the 16th of December to allow for a few days of going through and double checking everything is good for submission.  

***

### Help Documentation  
