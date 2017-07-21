fn main() {
    let s = String::from("パタトクカシーー");
    let s = s.chars()
        .enumerate()
        .filter(|&(i, _)| i % 2 == 0)
        .map(|(_, x)| x)
        .collect::<String>();
    println!("{}", s);
}
