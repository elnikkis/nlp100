fn bigram_word(sentence: &str) -> Vec<(&str, &str)> {
    sentence.split_whitespace().zip(
        sentence.split_whitespace().skip(1)).collect()
}
fn bigram_char(sentence: &str) -> Vec<(char, char)> {
    sentence.chars().zip(
        sentence.chars().skip(1)).collect()
}

// impl traitがrustに実装されていないので、interfaceみたいなIteratorを返す関数というのは書けない
// なのでVecを返すようにしようとしたけど、今度はVec<char>をVec<&str>に変換するのができない
//fn bigram(list: Vec<String>) -> Vec<(String, String)> {
//    let prev = list[0];
//
//    let mut ret = Vec::new();
//    for v in list.into_iter().skip(1) {
//        ret.push((prev, v));
//        //ret.push(v);
//    }
//    ret
//}

fn main() {
    let s = "I am an NLPer";
    let w_bigram = bigram_word(&s);
    let c_bigram = bigram_char(&s);

    //let w_bigram = bigram(s.split_whitespace().collect());
    //let c_bigram = bigram(s.chars().map(|c| &(c.to_string())).collect());

    //let w_bigram: Vec<_> = s.split_whitespace().zip(s.split_whitespace().skip(1)).collect();
    //let c_bigram: Vec<_> = s.chars().zip(s.chars().skip(1)).collect();

    println!("単語 bi-gram: {:?}", w_bigram);
    println!("文字 bi-gram: {:?}", c_bigram);
}
