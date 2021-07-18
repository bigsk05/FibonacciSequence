<?php 
function calc($n){
    if ($n <= 1){
        return $n;
    }else{
        return (calc($n - 1) + calc($n - 2));
    }
}
function main(){
    $ts=microtime();
    for ($i=0;$i<30;$i++){
        //echo calc($i);
        calc($i);
    }
    $used=microtime()-$ts;
    if ($used<0){
        $used=0;
    }
    echo "[".$used."]\n";
}
@main()
?>