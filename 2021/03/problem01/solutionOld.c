#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/stat.h>

int main() {
    char ch;
    const char file_name[] = "file";
    FILE *fp;

    fp = fopen(file_name, "r");

    if (!fp) {
        perror("Error while opening the file.\n");
        exit(EXIT_FAILURE);
    }

    int number;
    int xDist = 0;
    int depth = 0;

    char arr[100];
    /* char command[20]; */
    char forward[]="forward";
    char up[]="up";
    char down[]="down";


    struct stat sb;
    if (stat(file_name, &sb) == -1) {
        perror("stat");
        exit(EXIT_FAILURE);
    }

    char *file_contents = malloc(sb.st_size);


    /* while (fscanf(fp, "%[^\n ] ", file_contents) != EOF) { */
    while (fscanf(fp, "%s", file_contents) != EOF) {

        /* printf("> %s\n", file_contents); */

        //forward, down up
        /* command = file_contents; */
        /* command = strtok(file_contents, ""); */
        if(!strcmp(file_contents, forward)) {
            fscanf(fp, "%s", file_contents);

            number = strtol(file_contents, NULL, 10);
            xDist+=number;

    
        } else if(!strcmp(file_contents, up)) {
            fscanf(fp, "%s", file_contents);

            number = strtol(file_contents, NULL, 10);
            depth-=number;


        } else {
            fscanf(fp, "%s", file_contents);

            number = strtol(file_contents, NULL, 10);
            depth+=number;


        }
        /* fscanf(fp, "%d", file_contents); */

        /* number = strtol(file_contents, NULL, 10); */
        /* /1* number = file_contents; *1/ */

        

    }

    printf("xDist: %d\n", xDist);
    printf("depth: %d\n", depth);
    printf("xDist*depth: %d\n", depth*xDist);



    fclose(fp);
    exit(EXIT_SUCCESS);

    return 0;
}
