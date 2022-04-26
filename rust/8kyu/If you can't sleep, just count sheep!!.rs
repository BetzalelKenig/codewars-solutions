// If you can't sleep, just count sheep!!
// Task:

// Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.

use std::fmt::Write;

fn count_sheep(n: u32) -> String {
    // (1..=n).map(|x| format!("{} sheep...", x)).collect()
    let mut res = String::new();
    for i in 1..n+1 {
        write!(&mut res, "{} {}", &i.to_string(), "sheep...").unwrap();
    }
    return res;
}
