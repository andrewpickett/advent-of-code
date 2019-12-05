data = map(x -> parse(Int64, x), readlines("day1/input.txt"))

calc_spec_fuel(val) = convert(Int64, floor(val / 3)) - 2

function calc_total_fuel(start)
	n = calc_spec_fuel(start)
	if n <= 0
		return 0
	end
	return n + calc_total_fuel(n)
end

part_one() = sum(map(calc_spec_fuel, data))
part_two() = sum(map(calc_total_fuel, data))

function main()
   println(part_one())
   println(part_two())
end

main()
