// Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.
// Examples

// "This is an example!" ==> "sihT si na !elpmaxe"
// "double  spaces"      ==> "elbuod  secaps"

//🐙🤺
public class Kata
{
  public static String reverseWords(final String original)
  {
    if(original.trim().isEmpty()){return original;}
    String[] arr = original.split(" ");
    for(int i = 0; i < arr.length; i++){
      arr[i] = new StringBuilder(arr[i]).reverse().toString();
    }
    return String.join(" ", arr);
  }