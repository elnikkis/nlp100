fn main() {
    let s = String::from("stressed");
    let s = s.chars().rev().collect::<String>();
    println!("{}", &s);
}
