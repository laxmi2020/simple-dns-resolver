Simple DNS Resolver
Description
This project is a simple DNS resolver that takes a domain name as input and returns its corresponding IP address using Python's socket library. It demonstrates basic network programming and DNS resolution in Python.

Features
Accepts a domain name from the user.
Resolves and returns the IP address for the given domain.
Handles errors when the domain name is invalid or cannot be resolved.
Prerequisites
Before running the project, ensure you have the following installed:

Python 3.x
Socket library (comes pre-installed with Python)

Run the Python Script:python dns_resolver.py

Input the Domain Name:

When prompted, enter a domain name (e.g., google.com), and the script will return the IP address.

Example Usage
After running the script, it will prompt you to enter a domain name. Here's what it might look like:


Enter the domain name: google.com
The IP address of google.com is: 142.250.190.78
Error Handling
If you enter an invalid domain, the script will display an error message:


Enter the domain name: invalid_domain
Invalid domain name or unable to resolve.


Contributing
Feel free to fork this repository and submit pull requests if you have improvements or bug fixes.

Contact
If you have any questions, feel free to contact me via GitHub Issues.

