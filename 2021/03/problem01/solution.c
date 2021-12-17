#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/stat.h>

#define BYTE_TO_BINARY_PATTERN "%c%c%c%c%c%c%c%c"
#define BYTE_TO_BINARY(byte)  \
      (byte & 0x80 ? '1' : '0'), \
        (byte & 0x40 ? '1' : '0'), \
          (byte & 0x20 ? '1' : '0'), \
            (byte & 0x10 ? '1' : '0'), \
              (byte & 0x08 ? '1' : '0'), \
                (byte & 0x04 ? '1' : '0'), \
                  (byte & 0x02 ? '1' : '0'), \
                    (byte & 0x01 ? '1' : '0') 

int main() {
    char ch;
    const char file_name[] = "file";
    FILE *fp;

    fp = fopen(file_name, "r");

    if (!fp) {
        perror("Error while opening the file.\n");
        exit(EXIT_FAILURE);
    }



    struct stat sb;
    if (stat(file_name, &sb) == -1) {
        perror("stat");
        exit(EXIT_FAILURE);
    }

    char *file_contents = malloc(sb.st_size);

    int binary = 0;
    int gamma = 0;
    int epsilon = 0;


    int numberOfOnesInFirst     = 0;
    int numberOfOnesInSecond    = 0;
    int numberOfOnesInThird     = 0;
    int numberOfOnesInFourth    = 0;
    int numberOfOnesInFifth     = 0;
    int numberOfOnesInSixth     = 0;
    int numberOfOnesInSeventh   = 0;
    int numberOfOnesInEighth     = 0;
    int numberOfOnesInNineth    = 0;
    int numberOfOnesInTenth     = 0;
    int numberOfOnesInEleventh  = 0;
    int numberOfOnesInTwelveth  = 0;

    
    /* while (fscanf(fp, "%[^\n ] ", file_contents) != EOF) { */
    while (fscanf(fp, "%s", file_contents) != EOF) {

        /* printf("> %s\n", file_contents); */
        
        binary = strtol(file_contents, NULL, 2);

        /* printf("binary: %d\n", binary); */

        numberOfOnesInFirst+=(binary>>11) & 01;
        numberOfOnesInSecond+=(binary>>10) & 01;
        numberOfOnesInThird+=(binary>>9) & 01;
        numberOfOnesInFourth+=(binary>>8) & 01;
        numberOfOnesInFifth+=(binary>>7) & 01;
        numberOfOnesInSixth+=(binary>>6) & 01;
        numberOfOnesInSeventh+=(binary>>5) & 01;
        numberOfOnesInEighth+=(binary>>4) & 01;
        numberOfOnesInNineth+=(binary>>3) & 01;
        numberOfOnesInTenth+=(binary>>2) & 01;
        numberOfOnesInEleventh+=(binary>>1) & 01;
        numberOfOnesInTwelveth+=(binary) & 01;

        /* printf("numberOfOnesInFirst: %d\n", numberOfOnesInFirst); */
    }

    if(numberOfOnesInFirst > 500) {
        gamma+=1<<11;
    } else {
        epsilon+=1<<11;
    }
        
    if(numberOfOnesInSecond > 500) {
        gamma+=1<<10;
    } else {
        epsilon+=1<<10;
    }


    if(numberOfOnesInThird > 500) {
        gamma+=1<<9;
    } else {
        epsilon+=1<<9;
    }


    if(numberOfOnesInFourth > 500) {
        gamma+=1<<8;
    } else {
        epsilon+=1<<8;
    }


    if(numberOfOnesInFifth > 500) {
        gamma+=1<<7;
    } else {
        epsilon+=1<<7;
    }


    if(numberOfOnesInSixth > 500) {
        gamma+=1<<6;
    } else {
        epsilon+=1<<6;
    }


    if(numberOfOnesInSeventh > 500) {
        gamma+=1<<5;
    } else {
        epsilon+=1<<5;
    }


    if(numberOfOnesInEighth > 500) {
        gamma+=1<<4;
    } else {
        epsilon+=1<<4;
    }


    if(numberOfOnesInNineth > 500) {
        gamma+=1<<3;
    } else {
        epsilon+=1<<3;
    }


    if(numberOfOnesInTenth > 500) {
        gamma+=1<<2;
    } else {
        epsilon+=1<<2;
    }



    if(numberOfOnesInEleventh > 500) {
        gamma+=1<<1;
    } else {
        epsilon+=1<<1;
    }



    if(numberOfOnesInTwelveth > 500) {
        gamma+=1;
    }else {
        epsilon+=1<<1;
    }


    /* epsilon = ~gamma; */
    /* epsilon = epsilon & 0111111111111; */ 

    printf("gamma in binary: "BYTE_TO_BINARY_PATTERN"\n", BYTE_TO_BINARY(gamma));

    printf("gamma rate: %d\n", gamma);

    printf("epsilon in binary: "BYTE_TO_BINARY_PATTERN"\n", BYTE_TO_BINARY(epsilon));
    printf("epsilon rate: %d\n", epsilon);
    printf("gamma*epsilon: %d\n", gamma*epsilon);



    fclose(fp);
    exit(EXIT_SUCCESS);

    return 0;
}
