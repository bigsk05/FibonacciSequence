require "time"
def calc(n)
    if n <= 1
        return n
    else
        return calc(n - 1) + calc(n - 2)
    end
end
def main()
    ts=Time.now
    for i in 0..29
        #puts i
        #puts calc(i)
        calc(i)
    end
    tf=Time.now
    puts "["+(tf-ts).to_s+"]"
end
main()