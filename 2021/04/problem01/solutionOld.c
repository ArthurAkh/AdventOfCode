#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/stat.h>

#define LENGTH 12
#define TOTAL 1000

/* #define LENGTH 5 */
/* #define TOTAL 12 */

int determineNumberOfOnes (int *array, int size, int dist) {
    int counter = 0;
    for(int i = 0; i < size; ++i) {
        if ((*(array + i) >> dist) & 01 == 1) counter++;
    }

    return counter;
}

void * filterArray (int *arrayToFilter, int *arrayDestination, int size, int dist, int filter) {

    int counter = 0;

    for(int i = 0; i < size; ++i) {
        
        if (((*(arrayToFilter+i) >> dist) & 01) == filter) {
            *(arrayDestination + counter++) = *(arrayToFilter + i);
        }
    }
}

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

    int numbers[TOTAL];
    int i = 0;

    while (fscanf(fp, "%s", file_contents) != EOF) {
        /* printf("> %s\n", file_contents); */
        binary = strtol(file_contents, NULL, 2);
        numbers[i++] = binary;
        /* printf("binary: %d\n", binary); */
        /* numberOfOnesInFirst+=(binary>>11) & 01; */
        /* printf("numberOfOnesInFirst: %d\n", numberOfOnesInFirst); */
    }

    int numberOfOnes = determineNumberOfOnes(numbers, TOTAL, LENGTH - 1);
    int numberOfZeroes = TOTAL - numberOfOnes;

    int mostFilter;
    int fewFilter;
    int size;

    if (numberOfOnes >= numberOfZeroes) {
        mostFilter = 1;
        fewFilter = 0;
        size = numberOfOnes;
    } else {
        mostFilter = 0;
        fewFilter = 1;
        size = numberOfZeroes;
    }

    int *arrayMost = (int *) calloc(size, sizeof(int));
    if (!arrayMost) {
        printf("Error, memory not allocated!");
        exit;
    }

    int *arrayFew = (int *) calloc(TOTAL-size, sizeof(int));
    if (!arrayFew) {
        printf("Error, memory not allocated!");
        exit;
    }

    filterArray(numbers, arrayMost, TOTAL, LENGTH-1, mostFilter);
    filterArray(numbers, arrayFew, TOTAL, LENGTH-1, fewFilter);

    int counter = LENGTH-2;
    int newSize;
    int *temp;

    int originalSize = size;
    
    while (counter >= 0) {
        numberOfOnes = determineNumberOfOnes(arrayMost, size, counter);

        if (numberOfOnes >= size-numberOfOnes) {
            mostFilter = 1;
            newSize = numberOfOnes;
        } else {
            mostFilter = 0;
            newSize = size - numberOfOnes;
        }

        temp = (int *) calloc(newSize, sizeof(int));
        if (!temp) {
            printf("Couldn't allocate temp!");
            exit;
        }

        filterArray(arrayMost, temp, size, counter--, mostFilter);
        free(arrayMost);
        arrayMost = temp;

        size = newSize;
        if (size <= 1) break;
    }

    printf("counter = %d\n", counter);
    printf("newSize = %d\n", newSize);
    printf("arrayMost[0]: %d\n", *arrayMost);

    counter = LENGTH-2;
    size = TOTAL - originalSize;
    int filter;

    while (counter >= 0) {
        numberOfOnes = determineNumberOfOnes(arrayFew, size, counter);

        if (numberOfOnes >= size-numberOfOnes) {
            filter = 0;
            newSize = size - numberOfOnes;
        } else {
            filter = 1;
            newSize = numberOfOnes;
        }

        temp = (int *) calloc(newSize, sizeof(int));
        if (!temp) {
            printf("Couldn't allocate temp!");
            exit;
        }

        filterArray(arrayFew, temp, size, counter--, filter);
        free(arrayFew);
        arrayFew = temp;

        size = newSize;
        if (size <= 1) break;
    }

    printf("counter = %d\n", counter);
    printf("newSize = %d\n", newSize);
    printf("arrayFew[0]: %d\n", *arrayFew);

    printf("Few * Most = %d\n", (*arrayFew)*(*arrayMost));
    
    /* printf("gamma in binary: "BYTE_TO_BINARY_PATTERN"\n", BYTE_TO_BINARY(gamma)); */

    /* printf("gamma rate: %d\n", gamma); */

    /* printf("epsilon in binary: "BYTE_TO_BINARY_PATTERN"\n", BYTE_TO_BINARY(epsilon)); */
    /* printf("epsilon rate: %d\n", epsilon); */
    /* printf("gamma*epsilon: %d\n", gamma*epsilon); */

    fclose(fp);
    exit(EXIT_SUCCESS);

    return 0;
}
