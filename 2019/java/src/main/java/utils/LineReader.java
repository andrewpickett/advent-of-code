package utils;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public final class LineReader {

	private LineReader() {
	}

	public static List<String> readLines(final String filePath) {
		String f = ClassLoader.getSystemClassLoader().getResource(filePath).getFile();
		final List<String> list = new ArrayList<>();
		try (BufferedReader br = new BufferedReader(new FileReader(f))) {
			String line = br.readLine();
			while (line != null) {
				list.add(line);
				line = br.readLine();
			}
		} catch (IOException e) {
			e.printStackTrace();
		}
		return list;
	}

	public static List<Integer> readLinesAsInts(final String filePath) {
		return readLines(filePath).stream().map(Integer::valueOf).collect(Collectors.toList());
	}
}
