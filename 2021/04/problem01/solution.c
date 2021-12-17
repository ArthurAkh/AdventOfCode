#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/stat.h>

#define FILENAME "file"
#define HEIGHT 5
#define WIDTH 5
#define TOTALNUMBERS 100

int getWinner(int boolean[][HEIGHT+1][WIDTH+1], int x, int y, int z) {

    // for each card
    for (int i = 0; i < x; ++i) {
        // for each line
        for (int j = 0; j < y; ++j) {
            if(boolean[i][j][z] == z)
                return i;
        }
        // for each column
        for (int k = 0; k < z; ++k) {
            if (boolean[i][y][k] == y) {
                return i;
            }
        }
    }
    return -1;
}

void simulateStep(int ***array, int boolean[][HEIGHT+1][WIDTH+1], int* numbers, int x, int y, int z, int index) {

    int bingoDigit = numbers[index];

    for (int i = 0; i < x; ++i) {
        for (int j = 0; j < y; ++j) {
            for (int k = 0; k < z; ++k) {
                if (array[i][j][k] == bingoDigit) {
                    boolean[i][j][k] = 1;
                    ++boolean[i][j][z];
                    ++boolean[i][y][k];
                    goto loopInCards;
                }
            }
        }
        loopInCards:
    }
}

int getSumOfUnmarked(int ***array, int boolean[][HEIGHT+1][WIDTH+1], int y, int z, int indexWinner) {

    int sum = 0;

    int i = indexWinner;

    for (int j = 0; j < y; ++j) {
        for (int k = 0; k < z; ++k) {
            if (!boolean[i][j][k]) {
                sum += array[i][j][k];
            }
        }
    }

    return sum;
}

int main() {
    const char file_name[] = FILENAME;
    FILE *fp;

    /* OPENING OF THE FILE */
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

    int size = TOTALNUMBERS;

    int *bingoNumbers = (int *) calloc(size, sizeof(int));

    fscanf(fp, "%s", file_contents); 

    char *temp;
    temp = strtok (file_contents, ",");

    int i = 0;

    while (temp != NULL) {
        int a = atoi(temp);
        bingoNumbers[i++]= a;
        temp = strtok (NULL, ",");

        if(i >= size) {
            size *= 2;
            bingoNumbers = (int *) realloc(bingoNumbers, sizeof(int));
        }
    }

    int bingoLength = i;
    int bingoCardsNumber = 10;

    int *tempLines = malloc (bingoCardsNumber * (HEIGHT + 1) * (WIDTH + 1) * sizeof(int));
    int ***bingoCards = (int ***) malloc(bingoCardsNumber * sizeof(int **));

    if(!bingoCards) {
        fprintf(stderr, "Out of Memory");
        exit(0);
    }

    for (i = 0; i < bingoCardsNumber; ++i) {
        bingoCards[i] = malloc ((HEIGHT + 1) * sizeof(int **));
        for (int j = 0; j < (HEIGHT + 1); ++j) {
            bingoCards[i][j] = tempLines + (bingoCardsNumber * (HEIGHT + 1) * (WIDTH + 1)) + (HEIGHT+WIDTH + 2); 
        }
    } 

    int index = 0;

    while (1) {

        int lineNumbers[WIDTH];
        /* int bingoCard[HEIGHT][WIDTH]; */
        int **bingoCard = (int **) malloc((HEIGHT+1) * sizeof(int *));

        for (i = 0; i < HEIGHT+1; i++)
            bingoCard[i] = (int *) malloc((WIDTH+1) * sizeof(int));

        for(int line = 0; line < HEIGHT; ++line) {

            i = 0;

            /* while (temp != NULL) { */
            while (i < WIDTH) {

                if(fscanf(fp, "%s", file_contents) == EOF) {
                    goto endOfFile;
                }
                temp = strtok (file_contents, " ");

                int a = atoi(temp);
                lineNumbers[i++]= a;
            }
            // copying the line to the entire 5x5 card at position line
            for(i = 0; i < WIDTH; ++i) {
                bingoCard[line][i] = lineNumbers[i];
            }
        }
        // copying the card to the list of cards
        memcpy(bingoCards[index++], bingoCard, HEIGHT * WIDTH * sizeof(int));

        if (index >= bingoCardsNumber) {
            bingoCardsNumber*=2;

            bingoCards = (int ***) realloc(bingoCards, bingoCardsNumber * sizeof(int **));

            for (i = index; i < bingoCardsNumber; ++i) {
                bingoCards[i] = malloc ((HEIGHT + 1) * sizeof(int **));
                for (int j = 0; j < (HEIGHT + 1); ++j) {
                    bingoCards[i][j] = tempLines + (bingoCardsNumber * (HEIGHT + 1) * (WIDTH + 1)) + (HEIGHT+WIDTH + 2); 
                }
            }
        }
    }

    endOfFile: 

    bingoCardsNumber = index;

    i = 0;

    free(tempLines);

    int bingoCardsBoolean[bingoCardsNumber][HEIGHT+1][WIDTH+1];
    memset(bingoCardsBoolean, 0, sizeof bingoCardsBoolean);


 
    int winner;

    while(1) {

        simulateStep(bingoCards, bingoCardsBoolean, bingoNumbers, bingoCardsNumber, HEIGHT, WIDTH, i);

        winner = getWinner(bingoCardsBoolean, bingoCardsNumber, HEIGHT, WIDTH);
        if (winner != -1) {
            break;
        }

        i++;
    }

    int sum = getSumOfUnmarked(bingoCards, bingoCardsBoolean, WIDTH, HEIGHT, winner);

    int lastDigit = bingoNumbers[i];

    sum *= lastDigit;

    printf("sum: %d\n", sum);
 
    free(bingoCards);

    fclose(fp);

    return 0;
}
