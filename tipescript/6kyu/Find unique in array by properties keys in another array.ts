// Your task is to return unique objects from an array.

// You will receive two arrays, objs and keys. Unique objects mean that the object properties defined on keys are unique, for example:

// // keys
// [ 'x', 'y' ]

// // objs
// { x: 1, y: 1 },
// { x: 2, y: 2 },
// { x: 1, z: 1 },
// { x: 1, y: 1, z: 3 },
// The expected result is:

// { x: 1, y: 1 },
// { x: 2, y: 2 },
// { x: 1, z: 1 },
// Because x and y repeat on the first and last element, so only the first will be picked up.

// If a key is not present in the object the value of this property will be considered "not defined" native value for the current language.

export function unique(arr: any[], keys: string[]) {
    const seen = new Set();

    return arr.filter(obj => {
        const keyValues = keys.map(key => obj[key]);
        const keyString = keyValues.join(',');

        if (!seen.has(keyString)) {
            seen.add(keyString);
            return true;
        }
        return false;
    });
}