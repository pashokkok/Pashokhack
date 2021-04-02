#!/bin/bash
clear
echo"---------------"
echo"-  who you ?  -
echo"---------------
echo"-  1.Termux   -
echo"---------------"
read numb
if [$numb = "1"]
then
 pip install colorama
 pkg install python
else
 echo "Pls write 1 or exit"
 fi