


cat hightemp.txt | sed -e 's/\t/ /g'


cat hightemp.txt | tr "\t" ' '

cat hightemp.txt | expand -t 1
