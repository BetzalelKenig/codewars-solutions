// Complete the solution so that the function will break up camel casing, using a space between words.
// Example

// solution("camelCasing")  ==  "camel Casing"

//🐙🤺
class Solution {
  public static String camelCase(String input) {
    return String.join(" ", input.split("(?<=[a-z])(?=[A-Z])")); 
  }
}