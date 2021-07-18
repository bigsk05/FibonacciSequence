function calc(n){
    if (n <= 1){
        return n;
    }
    return (calc(n - 1) + calc(n - 2));
}
function main(){
    var ts = new Date();
    for (i=0;i<30;i++){
        //console.log(calc(i));
        calc(i)
    }
    var tf = new Date();
    console.log("["+((tf-ts)/1000)+"]");
}
main()