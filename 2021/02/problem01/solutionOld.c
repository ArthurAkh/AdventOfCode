#include <errno.h>
#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    /* char string[] = "test 1, 2, 3!"; */
    /* char ch, file_name[25]; */
    char ch;
    char file_name[] = "file";
    FILE *fp;
    /* char *found; */

    /* /1* file_name = "file"; *1/ */
    fp = fopen(file_name, "r");

    if (fp == NULL) {
        perror("Error while opening the file.\n");
        exit(EXIT_FAILURE);
    }

    /* printf("Original: '%s'\n", string); */

    /* found = strtok(string, " "); */

    /* if (found == NULL) { */
    /*     printf("\t'%s'\n", string); */
    /*     puts("\tNoseparators found"); */
    /*     return 1; */
    /* } */
    /* while(found) { */
    /*     printf("\t'%s'\n", found); */
    /*     found = strtok(NULL, " "); */
    /* } */

    int counter = 0;
    int current;
    int previousOne = -99999999;
    int previousTwo = -9999999;
    int previousSum = 999999;
    int sum = 0;


    char arr[100];
    char* ptr;

    /* for(int it = 0; it < 20; it++) { */
    for(;;) {

        if(!fgets(arr, sizeof arr, fp))
            break;

        ptr = strtok(arr, "");

        current = strtol(ptr, NULL, 10);
        
        if(previousTwo > 0 && previousOne > 0) {

            sum = current + previousOne + previousTwo;
            
            if(sum > previousSum)
                counter++;

            printf("sum: %d, current: %d, counter: %d\n", sum, current, counter);

        previousSum = sum;
        }
        
        ptr = strtok(NULL, "\n");

        previousTwo = previousOne;
        previousOne = current;
    }

    printf("counter: %d\n", counter);

    /* for (;;) { */
    /*     errno = 0; */
    /*     char *end; */
    /*     const long i = strtol(fp, &end, 10); */
    /*     if (p == end) */
    /*         break; */

    /*     const bool range_error = errno == ERANGE; */

    /*     if(previous != NULL && i > previous) counter++; */

    /*     previous = i; */
    /*     p = end; */

    /*     if (range_error) */
    /*         prinf("Range error occured."); */

    /*     putchar('\n'); */
    /* } */





    /* char first = fgetc(fp); */
    /* int previous = strtol(first, NULL, 10); */

    /* while((ch = fgetc(fp)) != EOF) { */
    /*     int current = strtol(ch, NULL, 10); */
    /*     if (current > previous) { */
    /*         counter++; */
    /*     } */
    /*     previous = current; */

    /*     /1* printf("%c", ch); *1/ */
    /* } */

    /* fclose(fp); */

    return 0;
}
