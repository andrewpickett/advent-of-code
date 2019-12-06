data = map(x -> parse(Int64, x), split(readline("input.txt"), ','))

function create_data_list(noun, verb)
	op_data = copy(data)
	op_data[2] = noun
	op_data[3] = verb
	return op_data
end

calculate_output(d) = for i in 1:4:length(d)
	if d[i] == 99
		return d[1]
	end
	outIdx = d[i + 3] + 1
	in1Idx = d[i + 1] + 1
	in2Idx = d[i + 2] + 1
	d[outIdx] = d[i] == 1 ? d[in1Idx] + d[in2Idx] : d[in1Idx] * d[in2Idx]
end

part_one() = calculate_output(create_data_list(12, 2))

part_two() = for noun in 1:100
	for verb in 1:100
		if calculate_output(create_data_list(noun, verb)) == 19690720
			return noun * 100 + verb
		end
	end
end

function main()
	println(part_one())
	println(part_two())
end

main()
