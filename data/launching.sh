for i in {1..6}
do
    (
        python3 ../src/main.py  \
            -i input/$i.fasta \
            -o output/$i.csv \
            -mf output/$i.mol2 \
            -s 20000 \
            -rp
    ) &
done
