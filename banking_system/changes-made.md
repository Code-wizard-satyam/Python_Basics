# SUMMARY
### check code lines commented with CHANGE: to Know more:

## Recent Changes

### `main.py`
- Added an option to exit the program gracefully.
- Ensured consistent use of single quotes for strings.
- Added a message for exiting the program.
- Fixed the issue where the loop restarted with default section 2 after logging out by re-prompting the user for the main menu.

### `bank.py`
- Fixed missing double underscores in private attribute access.
- Corrected the iteration over `self.users` to avoid calling it as a function.
- Added a success message when a new user is added.
- Ensured proper handling of CSV file writing with `newline=''` to avoid concatenation issues.

### `user.py`
- Removed `(object)` from the `User` class definition as it is unnecessary in Python 3.
- Fixed an infinite loop in the `change_pin` method.
- Added a message for exceeding the maximum number of PIN attempts.
- Ensured unique card numbers are generated for each user.
- Improved withdrawal and deposit methods to handle user input more effectively.


## Future Improvements
- Better CSV handling with pandas and updation of records.
- Add more robust error handling.
