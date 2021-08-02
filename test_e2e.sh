#! /usr/bin/env sh
#
echo "##########################"
echo "### Running e2e tests! ###"
echo "##########################\n"
count=0 # number of test cases run so far

# Assume all `.in` and `.out` files are located in a separate `tests_e2e` directory

for folder in `ls -d tests_e2e/*/ | sort -V`; do
    name=$(basename "$folder")
    
    echo Running test $name.
 
    config_file=tests_e2e/$name/$name.config
    expected_file=tests_e2e/$name/$name.out
    in_file=tests_e2e/$name/$name.in

    python3 run.py $config_file < $in_file | diff - $expected_file || echo "Test $name: failed!\n"

    count=$((count+1))
done

name='10'
expected_file=11/10.out
config_file="bumblebee.txt"

echo Running test $name
python3 run.py $config_file | diff - $expected_file || echo "Test $name: failed!\n"
count=$((count+1))

name='11'
expected_file=11/11.out

echo Running test $name.
python3 run.py  | diff - $expected_file || echo "Test $name: failed!\n"
count=$((count+1))

echo "Finished running $count tests!"
