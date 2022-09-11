package ca.ualberta;

import ca.ualberta.smr.typeresolution.TypeResolver;
import lombok.SneakyThrows;
import lombok.val;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Objects;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;

public class TypeResolverProvider {
    private final String jarZipFile;

    public TypeResolverProvider(String jarZipFile) {
        this.jarZipFile = jarZipFile;
    }

    private Collection<InputStream> loadJarFiles() throws IOException {
        val in = Objects.requireNonNull(getClass().getResourceAsStream(jarZipFile), "Libraries could not be loaded for type resolving");
        val zip = new ZipInputStream(in);

        Collection<InputStream> jarFiles = new ArrayList<>();
        for (ZipEntry ze = zip.getNextEntry(); ze != null; ze = zip.getNextEntry()) {
            val bos = new ByteArrayOutputStream();

            int read;
            while ((read = zip.read()) != -1) {
                bos.write(read);
            }

            byte[] buf = bos.toByteArray();
            val bis = new ByteArrayInputStream(buf);
            jarFiles.add(bis);
        }
        return jarFiles;
    }

    @SneakyThrows
    public TypeResolver getTypeResolver() {
        return new TypeResolver(loadJarFiles());
    }
}
