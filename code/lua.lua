function calc(n)
    if n <= 1 then
        return n
    else
        return calc(n - 1) + calc(n - 2)
    end
end
function main()
    local ts = os.clock()
    for i=0,29,1 do
        --print(calc(i))
        calc(i)
    end
    local tf = os.clock()
    print(string.format("[%f]",tf-ts))
end
main()