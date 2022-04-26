// Rules:

//     Each character has its own power:

//       A = 1, B = 2, ... Y = 25, Z = 26
//       a = 0.5, b = 1, ... y = 12.5, z = 13

//     Only alphabetical characters can and will participate in a battle.
//     Only two groups to a fight.
//     Group whose total power (a + B + c + ...) is bigger wins.
//     If the powers are equal, it's a tie.

// Examples:

//   battle("One", "Two"); // => "Two"`
//   battle("ONE", "NEO"); // => "Tie!"

#include <ctype.h>

const char *battle (const char *group_1, const char *group_2)
{
  float x = 0, y = 0;
  for (int i = 0; group_1[i] != '\0'; i++) {
    if (isupper(group_1[i])) {
      x += group_1[i] - 64;
    } else {
      x += ((float) group_1[i] - 96) / 2; 
    }
  }
  for (int i = 0; group_2[i] != '\0'; i++) {
      if (isupper(group_2[i])) {
        y += group_2[i] - 64;
      } else {
        y += ((float) group_2[i] - 96) / 2; 
      }
    }
  if (x > y) return group_1;
  if (y > x) return group_2;
  return  "Tie!";
}