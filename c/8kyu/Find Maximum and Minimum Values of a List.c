// Your task is to make two functions, max and min (maximum and minimum in PHP and Python) that take a(n) array/vector of integers list as input and outputs, respectively, the largest and lowest number in that array/vector.

// #Examples

// max({4,6,2,1,9,63,-134,566}) returns 566
// min({-52, 56, 30, 29, -54, 0, -110}) returns -110
// max({5}) returns 5
// min({42, 54, 65, 87, 0}) returns 0
// #Notes

// You may consider that there will not be any empty arrays/vectors.

int min(int *array, int arrayLength)
{
    int min = array[0];
    while (arrayLength)
    {
        if (array[--arrayLength] < min)
            min = array[arrayLength];
    }
    return min;
}

int max(int *array, int arrayLength)
{
    int max = array[0];
    while (arrayLength)
    {
        if (array[--arrayLength] > max)
            max = array[arrayLength];
    }
    return max;
}