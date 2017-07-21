fn bigram<T: Iterator>(l: T) -> Iterator<Item=(T::Item, T::Item)> {
    let i1 = &l;
    let i2 = l.skip(1);
    i1.zip(i2)
}

fn abigram<T: Iterator>(l: T) -> Vec<(T::Item, T::Item)> {
    let mut res: (T::Item, T::Item) = Vec::new();
    let mut prev = &l.nth(0).unwrap();
    for i in l {
        res.push((*prev, i));
        let prev = &i;
    }
    return res
}

fn main() {
    let s = "I am an NLPer";
    let w_bigram = bigram(s.split_whitespace());
    let c_bigram = bigram(s.chars());
    println!("単語 bi-gram: {:?}", w_bigram);
    println!("文字 bi-gram: {:?}", c_bigram);
}
