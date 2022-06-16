// This kata is about converting numbers to their binary or hexadecimal representation:

//     If a number is even, convert it to binary.
//     If a number is odd, convert it to hex.

// Numbers will be positive. The hexadecimal string should be lowercased.

fn evens_and_odds(n: u64) -> String {
    if n % 2 == 0 {
        format!("{:b}", n)
    } else {
        format!("{:x}", n)
    }
}