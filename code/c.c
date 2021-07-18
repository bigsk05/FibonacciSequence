#include<stdio.h>
#include<sys/time.h>

long calc(long n){
	if (n <= 1){
        return n;
    }else{
        return (calc(n - 1) + calc(n - 2));
	}
}
int main(){
    struct timeval tv1, tv2;
    gettimeofday(&tv1, NULL);
	for (int i=0;i<30;i++){
        calc(i);
		//printf("%ld\n",calc(i));
        //fflush(stdout);
	}
    gettimeofday(&tv2, NULL);
	printf("[%f]\n",(double)(tv2.tv_sec-tv1.tv_sec)+(double)(tv2.tv_usec-tv1.tv_usec)/1000000);
	return 0;
}
