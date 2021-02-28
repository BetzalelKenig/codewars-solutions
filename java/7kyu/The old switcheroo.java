// Write a function

// vowel2Index(String s)

// that takes in a string and replaces all the vowels [a,e,i,o,u] with their respective positions within that string.
// E.g:

// Kata.Vowel2Index("this is my string") == "th3s 6s my str15ng"
// Kata.Vowel2Index("Codewars is the best site in the world") == "C2d4w6rs 10s th15 b18st s23t25 27n th32 w35rld"

// Your function should be case insensitive to the vowels.

//🐙🤺
public class Kata {
  public static String vowel2Index(String s) {
    String v = " aeiou";
    String[] arr = s.split("");
    for(int i = 0; i < arr.length; i++){
      if(v.indexOf(arr[i]) > 0){
        arr[i] = String.valueOf(i+1);
      }
    }
    return String.join("", arr);
  }
}