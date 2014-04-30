#!/bin/bash

for p in 2 1.01 1.001 1.0001 1.00001 1.000001 1.0000001 1.00000001 1 
do
    for normind in 0.1 0.01 0.001 0.0001 0.000001 0.00000001
    do
	echo $p $normind
	~/Documents/thesis/lbfgsbNS/./rosenbrockp 10 10000 $p $normind >> outputBreak/lastexperimentnormind10000.txt
	#~/Documents/thesis/lbfgsfortran/./rosenbrockStrongp 10 2000 $p >> outputBreak/breakrosenbrockStrong$p.txt
    done
done

exit 0;

