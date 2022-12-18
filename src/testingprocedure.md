# Testing procedure and cases

## Acceptance test in test folder  

A basic acceptance test can be found in the tests folder, this test was done just to ensure that pytest was working as intended.  

***

## File system tests  

The file system test have all been automated and to ensure everything is working simply run pytest before operating the program.  
The testing procedure goes through a series of different tests which are outlined as follows.

- First test, is to test the mapped characters in the translation table remove the special characters from an inputted string. The expected results is to take "t!es$t@file?" and turn the string into testfile.json.
- Second test, ensures that the correct saved_files directory exists, and if not will create the path. Expected results is asserting that the function directory_path returns "./saved_files".
- Third test, is designed to ensure that list of files function returns the completed path "./saved_files/sample_poems.json.
- Forth test, confirms that the error KeyboardInterrupt is raised when back is typed into the input prompt.
- Fifth test, This test is ensuring that the create file function is creating a file called test_file.json.
- Sixth test, This test is confirming that the remove file function successfully deletes the test_file.json.
- Seventh test, testing to ensure that when open read file function is called upon that the returning output is a list structure.
- Eight test, testing the function file size takes the argument of the poem data and checks the length of the list, returning a fail message due to not having  2 or more poems in the list.
- Ninth test, is testing the file size function is returning the list of poems when the condition of 2 or more poems is met.

***

### Haiku tests

Haiku tests have also been automated and just require running pytest before operating the program.  
Testing procedure is as follows.  

- First test, tests that the five_syllable_count function escapes when the user types back into the input. This is checked by ensuring that the Keyboard Interrupt error is raised.
- Second test, using the five_syllable_count function this is testing to ensure that the function returns a string when the syllable count is met.  
- Third test, testing line_selection function returns the matching line when user inputs the desired line. Expected results is line_one.
- Forth test, testing line_selection returns line_two.
- Fifth test, testing line_selection returns line_three.
- Sixth test, testing line_selection function raises ValueError when "done" is inputted.
- Seventh test, testing the function haiku_creator returns a dictionary when inputting the values. For this test the values are some sample text writing and the key values were the title, line_one, line_two and line_three.
