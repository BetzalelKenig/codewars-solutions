// Yor task is to write function factorial

unsigned __int128 factorial(unsigned n)
{
    if (n < 1)
        return 1;
    else
        return n * factorial(n - 1);
}