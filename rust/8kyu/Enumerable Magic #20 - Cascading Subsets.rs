// Create a method each_cons that accepts a list and a number n, and returns cascading subsets of the list of size n, like so:

// each_cons([1,2,3,4], 2)
//   #=> [[1,2], [2,3], [3,4]]

// each_cons([1,2,3,4], 3)
//   #=> [[1,2,3],[2,3,4]]
  

// As you can see, the lists are cascading; ie, they overlap, but never out of order.

fn each_cons(arr: &[u8], n: usize) -> Vec<Vec<u8>> {
    let mut res: Vec<Vec<u8>> = Vec::new();
    if arr.len() == 0 { return res; }
    let s: i32 = (arr.len() as i32) - ((n as i32) - 1);
    for e in 0..s {
        let mut iner_vec: Vec<u8> = Vec::new();
        for (i, el) in arr.iter().enumerate() {
            if (i as i32) >= (e as i32) && (i as i32) < (e as i32) + (n as i32){
            iner_vec.push(*el);    
            }
        }
        res.push(iner_vec);
    }
    res
}