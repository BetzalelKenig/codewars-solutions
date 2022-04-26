// Write a function that will check if two given characters are the same case.

// 'a' and 'g' returns 1

// 'A' and 'C' returns 1

// 'b' and 'G' returns 0

// 'B' and 'g' returns 0

// '0' and '?' returns -1

// If any of characters is not a letter, return -1.

// If both characters are the same case, return 1.

// If both characters are letters and not the same case, return 0.

int isUpper(char letter) {
  return letter > 64 && letter < 91;
}

int isLower(char letter) {
  return letter > 96 && letter < 123;
}

int same_case (char a, char b) {
  if ( (!isUpper(a) && !isLower(a)) || (!isUpper(b) && !isLower(b)) ) {
    return -1;
  }
  
  if ( isUpper(a) == isUpper(b) || isLower(a) == isLower(b) ) {
    return 1;
  }
  
  return 0;
}