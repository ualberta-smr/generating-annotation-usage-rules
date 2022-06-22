package ca.ualberta.smr.deprecated.model;

import com.github.javaparser.Range;
import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
public class ViolationRange {

    private final int lineStart;
    private final int colStart;
    private final int lineEnd;
    private final int colEnd;

    public ViolationRange(Range range) {
        this(range.begin.line, range.begin.column, range.end.line, range.end.column);
    }

    @Override
    public String toString() {
        return String.format("(line %d, col %d) - (line %d, col %d)", lineStart, colStart, lineEnd, colEnd);
    }
}
