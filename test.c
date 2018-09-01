/*author: rameez
date: 1st september 20018
*/

#include<stdio.h>					
#include<stdlib.h>
#include<unistd.h>						//linux library used for fork.
#include<string.h>						//dealing with the string and string concatenation

char pre[10]="echo \"";					//system command string is split into three parts pre,data and post
char post[30]="\" > /dev/ttyUSB0";		//actual data to be sent is taken into data variable
char data[20]="hello";
char sumup[50]="";						//final data is concatenated into this string

void main()
{
	int i= fork();						//process creates a second copy of itself

	/*if return of fork is 0 (zero) then it is parent process and positive value is pid of forked process
	**with the if else loop parent process is made to show output of incoming string
	**while child process is used to send data to port*/
	
	if(i==0)						//parent process
		
	   system("lxterminal -t output_terminal -e cat /dev/ttyUSB0");

	else							//child process
	   {
	  	 while(1)
		 {
		   printf("input a character\n");		//asks for user input
		   scanf("%s" , &data);
		   strcat(sumup,pre);					//the final command is made by concatenating strings with variable named sumup
           strcat(sumup,data);
           strcat(sumup,post);
		   printf("\n\n\n\t\t\tdata is %s\t:::%d\n\n\n", sumup ,getpid());	//shows the final command to be sent(for debugging purpose only!)
		   system(sumup);						//crux of the code! executes the string on system shell

		 }

	   }
}

