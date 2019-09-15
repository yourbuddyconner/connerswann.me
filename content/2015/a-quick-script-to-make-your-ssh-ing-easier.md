Title: A Quick Script to Make Your SSH-ing Easier
Date: 2015-01-21 15:50
Author: Conner Swann
Slug: a-quick-script-to-make-your-ssh-ing-easier
Category: MacOS
Tags: MacOS, BASH, Script, Fixes

At work, I find myself SSH-ing into at least five different machines a day. I use a password manager, so my workflow looks like this:

> 1. ssh conner@myserver.com 
> 2. Grab my password from password manager
> 3. paste password into terminal
> 4. if you messed up GOTO 1

This gets really tedious after the 20th time, so I wrote a quick Bash script that leverages the handy [ssh-copy-id](http://manpages.ubuntu.com/manpages/precise/man1/ssh-copy-id.1.html) command. 

<pre class="line-numbers">
<code class="language-bash">
##########################################
# This script relies on the package "ssh-copy-id". It's on all your major package 
# managers. This script was written for an OSX environment, but there's no reason 
# why it wouldn't work on other unix-ey platforms. 
#
# WARNING: Use this at your own risk, I'm not responsible if you break something by running it.
#
#	The following happens when this script runs.
#	.5. Data is gathered.
# 	1. Keys are generated and named based on the short name you supply in ~/.ssh/.
#	2. The private key is sent to the server with ssh-copy-key using the port specified. 
#	3. The pertinent information is added to your ssh-config (if you haven't made one, it'll make one for you).
#	
#	You can now ssh into your server using "ssh server_short_name"!
#
# 08/20/2014 http://connerswann.me
 
server_host_name=""
server_short_name=""
server_user=""
server_port=""
ssh_config=~/.ssh/config
 
clear 
 
if [ -z "$(which ssh-copy-id)" ]; then
	echo "Dude, you need 'ssh-copy-id' installed. Dying..."
	exit 1
fi
 
echo "Sup, let's save some SSH keys."
 
while [[ ! $confirm =~ ^([yY][eE][sS]|[yY])$ || $confirm == "" ]]; do
	echo 
	echo "Enter the server host name: "
	read server_host_name
	echo "Enter a short name for the server: "
	read server_short_name
	echo "Enter your username on the external server: "
	read server_user
	echo "Which port should I connect to? (just hit ENTER for default port 22)"
	read server_port
	if [ -z "$server_port" ] ; then server_port=22; fi #map empty server_port -> 22
 
	echo "Please verify that this is correct."
	echo "Short Name -> $server_short_name"
	echo "Host Name -> $server_host_name"
	echo "Server User -> $server_user"
	echo "Server Port -> $server_port"
	echo "Confirm? (Y/n)"
	read confirm 
	if [ -z "$confirm" ] ; then confirm="Y"; fi #map empty string to -> "Y"
done
 
clear
echo "Passing to ssh-keygen..."
ssh-keygen -t rsa -f ~/.ssh/$server_short_name 
 
echo "I hope that worked "
echo "Press ENTER to continue."
read confirm
 
cd ~/.ssh/
 
ssh-copy-id -p $server_port -i $server_short_name.pub $server_user@$server_host_name
 
touch $ssh_config

echo >>$ssh_config
echo "Host $server_short_name" >>$ssh_config
echo "Hostname $server_host_name" >>$ssh_config
echo "User $server_user" >>$ssh_config
echo "Port $server_port" >>$ssh_config
echo "IdentityFile ~/.ssh/$server_short_name" >>$ssh_config
 
echo "Contents of SSH Config File:"
echo 
cat $ssh_config
echo 
</code>
</pre>

The comments really say it all, but here's the TL;DR:

1. It collects information about the server you're configuring
2. It generates RSA keys for password-less identification with ssh-keygen
3. It sends those keys to the server using ssh-copy-id and saves all the information to your SSH profile

Now, my workflow looks like this: 
> \> ssh myserver

There you have it! If you've got any questions as to how this works or implementing it, shoot me a [tweet](http://twitter.com/yourbuddyconner)!