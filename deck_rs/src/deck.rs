#[path = "./card.rs"]
pub mod card;

#[path = "./cardComponent.rs"]
pub mod cardComponent;

use rand::seq::SliceRandom;
use strum::IntoEnumIterator;

use crate::{
    card::card::Card,
    cardComponent::{Face, Suit},
};

pub struct Deck {
    list: Vec<Card>,
}

impl Deck {
    pub fn new() -> Deck {
        let mut list = Vec::new();
        for f in Face::iter() {
            for s in Suit::iter() {
                list.push(Card::new(f, s))
            }
        }

        Deck { list: list }
    }

    pub fn deckSize(&self) -> usize {
        self.list.len()
    }

    pub fn shuffle(&mut self) {
        let mut rng = rand::thread_rng();
        self.list.shuffle(&mut rng);
    }

    pub fn draw(&mut self) -> Card {
        if !self.list.is_empty() {
            return self.list.remove(0);
        }
        panic!("No Cards in Deck")
    }
}
