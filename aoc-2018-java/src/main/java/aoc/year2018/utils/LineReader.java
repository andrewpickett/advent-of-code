package aoc.year2018.utils;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

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
}
