for f in ./*.py
do
   echo "Processing $f"

   echo '# Author Tiago Ferreira, Brian Northan' | cat - $f > temp && mv temp $f

done
