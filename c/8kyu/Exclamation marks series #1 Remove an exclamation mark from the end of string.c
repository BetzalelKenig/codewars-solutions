// Description:

// Remove an exclamation mark from the end of a string. For a beginner kata, you can assume that the input data is always a string, no need to verify it.
// Examples

// remove("Hi!") === "Hi"
// remove("Hi!!!") === "Hi!!"
// remove("!Hi") === "!Hi"
// remove("!Hi!") === "!Hi"
// remove("Hi! Hi!") === "Hi! Hi"
// remove("Hi") === "Hi"

char *remove_mark (char *string)
{
	if (string[strlen(string)-1] == '!') {
    string[strlen(string)-1] = '\0';
  }
	return string;
}