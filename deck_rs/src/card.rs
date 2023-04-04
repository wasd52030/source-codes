#[path="./cardComponent.rs"]
pub mod cardComponent;

pub mod card {
    use crate::cardComponent::{Face, Suit};
  

    #[derive(Debug)]
    pub struct Card {
        face: Face,
        suit: Suit,
    }

    impl Card {
        pub fn new(f: Face, s: Suit) -> Card {
            Card { face: f, suit: s }
        }
    }

    impl std::fmt::Display for Card {
        fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
            write!(f, "{}-{}", self.face, self.suit)
        }
    }
}
