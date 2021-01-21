# Basic_Reverse_Shell
A basic reverse shell, written in python3 to help me learn the python sockets module.
This reverse shell uses the python3 sockets module and allows the user to execute commands on a remote host. 

The Server.py script listens for incoming connections, until the Client.py script is ran on a remote machine. When ran, the Client.py script connects to the server host, allowing the server to send and execute commands remotely and receive the ouputs. 

This script will not work over the internet by default; in order to achieve this you will need to port forward.

# Prerequisites
* The server ideally must run on a DEBIAN based system
* Sudo privileges
* Basic understanding of python3 variables
* An installation of dos2unix

# Installation
Grab the script in any way you want:

1) Clone the repository:
<pre>git clone https://github.com/nochhacks/Basic_Reverse_Shell</pre>

2) Directly download the ZIP file from the "Code" section above the landing page.


<b>(Linux Only!)</b>

In the Basic_Reverse_Shell folder, give both scripts execute permissions and convert the line endings to UNIX.
<pre>cd Basic_Reverse_Shell</pre> 
<pre>sudo apt install -y dos2unix && chmod +x *.py && dos2unix *.py</pre>

<b>If you wish to change the line ending styles you can do so manually with dos2unix / unix2dos:</b>

<pre>dos2unix file.py</pre>
<b>Or</b>
<pre>unix2dos file.py</pre>

# Usage

1) Edit the <b>Server.py</b> script with any text editor, and substitute the variables "SERVER_HOST" and "SERVER_PORT" with your machine's corresponding IP address and a port number. (The default "0.0.0.0" SERVER_HOST value is loopback, so should work as-is in most cases).

2) Edit the <b>Client.py</b> script with any text editor, and subsitute the variables "SERVER_HOST" and "SERVER_PORT" with the server's corresponding IP adress and port number. To clarify, by "server" I mean the machine that is running the Server.py script. In most cases, this is probably the only variable you will need to edit. Ensure that both script's "SERVER_PORT" variables are the same.

3) Run the Server.py script first from the command line:
<pre>./Server.py</pre>

4) Then run the Client.py script through python, or through the command line. Depending on the client OS, you may need to manually convert the line ending style using <b>dos2unix</b>.
