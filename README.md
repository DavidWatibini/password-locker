# PASSWORD LOCKER

This is a Python app that allows users to save passwords to various online accounts they have.

## Author name

[David Watibini Makhanu](https://github.com/watibini/password-locker.git)

## Project Description

This is an app that allows users to store account credentials, it also gives them the chance to create new accounts and store their credentials, they can also delete those credentials they don't need any more.

## Technologies Used

Python 3.6

## Application requirements

1. Ensure you have Python3.6 installed in your computer. you can download it by running this command

`$ sudo apt-get update sudo apt-get install python3.6.`

2. Ensure you have PiP installed in your computer, you can download it by running this command:

`$ python get-pip.py`

## Project setup instruction/ installations


1. From the repository, click + in the global sidebar and select Clone this repository .

2.  Copy the clone command.

3.  From a terminal window, change to the local directory where you want to clone your repository.

or just use this

`$ git clone https://github.com/watibini/password-locker.git`

4. Run the following command to make the app executable;

`$ chmod +x run.py`

5. Run this command to open the app

`$ ./run.py`


## BDD

| Behavior        | Result |
| ------------- |:----:|
| User types in 1 when requested | User is prompted to input account details |
| User types in 2 | User is able to view all accounts created by him/her|
| User types in 3 | User is able to search for saved accounts using their username|
| User types in 4 | The application closes|

## TDD

-To test the app, run this commands in the terminal;

`$ python3.6 user_test.py`

`$ python3.6 credential_test.py`

## Live link

Use this link to see the web-page

(<https://watibini.github.io/password-locker/>)

## Contact Information

Email-(watimakhanu@gmail.com)

Github user name -Watibini

## License

MIT License

Copyright (c) [2018] [David Watibini Makhanu]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
