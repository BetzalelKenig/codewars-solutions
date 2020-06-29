# Create a function (or write a script in Shell) that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

if [ $(($1 % 2)) -eq 0 ]
  then echo "Even"
  else echo "Odd"
fi
