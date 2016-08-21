# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

1. $ pwd - display path of current working direcoty
2. $ cd - change directory
3. $ mkdir - make diretory
4. $ pushd - save current location and go to new location
5. $ popd - go to saved location
6. $ cp - copy file
7. $ mv - move file
8. $ rm - remove file
9. $ less - view file
10. $ exit - exit

---

###Q2.  List Files in Unix   

What do the following commands do:  
`ls`  - it lists all files in the directory
`ls -a`  - it displays all files, including hidden files
`ls -l`  - it displays long format listing
`ls -lh` - it displays long format listing, and file size in KB
`ls -lah` - it displays long format listing, file size in KB and display all files, including hidden files.  
`ls -t`  - it displays the newest files first, based on timestamp
`ls -Glp`  - it displays long format listing, color code the directory and display the directories with /

---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

ls -1 - it displays each entry on a line
ls -F - it flags file names
ls -R - it displays subdirectories
ls -d - it displays only directories
ls -p - it displays directories with /

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

xargs is normally used to group arguments together so that you dont get a "too many arguments " error which occurs when you pass a large number of arguments to a command

Here's an example where xargs is needed to group a large number of arguments to avoid errors:

#!/bin/sh
#script to echo out the arguments 1 at a time!
for a in $*
do
    echo $a
done
the command

$sh myscript 1 2 3 4 5
will yield

1
2
3
4
5
but

$sh myscript 1 2 3 4 5 6 7 8 9 10 11
will not work since the max number of parameters is exceeded

To get around this we could xargs

#!/bin/sh
#script to echo out the arguments 1 at a time!
for a in $*
do
    echo $a | xargs echo
done

We could then run it like this

 $sh myscript "1 2 3 4 5" "6 7 8 9 10 11"
and get the correct result since there are just 2 parameters
