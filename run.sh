ms=/home/owary/Programming/Research/Annotation-Violation-Detector/complete-detector-experiment/detector-evaluation/target_projects
ps=/home/owary/Programming/Research/Annotation-Violation-Detector/project/generating-annotation-usage-rules/violation-detector/violation-detector-maven-plugin/src/main/resources/lib
image=demo1
docker run  -it \
            -v $ms:/pipeline/mining-sources \
            -v $ps:/pipeline/lib-sources $image