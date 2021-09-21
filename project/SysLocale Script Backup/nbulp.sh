:set ff=unix
#!/bin/bash
#echo "Script for mounting Language pack"
# To run nbulp.sh 0089 JA

touch language_$(date +"%Y_%m_%d_%I_%M_%p").log
OUTPUT="language_$(date +"%Y_%m_%d_%I_%M_%p").log"
exec >$OUTPUT

echo "Enter the build version" $1 
echo "Enter the language pack" $2

Buildlocation="10.210.73.181:/newbuilds/NB_811/NB_8.1.1_$1"
nbucheck="/usr/openv/netbackup"

if [ -d "$nbucheck" ]
then
	echo "Netbackup is installed" 
		if [ "$2" == "JA" ]; then
		   echo "$Buildlocation"
		   mount $Buildlocation/NetBackup_8.1.1_JA /newbuilds
		   echo "Japanese language pack"
		elif [ "$2" == "ZH" ]; then
			mount $Buildlocation/NetBackup_8.1.1_ZH /newbuilds
			echo "Chinese language pack"
		elif [ "$2" == "FR" ];then
			mount $Buildlocation/NetBackup_8.1.1_FR /newbuilds
			echo "French language pack"
		fi
else
	echo "ERROR: Please install Netbackup as prerequisite"
fi


#echo below code is to validate NBU is installed or not /usr/openv/netbackup
nbucheck="/usr/openv/netbackup"

if [ -d "$nbucheck" ] 
then
	echo "file found"
else
	echo "not found"
fi




