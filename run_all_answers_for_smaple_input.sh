for f in answers/*.py;
do
    echo "Running $f";
    echo "-----------------------"
    python3 "$f";
    echo "-----------------------"
done