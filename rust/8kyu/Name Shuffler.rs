// Write a function that returns a string in which firstname is swapped with last name.

// Example(Input --> Output)

// "john McClane" --> "McClane john"

fn name_shuffler(s: &str) -> String {
    let words: Vec<&str> = s.split_whitespace().collect();
    words[1].to_owned() + " " + words[0]
}