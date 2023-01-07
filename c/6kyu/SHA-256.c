// Create a function that converts a given ASCII string to its hexadecimal SHA-256 hash.

// sha256("Hello World!") => "7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069"

#include <stdlib.h>
#include <string.h>
#include <openssl/sha.h>

/* Compute the SHA-256 hash of a string and store it in the output buffer */
char *sha256(char *hash, const char *string)
{
    unsigned char digest[SHA256_DIGEST_LENGTH];
    SHA256_CTX ctx;

    SHA256_Init(&ctx);
    SHA256_Update(&ctx, string, strlen(string));
    SHA256_Final(digest, &ctx);

    for (int i = 0; i < SHA256_DIGEST_LENGTH; i++)
    {
        sprintf(hash + (i * 2), "%02x", digest[i]);
    }
    hash[SHA256_DIGEST_LENGTH * 2] = '\0';

    return hash;
}