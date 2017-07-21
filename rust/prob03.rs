fn main() {
    let s = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.";
    let pi: Vec<usize> = s.split_whitespace()
        .map(|w| w.trim_matches(','))
        .map(|w| w.trim_matches('.'))
        .map(|w| w.len()).collect();
    println!("{:?}", pi);
}
