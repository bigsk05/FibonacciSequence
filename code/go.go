package main

import (
	"fmt"
	"time"
)

func calc(n int) int {
    if (n <= 1){
        return n
    }
    return (calc(n - 1) + calc(n - 2))
}
func main()  {
	ts:=time.Now().UnixNano()
    for i:=0;i<30;i++{
        //fmt.Println(calc(i))
        calc(i)
    }
	fmt.Printf("["+fmt.Sprint(float64((time.Now().UnixNano()-ts))/1000000000.0)+"]")
}