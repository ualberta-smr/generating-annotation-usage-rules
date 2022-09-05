from zipfile import ZipFile

namespace = "org/eclipse/microprofile/"

jarFiles = [
    # "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/cdi-api-2.0.jar",
    # "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/jakarta.annotation-api-2.1.1.jar",
    # "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/jakarta.enterprise.cdi-api-4.0.0.jar",
    # "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/jakarta.inject-api-2.0.1.jar",
    # "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/jakarta.persistence-api-3.1.0.jar",
    # "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/jakarta.servlet-api-6.0.0.jar",
    # "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/jakarta.validation-api-3.0.2.jar",
    # "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/jakarta.ws.rs-api-3.1.0.jar",
    # "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/javax.inject-1.jar",
    # "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/javax.ws.rs-api-2.1.1.jar",
    "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/microprofile-config-api-3.0.1.jar",
    "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/microprofile-fault-tolerance-api-3.0.jar",
    "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/microprofile-graphql-api-1.1.0.jar",
    "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/microprofile-health-api-3.0.jar",
    "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/microprofile-jwt-auth-api-1.2.jar",
    "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/microprofile-metrics-api-4.0.jar",
    "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/microprofile-openapi-api-2.0.jar",
    "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/microprofile-reactive-messaging-api-2.0.jar",
    "../../violation-detector/violation-detector-maven-plugin/src/main/resources/lib/microprofile-rest-client-api-2.0.jar"
]

for jar in jarFiles:
    zip = ZipFile(jar)
    for name in zip.namelist():
        if not name.endswith(".class") and name.startswith(namespace):
            if 1 == len(name.split(namespace)[1][:-1].split("/")) and name != namespace:
                print(name)