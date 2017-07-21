fn main() {
    let s1 = String::from("パトカー");
    let s2 = String::from("タクシー");
    let mut s = String::new();
    for (c1, c2) in s1.chars().zip(s2.chars()) {
        s.push(c1);
        s.push(c2);
    }
    println!("{}", s);
}
