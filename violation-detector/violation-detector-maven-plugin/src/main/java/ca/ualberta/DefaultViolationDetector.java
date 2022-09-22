package ca.ualberta;

import ca.ualberta.smr.detection.ViolationDetector;
import ca.ualberta.smr.detection.clazz.ClassAnalyzer;
import ca.ualberta.smr.detection.field.FieldAnalyzer;
import ca.ualberta.smr.detection.method.MethodAnalyzer;
import ca.ualberta.smr.model.StaticAnalysisRule;
import ca.ualberta.smr.model.violationreport.ViolationCombination;
import lombok.SneakyThrows;
import lombok.val;

import java.io.*;
import java.util.*;
import static ca.ualberta.smr.parsing.utils.GeneralUtility.listOf;

public class DefaultViolationDetector {

    private final ViolationDetector violationDetector;

    @SneakyThrows
    public DefaultViolationDetector(final RuleProvider ruleProvider, TypeResolverProvider typeResolverProvider) {
        val rules = ruleProvider.getRules();
        val typeResolver = typeResolverProvider.getTypeResolver();
        val analyzers = listOf(new ClassAnalyzer(), new MethodAnalyzer(), new FieldAnalyzer());
        this.violationDetector = new ViolationDetector(typeResolver, rules, analyzers);
    }



    public Map<StaticAnalysisRule, Collection<ViolationCombination>> analyze(File file) {
        return violationDetector.detectViolations(file.getAbsolutePath());
    }

}