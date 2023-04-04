pub mod cardComponent;
pub mod card;
pub mod deck;

use deck::Deck;


fn deckTest(){
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
    deckTest();
}
