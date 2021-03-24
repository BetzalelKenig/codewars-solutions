// Create a function which answers the question "Are you playing banjo?".
// If your name starts with the letter "R" or lower case "r", you are playing banjo!

// The function takes a name as its only argument, and returns one of the following strings:

// name + " plays banjo"
// name + " does not play banjo"
// Names given are always valid strings.

#include <string.h>
#include <stdlib.h>
char *are_you_playing_banjo(const char *name)
{
    char *res;
    res = (char *)malloc(30);
    if (name[0] == 'R' || name[0] == 'r')
    {
        sprintf(res, "%s plays banjo", name);
    }
    else
    {
        sprintf(res, "%s does not play banjo", name);
    }
    return res;
}