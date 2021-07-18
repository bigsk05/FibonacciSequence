#!/usr/bin/env Rscript
calc <- function(n){
    if (n <= 1){
        return(n)    
    }else{
        return(calc(n - 1) + calc(n - 2))
    }
}
main <- function(){
    ts=proc.time()
    for ( i in seq(from = 0, to = 29, by = 1)){
        calc(i)
        #print(calc(i))
    }
    tf=proc.time()
    print(paste0("[",(tf-ts)[3][[1]],"]"))
}
main()