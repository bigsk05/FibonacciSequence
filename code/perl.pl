sub calc{
    if ($_[0] <= 1){
        return $_[0];
    }
    return (calc($_[0] - 1) + calc($_[0] - 2));
}
sub main{
    use Time::HiRes qw(gettimeofday tv_interval); 
     my $start_time = [gettimeofday];
    for ($i=0;$i<30;$i=$i+1){
        #print calc($i);
        #print "\n";
        calc($i)
    }
    my $interval=tv_interval($start_time,[gettimeofday]); 
    print "[$interval]\n"; 
}
main()