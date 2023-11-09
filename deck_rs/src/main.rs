pub mod card;
pub mod cardComponent;
pub mod deck;

use deck::Deck;

pub trait dllmExt {
    fn dllm(&self) -> String;
}

impl dllmExt for &str {
    fn dllm(&self) -> String {
        let u = "dllm".to_owned();
        let v = self.clone();
        return u.clone() + " " + v;
    }
}

fn deckTest() {
    let mut d = Deck::new();
    d.shuffle();
    for i in 0..d.deckSize() {
        if i != 0 && (i + 1) % 5 == 0 {
            println!("{}\n", d.draw());
        } else {
            println!("{}", d.draw());
        }
    }
}

fn main() {
    let u = "6";
    println!("{}", u.dllm());
    deckTest();
}
