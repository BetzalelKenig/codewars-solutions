# You are given a method called main, make it print Hello World! and don't return anything

# Note that for some languages, the function main is the entry point of the program.

# Here's how it will be tested:

#     java Solution.class parameter1 parameter2

# Hints:

#     Check your references
#     Think about the scope of your method
#     For prolog you can use write but there are better ways

#!/bin/bash
function Solution
{
    function main
    {
        echo 'Hello World!'
    }
    main
}
Solution