use std::collections::HashMap;

fn main() {
    let s = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.";
    let e: Vec<&str> = s.split_whitespace()
        .enumerate()
        .map(|(i, w)| match i+1 {
            1 | 5 | 6 | 7 | 8 | 9 | 15 | 16 | 19 => &w[..1],
            _ => &w[..2]
            })
        .collect();

    let mut elements = HashMap::new();
    for (i, e) in e.into_iter().enumerate() {
        elements.insert(e, i+1);
    }
    println!("{:?}", elements);
}
