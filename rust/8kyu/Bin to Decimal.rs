// Complete the function which converts a binary number (given as a string) to a decimal number.

fn bin_to_decimal(inp: &str) -> i32 {
    i32::from_str_radix(inp, 2).unwrap()
}