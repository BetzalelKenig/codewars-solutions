// Write function RemoveExclamationMarks which removes all exclamation marks from a given string.

#include <string.h>

void remove_exclamation_marks(const char *str_in, char *str_out) {
    int i, j;
    int len = strlen(str_in);
  
    for(i = j = 0; i < len; i++) {
      
        if(str_in[i] != '!') {
          str_out[j] = str_in[i];
          j++;
        }
    }
    str_out[j] = '\0';
}