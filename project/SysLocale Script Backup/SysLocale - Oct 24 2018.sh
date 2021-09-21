#!/bin/bash
echo "Setting locale..."
touch validation.log
OUTPUT="validation.log"
exec >$OUTPUT
#To get the OS flavour
OUTPUT2="$(uname -a)"
sentence="${OUTPUT2}"
stringarray1=($sentence)
echo "your system locale is:"$stringarray1
if [ "${stringarray1[0]}" == "Linux" ]
	then
	#	echo "Enter Language of your choice, in format [Lang_COUNTRY.encoding (e.g ja_JP.utf8.en_US.utf8] :"
		echo "Entered choice" $1
		#echo $1
		chmod 777 ~/.bash_profile
		echo "#Locale Setting
		export LANGUAGE=$1
		export LANG=$1
		export LC_ALL=$1
		export LC_ALL=$1">~/.bash_profile
		#echo "Enter the build version" $1
		fc-list -f "%{family}\n" :lang=$1 >> os.txt

		if  grep -q "Efont" os.txt;
		then
				echo "OS environment not recommended for I18N testing"
		else
				echo "Environment fine for I18N testing"
		fi

		reboot
#		echo " Would you like to reboot the machine for locale to set (y/n) :" $MachRestart
#		read MachRestart

#		if [ $MachRestart = "y" ]
#		then
#				source ~/.bash_profile
#				 reboot
#				else
#					echo " exiting"
#				fi
fi
#verfying the Solaris OS
#if [ "${stringarray1[0]}" == "SunOS" ]
#	then
#		echo "Enter Language of your choice, in format [Lang_COUNTRY.encoding (e.g ja_JP.UTF-8,en_US.UTF-8] :"
#		read $1
#		chmod 777 ~/.bash_profile
#		echo "#Locale Setting
#		export LANGUAGE=$$1
#		export LANG=$$1
#		export LC_ALL=$$1
#		export LC_ALL=$$1">~/.bash_profile
#		echo " Would you like to reboot the machine for locale to set (y/n) :" $MachRestart
#		read MachRestart
#
#		if [ $MachRestart = "y" ]
#		then
#				source ~/.bash_profile
#				 reboot
#				else
#					echo " exiting"
#				fi
#	fi
	
