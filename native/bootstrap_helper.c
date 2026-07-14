#include <errno.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <unistd.h>

static int executable_dir(char *buffer, size_t size) {
    ssize_t length = readlink("/proc/self/exe", buffer, size - 1);
    if (length < 0 || (size_t) length >= size) {
        return -1;
    }

    buffer[length] = '\0';
    char *slash = strrchr(buffer, '/');
    if (slash == NULL) {
        errno = EINVAL;
        return -1;
    }

    *slash = '\0';
    return 0;
}

int main(void) {
    char root[PATH_MAX];
    char artifact_dir[PATH_MAX];
    char bootstrap_path[PATH_MAX];

    if (executable_dir(root, sizeof(root)) != 0) {
        perror("downloader: unable to resolve executable directory");
        return 1;
    }

    if (snprintf(artifact_dir, sizeof(artifact_dir), "%s/artifacts", root) >= (int) sizeof(artifact_dir)) {
        fprintf(stderr, "downloader: artifact path is too long\n");
        return 1;
    }

    if (mkdir(artifact_dir, 0775) != 0 && errno != EEXIST) {
        perror("downloader: unable to create artifacts directory");
        return 1;
    }

    if (snprintf(bootstrap_path, sizeof(bootstrap_path), "%s/bootstrap.json", artifact_dir) >= (int) sizeof(bootstrap_path)) {
        fprintf(stderr, "downloader: bootstrap path is too long\n");
        return 1;
    }

    FILE *handle = fopen(bootstrap_path, "w");
    if (handle == NULL) {
        perror("downloader: unable to write bootstrap file");
        return 1;
    }

    const char *payload =
        "{\n"
        "  \"event\": \"downloader_executed\",\n"
        "  \"component\": \"downloader\",\n"
        "  \"scope\": \"repository-local\",\n"
        "  \"safe\": true\n"
        "}\n";

    if (fwrite(payload, 1, strlen(payload), handle) != strlen(payload)) {
        perror("downloader: unable to persist bootstrap file");
        fclose(handle);
        return 1;
    }

    if (fclose(handle) != 0) {
        perror("downloader: unable to close bootstrap file");
        return 1;
    }

    printf("Bootstrap record written to %s\n", bootstrap_path);
    return 0;
}
