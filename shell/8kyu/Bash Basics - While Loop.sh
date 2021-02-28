#Create a simple while loop in bash that prints the numbers 1-20 to stdout.
#
#It should look like (stdout):
#
#Count: 1
#Count: 2
#...
#Count: 21

#!/bin/bash

countToTwenty() {
  count=1
  while [ $count -le 20 ]
  do
    echo "Count: $count"
    count=$(( $count + 1 ))
  done
}

countToTwenty
