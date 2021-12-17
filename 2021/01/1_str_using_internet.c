#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_PARAMS 10
#define MAX_WORDS 10000

main () {

    char string[] = "12
        13
        10
        11";

    parse(string);

    




    return 0;
}

void parse(char *input) {
    int i, param = 0, buff_count = 0;
    char buffer[MAX_WORDS];

    for (i=0; input[i] && param < MAX_PARAMS; i++) {
        if((isspace(input[i]) && *buffer)) {
            add_param(params)
        }
    }
}
