FilenameUniqueId=$(date +"%Y%m%d_%H%M%S_%N.coffee")
OutputFile="."$FilenameUniqueId
echo "" > $OutputFile
while read x
do
#echo $x
echo $x >> $OutputFile
done
